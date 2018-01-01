import os
import json
from random import randrange
from django.shortcuts import render
from django.conf import settings
from dateutil import parser
import random
from newsapp.utils import finds_item_in_array_based_on_keyvalue


content_api = os.path.join(settings.STATIC_ROOT, 'content_api.json')
content_data = json.load(open(content_api))

for result in content_data["results"]:
    # created new parts of dictionary so we don't modify any part of the existing dictionary and save ourselfs a deepcopy
    result["article_type_pretty"] = result["article_type"].replace("-", " ")
    result["path_pretty"] = result["path"].replace(".aspx", "")
    result["publish_date_pretty"] = parser.parse(result["publish_at"]).strftime("%d %B %y")

def index(request):
    '''
        this code could be rewritten if we matched by "article_type": "10-promise-series" 
        instead of looping through the tags... this would also stop the double break, but the instructions said match
        to the tag, so I kept it as that for now. 
    '''
    articles = content_data["results"][:]
    number_of_articles_to_display = 3
    featured = {}
    for article in articles:
        for tag in article["tags"]:
            if tag["slug"] == "10-promise":
                featured = article
                break
        if bool(featured):
            break

    articles.remove(featured)
    random.shuffle(articles)
    articles = articles[0:number_of_articles_to_display]
    context = {
        'featured': featured,
        'articles': articles
    }
    return render(request, 'newsapp/page-home.html', context)

def investing(request, year, month, day, slug):
    url = "/investing/%s/%s/%s/%s.aspx" % (year, month, day, slug)
    context = finds_item_in_array_based_on_keyvalue(content_data["results"], "path", url)
    return render(request, 'newsapp/post-investing.html', context)

def blog(request):
    context = {'articles': content_data["results"]}
    return render(request, 'newsapp/page-blog.html', context)

