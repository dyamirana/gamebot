#!/usr/bin/env python
# -*- coding: utf-8 -*-


import vk
import utils
import ast
import settings
import random

api = vk.API(vk.Session(access_token='083a5837083a583708657de735086fac9f0083a083a583750f2072e9bdc2096b3522ed0'), v=5.65, timeout=30)

def get_photo(user,replace=True):


    if len(user)<1:
        return None
    user_pic_list = ast.literal_eval(user['pics'])
    photos = api.photos.get(owner_id=settings.album.split('_')[0],album_id=settings.album.split('_')[1])
    if photos['count']==0:
        return None
    photos = photos['items']
    random.shuffle(photos)

    for i in photos:

        if i['id'] not in user_pic_list:
            if replace:
                user_pic_list.append(i['id'])
                utils.insert_users(id=user['id'],pics=str(user_pic_list),answer=i['text'])
            photo_attach = i
            photo_attach.update({'attype':'photo'})
            return {'photo':[photo_attach],'count':i[
                'text']}
        else:
            continue
    return None
