# -*- coding: utf-8 -*-
import datetime, xmlrpclib

wp_url = "http://www.comiha.ir/xmlrpc.php"
wp_username = "##username##"
wp_password = "##password##"
wp_blogid = ""

status_draft = 0
status_published = 1

server = xmlrpclib.ServerProxy(wp_url)

title = ""
content = open("matlab.txt")
date_created = xmlrpclib.DateTime(datetime.datetime.strptime("2000-10-20 21:08", "%Y-%m-%d %H:%M"))
categories = ["Other"]
tags = ["sometag", "othertag"]
data = {'title': title, 'description': content.read(), 'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags}

post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)
