import json
import os.path
from datetime import datetime, timedelta
from typing import Optional


def read_file() -> Optional[dict]:
    current_date = (datetime.utcnow() + timedelta(hours=9)).isoformat()[:10]
    try:
        f = open(f"./{current_date}", 'r')
        a = f.readline()

    except:
        return None

    return json.loads(a)


def read_file_byDate(date_day) -> Optional[dict]:
    str_day = str(date_day)
    if date_day < 10:
        str_day = "0" + str(date_day)
    current_date = (datetime.utcnow() + timedelta(hours=9)).isoformat()[:8] + str_day
    file = f"./{current_date}"
    if not os.path.isfile(file):
        return None
    try:
        f = open(f"./{current_date}", 'r')
        a = f.readline()

    except:
        return None

    return json.loads(a)


def write_file(result: dict) -> None:
    current_date = (datetime.utcnow() + timedelta(hours=9)).isoformat()[:10]
    f = open(f"./{current_date}", 'w')

    f.write(json.dumps(result))
    f.close()


def check_custom_price_under() -> bool:
    return True
