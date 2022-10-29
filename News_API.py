import requests
from sys import argv
from API_KEY import ApiKey


def search_Top_by_cat(category_data):
    url = ('https://newsapi.org/v2/top-headlines?')
    parameters = {
        'category': category_data,
        "country": 'in',
        "apiKey": ApiKey
    }
    article_data(parameters, url)


def article_data(parameters, url):
    # print(url)
    resp = requests.get(url, params=parameters)
    arti = resp.json()['articles']
    result = []

    for data in arti:
        result.append({
            "author" : data['author'],
            "title" : data["title"],
            "description" : data["description"],
            "content" : data["content"],
            "link" : data['url']
            })
    for x in result:
        print("Author:",x['author'])
        print("Title:",x['title'])
        print("Description:",x['description'])
        print("Contents:",x['content'])
        print("Links/URL:",x['link'])
        print(" ")


def search_by_keyElements(name):
    url = ('https://newsapi.org/v2/everything?')
    parameters = {
        'q' : name,
        'apiKey' : ApiKey
    }
    article_data(parameters, url)


if __name__ == '__main__':
    search_Top_by_cat(argv[1])
    search_by_keyElements(argv[1])
