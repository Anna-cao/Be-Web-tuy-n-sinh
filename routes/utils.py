
import os, sys, logging
from flask import request, jsonify
from flasgger import swag_from
from functools import wraps
from database import db
from typing import Callable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#Swagger Config 
SWAGGER_CONFIG = {
    "common_responses": {
        "200": {"description": "Success", "schema": {"type": "object"}},
        "201": {"description": "Created", "schema": {"type": "object"}},
        "400": {"description": "Invalid input data"},
        "404": {"description": "Not found"}
    },
    "params": {
        "create": [{"in": "body", "name": "body", "required": True,
                    "schema": {"type": "object"}}],
        "update": [{"in": "path", "name": "{id}", "required": True, "type": "string"},
                   {"in": "body", "name": "body", "required": True,
                    "schema": {"type": "object"}}],
        "get_by_id": [{"in": "path", "name": "{id}", "required": True, "type": "string"}],
        "delete": [{"in": "path", "name": "{id}", "required": True, "type": "string"}],
        "get_all": [{"in": "query", "name": "page", "type": "integer", "default": 1},
                    {"in": "query", "name": "limit", "type": "integer", "default": 10}]
    }
}
ENDPOINTS = {
    "create": ("Create a new {model}", ["201", "400"]),
    "get_all": ("Get all {model}s", ["200"]),
    "get_by_id": ("Get {model} by ID", ["200", "404"]),
    "update": ("Update {model} by ID", ["200", "404"]),
    "delete": ("Delete {model} by ID", ["200", "404"])
}

def swagger_decorator(endpoint: str, model: str, id_param="id") -> Callable:
    def decorator(f: Callable) -> Callable:
        @wraps(f)
        def wrapper(*a, **kw): return f(*a, **kw)
        summary, resp_keys = ENDPOINTS[endpoint]
        params = SWAGGER_CONFIG["params"][endpoint]
        processed = []
        for p in params:
            q = dict(p)
            if "{id}" in q.get("name", ""):
                q["name"] = q["name"].replace("{id}", id_param)
            processed.append(q)
        responses = {c: SWAGGER_CONFIG["common_responses"][c] for c in resp_keys}
        return swag_from({
            "summary": summary.format(model=model.lower()),
            "parameters": processed,
            "responses": responses
        }, validation=False)(wrapper)
    return decorator

#Helper 
def make_response(api_schema, success: bool, message: str, data=None, status=200):
    return jsonify(api_schema.dump({"success": success, "message": message, "data": data})), status

def paginate_query(query, page, limit):
    total, items = query.count(), query.limit(limit).offset((page-1)*limit).all()
    return items, {"page": page, "limit": limit, "total_items": total,
                   "total_pages": (total+limit-1)//limit,
                   "has_next": page*limit < total, "has_prev": page > 1}

#CRUD Handler
def crud_handler(model, create_schema, update_schema, response_schema, api_response_schema, id_param="id"):
    cs, us, rs, api = create_schema(), update_schema(), response_schema(), api_response_schema()

    def get_all():
        p,l=request.args.get('page',1,int),request.args.get('limit',10,int)
        items,pag=paginate_query(model.query,p,l)
        logging.debug(f"{len(items)} {model.__name__} on page {p}")
        return make_response(api,True,f"List of all {model.__name__.lower()}s",
                             {"items":[rs.dump(i) for i in items],"pagination":pag})

    def get_by_id(i): return make_response(api,True,f"{model.__name__} found",rs.dump(model.query.get_or_404(i)))
    def create():
        obj=model(**cs.load(request.json)); db.session.add(obj); db.session.commit()
        return make_response(api,True,f"{model.__name__} created",rs.dump(obj),201)
    def update(i):
        obj=model.query.get_or_404(i); [setattr(obj,k,v) for k,v in us.load(request.json).items()]
        db.session.commit(); return make_response(api,True,f"{model.__name__} updated",rs.dump(obj))
    def delete(i):
        obj=model.query.get_or_404(i); db.session.delete(obj); db.session.commit()
        return make_response(api,True,f"{model.__name__} {i} deleted")

    return (swagger_decorator("get_all",model.__name__)(get_all),
            swagger_decorator("get_by_id",model.__name__,id_param)(get_by_id),
            swagger_decorator("create",model.__name__)(create),
            swagger_decorator("update",model.__name__,id_param)(update),
            swagger_decorator("delete",model.__name__,id_param)(delete))
