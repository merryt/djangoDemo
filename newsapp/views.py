import os
import json
from random import randrange
from django.shortcuts import render
from django.conf import settings
from dateutil import parser


content_api = os.path.join(settings.STATIC_ROOT, 'content_api.json')
content_data = json.load(open(content_api))

for result in content_data["results"]:
    # created new parts of dictionary so we don't modify any part of the existing dictionary and save ourselfs a deepcopy
    result["article_type_pretty"] = result["article_type"].replace("-", " ")
    result["path_pretty"] = result["path"].replace(".aspx", "")
    result["publish_date_pretty"] = parser.parse(result["publish_at"]).strftime("%d %B %y")

def index(request):
    results = content_data["results"]
    number_of_articles_to_display = 3
    # this code could be rewritten if we matched by "article_type": "10-promise-series" instead of looped through the tags
    featured = {}
    for result in results:
        # create new function that is "finds item in array based on keyvalue"
        for tag in result["tags"]:
            if tag["slug"] == "10-promise":
                featured = result
                break
        if bool(featured):
            break
    
    # clone the array,  then random `random.shuffle(array)` then grab first 3 (make sure I remove 10-promise from above)
    
    articles = []
    while(len(articles) < number_of_articles_to_display):
        length_of_array = len(results)
        random_index_in_results = randrange(length_of_array)
        article_to_add = results[random_index_in_results]
        if article_to_add["uuid"] != featured["uuid"] and article_to_add not in articles:
            articles.append(article_to_add)

    context = {
        'results': results,
        'featured': featured,
        'articles': articles
    }
    return render(request, 'newsapp/page-home.html', context)

def investing(request, year, month, day, slug):
    url = "/investing/%s/%s/%s/%s.aspx" % (year, month, day, slug)
    # create new function that is "finds item in array based on keyvalue"
    for article in content_data["results"]:
        if article["path"] == url:
            context = article
            break
        
    return render(request, 'newsapp/post-investing.html', context)

def blog(request):
    context = {'articles': content_data["results"]}
    return render(request, 'newsapp/page-blog.html', context)