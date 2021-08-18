# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from savenovelsdate.models import NovelsData, NovelsChapter, Novels, NovelsType, User


class NovelsDataItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = NovelsData

class NovelsChapterItem(DjangoItem):

    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = NovelsChapter

class NovelsItem(DjangoItem):

    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = Novels

class TypeItem(DjangoItem):#2

    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    django_model = NovelsType

class UserItem(DjangoItem):

    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    django_model = User
