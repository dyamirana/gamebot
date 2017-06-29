# -*- coding: utf-8 -*-
import os
import urlparse


#[vk settings]
group_id=os.environ.get('groupid',141410969)
token = os.environ.get('token','740f3f24062cf595ba12a8e5862c270814f4a5d7d7ab2a4001c5c45438d1881dea2d3d79124b4d0b670aa')


#[platform settings]
db=False
debug=True
if 'DATABASE_URL' in os.environ:
    db_url=os.environ.get('DATABASE_URL')
else:
    db_url = 'sqlite:////' + os.path.dirname(__file__) + '/databases/users.db'
if 'appname' in os.environ:
    host = 'https://'+os.environ.get('appname')+'.herokuapp.com'
else:
    host = 'http://vps.kadabot.tk'

#[join-leave module]
join = True
join_mes=u'Cпасибо за подписку! Чтобы начать игру напиши "начать игру"'

joinpls=u'Чтобы поиграть ты должен вступить в группу'

leave = True
leave_mes=u'Пока!'

#[gamebot settings]
album=os.environ.get('album','183156791_245737307')
lives=int(os.environ.get('lives',5))
