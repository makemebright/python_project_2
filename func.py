from bs4 import BeautifulSoup
import requests
import json


def get_first_receipts(from_url):
    request = requests.get(url=from_url)
    soup = BeautifulSoup(request.text, "html.parser")
    receipts = soup.find_all("h3", class_="horizontal-tile__item-title item-title")

    receipts_arr = []
    for receipt in receipts:
        receipt_url = f'https://eda.ru{receipt.find("a")["href"]}'
        receipts_arr.append(receipt_url)

    # return receipts_dict

    # print(receipts_dict)
    with open("receipts_dict.json", "w") as file:
        json.dump(receipts_arr, file, indent=4)


def write_to_json(name, url):
    with open("user_books.json", 'r') as jfr:
        jf_file = json.load(jfr)
    with open("user_books.json", 'w') as jf:
        if name not in jf_file.keys():
            jf_file[name] = []
            json.dump(jf_file, jf, indent=4)
            return
        if url in jf_file[name]:
            json.dump(jf_file, jf, indent=4)
            return
        if not url:
            json.dump(jf_file, jf, indent=4)
            return
        jf_file[name].append(str(url))
        json.dump(jf_file, jf, indent=4)

