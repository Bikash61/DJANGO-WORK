import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    total_qs = PageVisit.objects.all()
    qs = PageVisit.objects.filter(path = request.path)
    my_title = "My Page"
 
    my_context = {
        'page_title': my_title,
        'page_visit_count' : qs.count(),
        'total_page_visit_count' : total_qs.count(),
        'percent': (qs.count()*100/total_qs.count())
    }
    path = request.path
    print("path",path)
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)



