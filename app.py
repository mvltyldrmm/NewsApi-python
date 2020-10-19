from flask import Flask,render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="yourapikey")
    topheadlines = newsapi.get_top_headlines(country="tr")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    content = []
    url =[]
    date = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['content'])
        url.append(myarticles['url'])
        date.append(myarticles['publishedAt'])
    mylist = zip(news,desc,img,content,url,date)

    return render_template('index.html',context = mylist)


if __name__ == "__main__":
    app.run(debug=True)
