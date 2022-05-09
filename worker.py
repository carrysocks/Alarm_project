import requests

from config import HEADERS
from slack import post_ban_massage


def get_crawling_result(url: str, max_retry: int = 20) -> list:
    result = []

    for i in range(max_retry):
        response = requests.post(url=url + '&1', headers=HEADERS, timeout=30)

        try:
            arr = response.json()["react"]["components"]
        except:
            continue

        for comp in arr:
            if comp["component"] != "ui/flights/results/components/FlightResultDetails":
                continue

            result.append(
                {"airline_name": comp["props"]["result"]["legs"][0]["segments"][0]["airline"]["name"],
                 "departure_time": comp["props"]["result"]["legs"][0]["segments"][0]["departure"]["isoDateTimeLocal"][
                                   11:],
                 "agency_name": comp["props"]["result"]["optionsByFare"][0]["options"][
                     0
                 ]["providerInfo"]["displayName"],
                 "price": int(
                     "".join(
                         comp["props"]["result"]["optionsByFare"][0]["options"][0][
                             "fees"
                         ]["totalPrice"][:-1].split(",")
                     )
                 ),
                 }
            )

        if result:
            break

        if i == (max_retry-1):
            post_ban_massage()
            raise BaseException("URL 밴 먹었다!!!!")

    return sorted(result, key=lambda a: a.get("price"))
