from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import sqlite3
from suntzu_artofwar.models import ChaptersTranslation, Comments
# Create your views here.


def index(request):
    chapters = range(1,14)
    return render_to_response('main_page.html', {'chapters':chapters})

def all_book(request):
    """Function to open all_book page."""
    chapters_number = range(1, 14)
    chapter_objects = []
    for i in range(1, 14):
        chapter_objs = Comments.objects.filter(chapter=i)
        chapter_objects.append(chapter_objs)
    return render_to_response('book.html', {'chapters': chapters_number,
                                            'all_content': chapter_objects})