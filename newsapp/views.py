import os
import json
from random import randrange
from django.shortcuts import render
from django.conf import settings


content_api = os.path.join(settings.STATIC_ROOT, 'content_api.json')
content_data = json.load(open(content_api))

for result in content_data["results"]:
    # created new parts of dictionary so we don't modify any part of the existing dictionary and save ourselfs a deepcopy
    result["article_type_pretty"] = result["article_type"].replace("-", " ")
    result["path_pretty"] = result["path"].replace(".aspx", "")

def index(request):

    # this code could be rewritten if we matched by "article_type": "10-promise-series" instead of looped through the tags
    for result in content_data["results"]:
        featured = {}
        for tag in result["tags"]:
            if tag["slug"] == "10-promise":
                featured = result
                break
        if bool(featured):
            break
    
    articles = []
    while(len(articles) < 3):
        # Little heavy of a one liner, inside working out, it:
        # # - figures out how many items are in the results array
        # # - uses that as the max for random number generation
        # # - uses that as to select an item from the results array
        article_to_add = content_data["results"][randrange(len(content_data["results"]))]
        if article_to_add["uuid"] != featured["uuid"] and article_to_add not in articles:
            articles.append(article_to_add)

    context = {
        'results': content_data["results"],
        'featured': featured,
        'articles': articles
    }
    return render(request, 'newsapp/page-home.html', context)

def investing(request, year, month, day, slug):
    url = "/investing/%s/%s/%s/%s.aspx" % (year, month, day, slug)
    for article in content_data["results"]:
        print("url  -", url)
        print("path -", article["path"])
        if article["path"] == url:
            context = article
            break
        
    return render(request, 'newsapp/post-investing.html', context)

def blog(request):
    context = {'articles': content_data["results"]}
    return render(request, 'newsapp/page-blog.html', context)