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
    """Function to open all_book page.
    :return render to response: html to all book, dictionary:
    {chapters_number}
    """
    chapters_number = range(1, 14)
    chapter_objects = []
    translations = []
    for i in range(1, 14):
        chapter_objs = Comments.objects.filter(chapter=i)
        if i == 1:  # if it's first chapter
            translations = first_chapter_translation()
        chapter_objects.append(chapter_objs)
    return render_to_response('book.html', {'chapters': chapters_number,
                                            'all_content': chapter_objects,
                                            'sub_translations': translations})

def chapter(request, chapter):
    """Universal function for all chapters"""
    chapters_number = range(1, 14)
    chapter_objs = Comments.objects.filter(chapter=chapter)
    translations = []
    if chapter_objs[0].chapter == 1: # if it's first chapter
        translations = first_chapter_translation()
    return render_to_response('chapter.html', {'chapters': chapters_number,
                                               'chapter_info': chapter_objs,
                                               'sub_translations': translations})


def first_chapter_translation():
    """First chapter. Process """
    translate_objects = []
    translate_chapter = ChaptersTranslation.objects.all()
    current_sub = '2-3'
    current_sub_trans = []
    for obj in translate_chapter:
        if obj.sub_chapters == current_sub:
            current_sub_trans.append(obj)
        else:
            translate_objects.append((current_sub_trans, current_sub))
            current_sub_trans = []
            current_sub = obj.sub_chapters
    return translate_objects