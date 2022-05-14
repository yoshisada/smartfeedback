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


db.define_table('user',
                Field('email_address'),
                Field('first_name'),
                Field('last_name')
                )

db.define_table('question',
                Field('owner_id'),
                Field('title'),
                Field('description'),
                Field('submission_time')
                )

db.define_table('item',
                Field('submitter_id'),
                Field('submission_time'),
                Field('description')
                )

db.define_table('feedback',
                Field('feedback_provider'),
                Field('submission_time'),
                Field('question_id'),
                Field('item_id'),
                Field('item_feedback_rank'),
                Field('item_feedback_score'),
                Field('independence_flag)')
                )

db.define_table('question_active_items',
                Field('question_id'),
                Field('item_id'),
                Field('active_flag')
                )

db.define_table('duplicacy_info',
                Field('item_id1'),
                Field('item_id2'),
                Field('number_of_coappearences'),
                Field('number_of_duplicacy_reports'),
                Field('number_of_times_id1_is_preferred'),
                Field('number_of_times_id2_is preferred)')
                )

db.define_table('question_recommendations',
                Field('user_email'),
                Field('question_id'),
                Field('question_rank')
                )
