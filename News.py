import requests

api_address="https://newsapi.org/v2/top-headlines?country=us&apiKey=1617785d276d4e80a8b6bef4df727c79"

json_data=requests.get(api_address).json()

ar=[]

def news():
    for i in range(3):
        ar.append("Number "+str(i+1)+", " + json_data['articles'][i]['title']+".")

    return ar

arr=news()
