from django.db import models

# Create your models here.



class ChaptersTranslation(models.Model):

    chapter = models.PositiveIntegerField(verbose_name='chapter')
    sub_chapters = models.CharField(max_length=10, verbose_name='sub_chapters')
    translator = models.CharField(max_length=200, verbose_name='translator')
    translation = models.CharField(max_length=2000, verbose_name='translations')

    def __unicode__(self):
        return str(self.chapter)

class Comments(models.Model):

    chapter = models.PositiveIntegerField(verbose_name='chapter')
    sub_chapters = models.PositiveIntegerField(verbose_name='sub_chapter')
    sub_content = models.CharField(max_length=2000, default='-', verbose_name='chapter_content')
    commentator = models.CharField(max_length=2000, verbose_name='commentator')
    comment = models.CharField(max_length=2000, verbose_name='comment')
    com_translator = models.CharField(max_length=2000, verbose_name='trans_commentator', blank=True)
    com_translation = models.CharField(max_length=2000, verbose_name='com_translation', blank=True)

    def __unicode__(self):
        return str(self.chapter)