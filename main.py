from config import PRICE_THRESHOLD
from db import write_file, read_file
from graph import draw_graph
from slack import post_massage, post_ban_massage
from worker import get_crawling_result

if __name__ == "__main__":

    URL = "https://www.kayak.co.kr/flights/SEL-CJU/2022-05-20?" \
          "fs=takeoff=1830,2030;" \
          "providers=AWEBTOURDOMESTIC,ONLINETOURDOMESTIC,TW,MODETOURDOMESTIC,OZ,7C,BUDGETAIR,CTRIPAIR,KE,LJ" \
          "&sort=bestflight_a"

    result = get_crawling_result(url=URL)[0]

    if result['price'] > PRICE_THRESHOLD:
        post_massage(result=result)

    today_result = read_file()
    if not today_result:
        write_file(result=result)

    else:
        if today_result['price'] > result["price"]:
            write_file(result=result)
    draw_graph()