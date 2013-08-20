import os
import time


template = '''
Title: {title}
Date: {date}
Category: {category}
Tags: {tags}
Slug: {slug}
Author: Admalledd
Summary: {summary}



'''


def get_reply(msg,default= None,req=True):
    rep = raw_input(msg)
    if not rep:
        if default is not None:
            return default
        print "not a valid reply:%s"%rep
        return get_reply(msg,req)#recurse to try again?
    else:
        return rep

if __name__ == '__main__':
    print template.format(**{
        'title':get_reply("title of post:\n>>>"),
        'category':get_reply("Category of post (case matters)[Blog]:\n>>>",default='Blog'),
        'tags':get_reply("tags of post(case matters):\n>>>"),
        'slug':get_reply("slug/path/url of post(case matters):\n>>>"),
        'summary':get_reply("Summary of post:\n>>>"),
        'date':time.strftime('%Y-%m-%d %H:%M',time.localtime())

        })