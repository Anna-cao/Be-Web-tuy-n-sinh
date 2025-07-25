from flask import Blueprint, Response
import json
from app.db_connection import get_connection  

exam_groups_bp = Blueprint('exam_groups', __name__)

@exam_groups_bp.route("/exam_groups")
def get_exam_groups():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM EXAM_GROUPS")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]

    cursor.close()
    conn.close()

    json_data = json.dumps(data, ensure_ascii=False)
    return Response(json_data, content_type="application/json; charset=utf-8")
