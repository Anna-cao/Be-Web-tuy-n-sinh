from flask import Blueprint, Response
import json
from app.db_connection import get_connection
from app.schemas.major_schema import MajorSchema

majors_bp = Blueprint("majors", __name__)
schema = MajorSchema(many=True)

@majors_bp.route("/majors")
def get_majors():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM MAJORS")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]

    cursor.close()
    conn.close()

    json_data = json.dumps(schema.dump(data), ensure_ascii=False)
    return Response(json_data, content_type="application/json; charset=utf-8")
