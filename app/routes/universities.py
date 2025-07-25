from flask import Blueprint, Response
import json
from app.db_connection import get_connection
from app.schemas.university_schema import UniversitySchema

universities_bp = Blueprint("universities", __name__)
schema = UniversitySchema(many=True)

@universities_bp.route("/universities")
def get_universities():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM UNIVERSITIES")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]

    cursor.close()
    conn.close()

    json_data = json.dumps(schema.dump(data), ensure_ascii=False)
    return Response(json_data, content_type="application/json; charset=utf-8")

