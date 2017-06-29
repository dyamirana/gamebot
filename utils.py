#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import os
import logging
import settings
import traceback
import time
import __builtin__
import dataset

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'bot.log')

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    def dic(self):
        return dict


def getusers(id=None):
    if settings.db:
        db = dataset.connect(settings.db_url,engine_kwargs={'pool_recycle': 30})
        table = db['users']
        if table.count()<1:
            return []
        if id is not None:

            user = table.find_one(id=id)

            return [user]
        else:
            user = []
            for i in table.all():
                user.append(i)
            return user

    if len(__builtin__.users) <1:
        return []
    if id is not None:
        returnusers = []
        users = __builtin__.users
        for i in users:
            if i['id'] == id:
                returnusers.append(i)
        return returnusers
    else:
        return __builtin__.users

def insert_users(id,**kwargs):
    if settings.db:
        db = dataset.connect(settings.db_url, engine_kwargs={'pool_recycle': 30})
        table = db['users']
        kwargs.update({'id':id})
        table.upsert(kwargs,['id'])
        db.commit()
        return
    user_data_dict = {'id': id}
    user_data_dict.update(kwargs)
    for i in __builtin__.users:
        if i['id'] == id:
            i.update(user_data_dict)
            return
    __builtin__.users.append(user_data_dict)



