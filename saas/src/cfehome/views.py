import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    my_title = "My Page"
 
    my_context = {
        'page_title': my_title,
        'pagevisit' : queryset.count()
    }
    html_template = "home.html"
    PageVisit.objects.create()
    return render(request, html_template, my_context)



# def base_page_view(request, *args, **kwargs):
#     my_title = "My Page"
#     my_context = {
#         'page_title': my_title
#     }
#     html_template = "base.html"
#     return render(request, html_template, my_context)
