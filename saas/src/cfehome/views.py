import pathlib
from django.http import HttpResponse
from django.shortcuts import render

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        'page_tile': my_title
    }
    html_template = "home.html"
    return render(request, html_template)


def old_home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        'page_tile': my_title
    }
    html_ = ""


    # html_file_path = this_dir/"home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)
