# 공공 데이터 open API 실습

import requests

url = "http://openapi.seoul.go.kr:8088/6e41516150756e753130367a5a6a5259/json/GetParkInfo/1/1000"

response = requests.get(url)

response_json = response.json()

json_keys = response_json["GetParkInfo"].keys()

data_row = response_json["GetParkInfo"]["row"]


# print(len(new_data))
# print(new_data[0])


def get_data(gu: str) -> list:
    new_data = list()
    for data in data_row:
        place = data["ADDR"]
        if gu in place:
            new_data.append(data)
        else:
            pass

    return new_data


print(get_data("강남구"))
