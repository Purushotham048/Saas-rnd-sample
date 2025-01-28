from django.shortcuts import render
from django.http import HttpResponse
import pathlib
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path = request.path)
    my_title ="It's working"
    html_template = "home_page.html"
    try:
        percent = (page_qs.count()*100.0)/qs.count()
    except:
        percent = 0

    my_context={
        "page_title":my_title,
        "page_visit_count": qs.count(),
        "total_visit_count": page_qs.count(),
        "percent": percent
    }

    PageVisit.objects.create(path = request.path)
    path = request.path
    print("path", path)
    return render(request, html_template, my_context)

def my_old_home_page_view(request, *args, **kwargs):
    my_title ="My Page"
    my_context ={
        "page_title":my_title
    }
    html_ = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple HTML Page</title>
</head>
<body>
    <h1>Welcome to {page_title}</h1>
    <p>This is a simple HTML page.</p>
    <a href="https://www.google.com" target="_blank">Visit Google</a>
</body>
</html>

    """.format(**my_context)
    #html_file_path = this_dir/"home_page.html"
    #html_ = html_file_path.read_text()
    return HttpResponse(html_)