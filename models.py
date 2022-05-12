"""
This file defines the database models
"""
import datetime
from .common import db, Field, auth
from pydal.validators import *

def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

def get_time():
    return datetime.datetime.utcnow()

### Define your table below
#
db.define_table('question', Field('title'), Field('description'), Field('creation_time'), Field('question_owner', default=get_user_email),
        Field('question_id'), Field('status'), Field('dupe_num'))
db.commit()

db.define_table('ans_items', Field('content'), Field('ranking'), Field('question_id'), Field('item_id'),
        Field('dupe_num'), Field('item_owner'))
db.commit()

db.define_table('feedback', Field('question_id'), Field('item_id'), Field('feedback'), Field('feedback_owner'))
db.commit()

