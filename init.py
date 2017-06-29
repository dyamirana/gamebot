# -*- coding: utf-8 -*-

try:
    import settings
except:
    print 'Please create settings.py!'
    exit()
try:
    import vk
    import dataset
    import flask
    import antigate
    import sqlalchemy
    import logging

    logging.basicConfig()
except:
    print 'Please install requirements'
    exit()

if settings.db:
    try:
        db = dataset.connect(settings.db_url)
    except Exception as exp:
        print 'Error connecting to the database \n' + str(exp)
        exit()

    if 'users' not in db.tables:
        db.create_table(table_name='users',primary_id='id', primary_type='Integer')
        table = db['users']
        table.create_column('member', sqlalchemy.INT)
        table.create_column('mesallow',sqlalchemy.INT)
        table.create_column('time',sqlalchemy.INT)
        table.create_column('game',sqlalchemy.INT)
        table.create_column('lives',sqlalchemy.INT)
        table.create_column('score',sqlalchemy.INT)
        table.create_column('pics',sqlalchemy.TEXT)
        table.create_column('answer',sqlalchemy.TEXT)
        table.create_index(['id'])
