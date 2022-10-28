import requests
from sys import argv
from API_KEY import ApiKey

url = ('https://newsapi.org/v2/top-headlines?')

def search_by(category):
    paramaters = {
        'category': category,
        "country": 'in',
        "apiKey": ApiKey
    }

    resp = requests.get(url, params=paramaters)
    arti = resp.json()['articles']
    result = []

    for data in arti:
        result.append({
            "author" : data['author'],
            "title" : data["title"],
            "description" : data["description"],
            "content" : data["content"]
            })
    for x in result:
        print("Author:",x['author'])
        print("Title:",x['title'])
        print("Description:",x['description'])
        print("Contents:",x['content'])
        print(" ")


if __name__ == '__main__':
    search_by(argv[1])
