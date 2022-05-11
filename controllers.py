"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

# from os import uname
import uuid

from py4web import action, request, abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.url_signer import URLSigner

from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash

# from .models import get_user_email
from pydal.validators import *

url_signer = URLSigner(session)


@action("index")
@action.uses("index.html", auth, T)
def index():
    user = auth.get_user()
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    actions = {"allowed_actions": auth.param.allowed_actions}
    #form for login or answering a survey
    form_login = Form([Field("Username"), Field("Password")])
    code_login = Form([Field("login_by_code")])
    return dict(login = form_login, code = code_login)

@action("home")
@action.uses("home.html", auth, T)
def index():
    #form for login or answering a survey
    form_login = Form([Field("Username"), Field("Password")])
    code_login = Form([Field("login_by_code")])
    existing_prompts = ["p1", "p2", "p3"]
    new_prompts = ["p1", "p2", "p3"]

    #return table of existing prompts owned by user.  and table of public prompts.
    return dict(existing = existing_prompts, new = new_prompts)

# Add Prompt
@action('add', method=["GET", "POST"])
@action.uses(db, session, auth.user, 'add.html')
def add():
    # form = # ADD TO DB
    # if(form.accepted):
    #     redirect(URL('index'))

    # return dict(form=form)
    return

# Edit Prompt
@action('edit/<contact_id:int>', method=["GET", "POST"])
@action.uses(db, session, auth.user, url_signer.verify(), 'edit.html')
def edit(contact_id = None):
    # assert contact_id is not None
    # p = # TODO
    # if p is None:
    #     redirect(URL('index'))

    # form = # TODO
    # if(form.accepted):
    #     redirect(URL('index'))

    # return dict(form=form)
    return

# Delete Prompt
@action('delete/<contact_id:int>', method=["GET", "POST"])
@action.uses(db, session, auth.user, url_signer.verify())
def delete(contact_id=None):
    assert contact_id is not None
    db(db.contact.id == contact_id).delete()
    redirect(URL('index'))

# Vote Up / Down
@action('inc/<bird_id:int>') # the :int means: please convert this to an int.
@action.uses(db, session, auth.user, url_signer.verify())
# ... has to match the bird_id parameter of the Python function here.
def vote(bird_id=None):
    # TODO
    assert bird_id is not None
    bird = db.bird[bird_id]
    db(db.bird.id == bird_id).update(n_sightings=bird.n_sightings+1)
    redirect(URL('index'))