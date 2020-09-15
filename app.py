from flask import Flask, render_template
from newsapi import NewsApiClient




app = Flask(__name__)



@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="75448b4e83b542a1b7f5b61ff76e6b52")
    topheadlines = newsapi.get_sources()

    # print(topheadlines)
    articles = topheadlines['sources']
    # print(articles)
    name = []
    desc = []
    url = []
    url = []
    category=[]
    id=[]


    for i in range(len(articles)):
        myarticles = articles[i]


        name.append(myarticles['name'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])
        category.append(myarticles['category'])
        id.append(myarticles['id'])



    mylist = zip(name, desc, url,category,id)
    # print(mylist)

    return render_template('index.html', context = mylist)



@app.route('/sources/<source>')
def article(source):
    newsapi = NewsApiClient(api_key="75448b4e83b542a1b7f5b61ff76e6b52")
    topheadlines = newsapi.get_top_headlines(sources=source)

    articles = topheadlines['articles']
    print(articles)

    desc = []
    news = []
    img = []
    author=[]
    url=[]

    for i in range(len(articles)):
        myarticles = articles[i]
        
        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        author.append(myarticles['author'])
        url.append(myarticles['url'])


        

    mylist = zip(news, desc, img,author,url)

    return render_template('source.html', context=mylist,source=source)



if __name__ == "__main__":
     app.run(debug=True) 