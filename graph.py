from datetime import datetime, timedelta

from db import read_file_byDate, read_file
from slack import post_message_graph

def draw_graph():
    current_day = int((datetime.utcnow() + timedelta(hours=9)).isoformat()[8:10])
    date = (datetime.utcnow() + timedelta(hours=9)).isoformat()[:8]
    result = []
    today_price = read_file().get("price")
    for i in range(7):
        dict = read_file_byDate(current_day - i)
        if dict == None:
            break
        result.append({**dict, **{"date": date + str(current_day - i).zfill(2)},
                       **{"price_diff": dict.get("price") - today_price}})
    result.reverse()
    for res in result:
        print(res)
        post_message_graph(res)
