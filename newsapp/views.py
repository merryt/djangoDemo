from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.conf import settings
import json
import os
from random import *

content_api = os.path.join(settings.STATIC_ROOT, 'content_api.json')
json_data = json.load(open(content_api))


def index(request):

    # this code could be rewritten if we matched by "article_type": "10-promise-series" instead of looped through the tags
    for result in json_data["results"]:
        featured = {}
        for tag in result["tags"]:
            if tag["slug"] == "10-promise":
                featured = result
                featured["article_type_pretty"] = featured["article_type"].replace("-", " ")
                # created new part of results so we don't modify the existing array
                featured["path_pretty"] = featured["path"].replace(".aspx", "")
                break
        if bool(featured):
            break
    
    articles = []
    while(len(articles) < 3):
        article_to_add = json_data["results"][randrange(len(json_data["results"]))]
        article_to_add["article_type_pretty"] = article_to_add["article_type"].replace("-", " ")
        article_to_add["path_pretty"] = article_to_add["path"].replace(".aspx", "")
        if article_to_add["uuid"] != featured["uuid"] and article_to_add not in articles:
            articles.append(article_to_add)
    context = {
        'results': json_data["results"],
        'featured': featured,
        'articles': articles
    }
    return render(request, 'newsapp/home.html', context)

def investing(request, year, month, day, slug):
    print("-------")
    url = "/investing/%s/%s/%s/%s.aspx" % (year, month, day, slug)

    for article in json_data["results"]:
        print("url  -", url)
        print("path -", article["path"])
        if article["path"] == url:
            context = article
            break
        else:
            context = {}
        
    return render(request, 'newsapp/investing.html', context)

