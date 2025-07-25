
from flask import Blueprint, Response
import json
from datetime import datetime
from app.db_connection import get_connection  

admission_scores_bp = Blueprint('admission_scores', __name__)

@admission_scores_bp.route("/admission_scores")
def get_admission_scores():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ADMISSION_SCORES")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    data = []
    for row in rows:
        row_dict = dict(zip(columns, row))
        for key, value in row_dict.items():
            if isinstance(value, datetime):
                row_dict[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        data.append(row_dict)

    cursor.close()
    conn.close()

    json_data = json.dumps(data, ensure_ascii=False)
    return Response(json_data, content_type="application/json; charset=utf-8")
