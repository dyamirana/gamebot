# -*- coding: utf-8 -*-
import settings
import utils
import apifunc
from plugins import gamebot
from random import choice
import time

def answers(helper,text,user_id,attachments,message,user):
    ### PUT UR ANSWERS HERE ###

    if u'начать игру' in text or u'продолж' in text:
        if len(user) <1:
            utils.insert_users(id=user_id,member=helper.api.groups.isMember(group_id=settings.group_id, user_id=user_id), mesallow=0, time=0, game=1, lives=settings.lives, score=0,
                               pics='[]', answer='')
            user = utils.getusers(id=user_id)
        if user[0]['time'] > time.time() or user[0]['lives'] <= 0:
            helper.send_message(user_id=user_id, message=u'У тебя зкончились жизни, подожди 24 часа.')
            return
        if user[0]['lives'] <= 0 and user[0]['time'] < time.time():
            helper.send_message(user_id=user_id, message=u'Отлично! Теперь у тебя снова '+u'💜'*settings.lives+u' жизней')
            utils.insert_users(id=user_id, lives=settings.lives)
        utils.insert_users(id=user_id, game=1)
        photo = gamebot.get_photo(user[0])
        if photo is None:
            helper.send_message(user_id=user_id, message=u'У меня закончились картинки, зайди попозже!')
            return
        helper.send_message(user_id=user_id,message=u'Найди все отличия и напиши их количество!',attachments=photo['photo'])
        return

    if len(user)>0:

        if text.isdigit():
            if user[0]['lives'] <= 0 and user[0]['time'] < time.time():
                helper.send_message(user_id=user_id,
                                    message=u'Отлично! Теперь у тебя снова ' + u'💜' * settings.lives + u' жизней')
                utils.insert_users(id=user_id, lives=settings.lives)
                user = utils.getusers(id=user_id)
            if user[0]['time'] > time.time():
                helper.send_message(user_id=user_id, message=u'У тебя зкончились жизни, подожди 24 часа.')
                return


            if user[0]['game']==0:
                helper.send_message(user_id=user_id, message=u'У тебя не активна игра, напиши "начать игру"')
                return
            if text == user[0]['answer']:
                utils.insert_users(id=user_id, score=user[0]['score'] + user[0]['lives'],game=0,answer='')
                helper.send_message(user_id=user_id, message=u'Верно!'+u'\nТвой счет: '+str(user[0]['score'] + user[0]['lives'])+u'\nЧтобы продолжить игру напиши "продолжить"')
                return
            else:
                lives = user[0]['lives'] - 1
                if lives<=0:
                    helper.send_message(user_id=user_id, message=u'Неправильно!\nУ тебя зкончились жизни, подожди 24 часа.')
                    utils.insert_users(id=user_id,lives=0,time=time.time()+1)
                    return
                utils.insert_users(id=user_id, lives=lives)
                helper.send_message(user_id=user_id, message=u'Неправильно!\nУ тебя осталось '+u'💜'*lives+u' жизней')
                return
        elif text in [u'счёт',u'счет']:
            helper.send_message(user_id=user_id, message=u'Твой счет: '+ str(user[0]['score'])+u' 📊')
            return
        elif u'жизн' in text:
            if user[0]['lives'] == 0:
                helper.send_message(user_id=user_id, message=u'У тебя 0 жизней')
                return
            helper.send_message(user_id=user_id, message=u'У тебя ' + u'💜' * user[0]['lives'] + u' жизней')
            return
        else:
            helper.send_message(user_id=user_id, message=u'Я тебя не понимаю! Если хочешь сыграть в игру, напиши "начать игру". \nИли же "счет" или "жизни" чтобы узнать свою статистику')
            return
    helper.send_message(user_id=user_id,
                        message=u'Я тебя не понимаю! Если хочешь сыграть в игру, напиши "начать игру". \nИли же "счет" или "жизни" чтобы узнать свою статистику')
    return
class MessageModule:
    def __init__(self,api):
        self.api = api
        self.functions = apifunc.Functions(api)
        self.send_message = self.functions.send_message

    def answer(self,message):
        user_id = message.user_id
        mess_time = message.date
        read_state = message.read_state

        try:
            text = message.body
        except AttributeError:
            text = ''
        try:
            attachments = []
            for i in message.attachments:
                tpe = {'attype': i['type']}
                tpe.update(i[i['type']])
                attachments.append(tpe)
                del tpe
        except AttributeError:
            attachments = []
        except TypeError:
            attachments = []
        user = utils.getusers(id=user_id)

        if len(user) < 1:
            utils.insert_users(id=user_id, member=self.api.groups.isMember(group_id=settings.group_id, user_id=user_id), mesallow=0, time=0, game=0, lives=settings.lives, score=0,
                               pics='[]', answer='')
            user = utils.getusers(id=user_id)
        if settings.joinpls != '':
            if len(user)<1:
                if self.api.groups.isMember(group_id=settings.group_id, user_id=user_id) == 0:
                    utils.insert_users(id=user_id, member=0, mesallow=1, time=0, game=0, lives=settings.lives, score=0,
                               pics='[]', answer='')
                    self.send_message(user_id=user_id, message=settings.joinpls)
                    return
                else:
                    utils.insert_users(id=user_id, member=1, mesallow=1)

            elif self.api.groups.isMember(group_id=settings.group_id, user_id=user_id) == 0:
                utils.insert_users(id=user_id, member=0, mesallow=1, time=0, game=0, lives=settings.lives, score=0,
                               pics='[]', answer='')
                self.send_message(user_id=user_id, message=settings.joinpls)
                return

        answers(self,text.lower(),user_id,attachments,message,user)






