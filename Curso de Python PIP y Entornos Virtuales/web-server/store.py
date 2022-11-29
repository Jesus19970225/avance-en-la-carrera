import requests

def get_categories():
    r = requests.get('https://tmohentai.com/section/all?search[searchText]=Ratatatat74&search[searchBy]=artist&exact=1')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category['name'])
