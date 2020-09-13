from flask import Flask, render_template
from newsapi import NewsApiClient




app = Flask(__name__)



@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_sources()

    # print(topheadlines)
    articles = topheadlines['sources']
    print(articles)
    name = []
    desc = []
    url = []
    url = []
    country=[]


    for i in range(len(articles)):
        myarticles = articles[i]


        name.append(myarticles['name'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])
        country.append(myarticles['country'])



    mylist = zip(name, desc, url,country)


    return render_template('index.html', context = mylist)



@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="YOUR-API-KEY")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render_template('bbc.html', context=mylist)



if __name__ == "__main__":
    app.run(debug=True)