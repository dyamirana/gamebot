# -*- coding: utf-8 -*-
import os
import urlparse


#[vk settings]
group_id=os.environ.get('groupid',149222864)
token = os.environ.get('token','f91c78c67db7f79f09d405bfd15b5939d073dfa3edb52d2d0439b8eba73b800e2bc30fc0e4aaa3d810287')


#[platform settings]
db=True
debug=True
if 'DATABASE_URL' in os.environ:
    db_url=os.environ.get('DATABASE_URL','postgres://gamebot:VqWPz8ugAy5pu18d@35.189.224.206:5432/gamebot')
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
leave_mes=u'Эх , зря. Теперь я не смогу тебе прислать новое отличие, которое уже готовится для тебя и почти готово 😔\nМожет, подпишешься обратно?😋'

#[gamebot settings]
album=os.environ.get('album','183156791_245737307')
lives=int(os.environ.get('lives',5))
