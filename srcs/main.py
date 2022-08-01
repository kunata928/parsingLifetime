import requests
import csv
import json
from datetime import datetime


def collect_data():
    fileName = str(datetime.now().replace(microsecond=0)).replace(' ', '_')
    print(str(fileName))
    respone = requests.get("https://www.lifetime.plus/api/analysis2", )

    # with open(f'info_{fileName}.json', 'w') as file:
    #     json.dump(respone.json(), file, indent=4, ensure_ascii=False)

    categories = respone.json()['categories']
    result = list()
    for category in categories:
        categoryName = category['name']
        categoryItems = category['items']
        for item in categoryItems:
            itemName = item.get('name')
            itemPrice = item.get('price')
            itemDescription = item.get('description')
            itemWait = item.get('days')
            itemBio = item.get('biomaterial')
            result.append(
                [categoryName, itemName, itemBio, itemPrice, itemDescription, itemWait, ]
            )
    with open(f'info_{fileName}.csv', 'a') as file:
        writer = csv.writer(file)

        writer.writerow(
            ('Категория',
             'Анализ',
             'Биоматериал',
             'Цена, руб',
             'Описание',
             'Время ожидания в днях',
             )
        )

        writer.writerows(
            result
        )

def main():
    collect_data()


if __name__ == '__main__':
    main()