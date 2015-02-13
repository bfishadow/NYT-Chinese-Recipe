#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return NYTChinese

class NYTChinese(BaseFeedBook):
    title                 = u'纽约时报中文网'
    description           = u'包括“国际纵览”与“国际生活”两个全文 RSS Feeds 最近七天的文章'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_nytchinese.gif"
    coverfile             = "cv_nytchinese.jpg"
    oldest_article        = 7
    feeds = [
            (u'国际纵览', 'http://cn.nytimes.com/rss.html', True),
            (u'国际生活', 'http://cn.tmagazine.com/rss.html', True),
           ]
