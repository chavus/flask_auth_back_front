import os
import socket
from flask import Blueprint, render_template, redirect, url_for, session, Response
from auth_api.core_front.forms import ItemForm
from auth_api import auth_api_url
from flask_login import login_required,current_user
import requests
from auth_api.resources.item import ItemList

core_blueprint = Blueprint('core', __name__)  # , template_folder=(os.path.join(project_dir, '/templates')))


@core_blueprint.route('/home', methods=['GET', 'POST'])
def home():
    print('api url :', auth_api_url)
    print('in home')
    form = ItemForm()
    if form.validate_on_submit():
        item = form.item.data
        print(item)
        return redirect(url_for('core.item', item=item))
    return render_template('home.html', form=form)


@core_blueprint.route('/item/<string:item>')
@login_required
def item(item):
    r = requests.get(auth_api_url + '/api/item/' + item, headers={'api_key': session['user_api_key']})
    return Response(r)


@core_blueprint.route('/items_list')
# @login_required
def items_list():
    print('in items_list with api url: ', auth_api_url)
    r = requests.get(auth_api_url + '/api/items', headers={'api_key': 'UnB7LglbdzOOF8xa'}) #session['user_api_key']
    # r = ItemList().get()
    print(r)
    return Response(r)
