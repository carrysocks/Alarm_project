import json

import requests

from config import SLACK_TOKEN

def post_massage(result: dict):
    requests.post("https://slack.com/api/chat.postMessage",
                  headers={"Authorization": "Bearer " + SLACK_TOKEN},
                  data={"channel": "#항공",
                        "attachments": json.dumps([{"pretext": f"✈️ {result['price']}원 항공권이 등장!!", "text":
                            f"\n"
                            f"가격: {result['price']}\n원"
                            f"시간: {result['departure_time']}\n"
                            f"항공사: {result['airline_name']}\n"
                            f"대행사: {result['agency_name']}"}]), "color": "#f03e3e"
                        })

def post_message_graph(result: dict):
    requests.post("https://slack.com/api/chat.postMessage",
                  headers={"Authorization": "Bearer " + SLACK_TOKEN},
                  data={"channel": "#항공",
                        "attachments": json.dumps([{"pretext": "일주일 가격 추세", "text":
                            f"\n"
                            f"날짜: {result['date']}\n"
                            f"가격: {result['price']}원\n"
                            f"가격차이: {result['price_diff']}원\n"}]),
                        })


def post_ban_massage():
    requests.post("https://slack.com/api/chat.postMessage",
                  headers={"Authorization": "Bearer " + SLACK_TOKEN},
                  data={"channel": "#항공",
                        "text": "URL 밴 먹었어요 ㅜㅜ"})
