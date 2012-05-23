# -*- coding: utf-8 -*-
"""
    web.blueprints.dormitories
    ~~~~~~~~~~~~~~

    This module defines view functions for /dormitories
    :copyright: (c) 2012 by AG DSN.
"""

from flask import Blueprint, render_template, redirect, url_for, flash
from pycroft.helpers import dormitory_helper
from pycroft.model.session import session
from pycroft.model.dormitory import Room, Dormitory
from web.blueprints import BlueprintNavigation
from web.blueprints.dormitories.forms import RoomForm, DormitoryForm

bp = Blueprint('dormitories', __name__, )
nav = BlueprintNavigation(bp, "Wohnheime")


@bp.route('/')
@nav.navigate(u"Wohnheime")
def dormitories():
    dormitories_list = Dormitory.q.all()
    dormitories_list = dormitory_helper.sort_dormitories(dormitories_list)
    return render_template('dormitories/dormitories_list.html',
        dormitories=dormitories_list)


@bp.route('/show/<dormitory_id>')
def dormitory_show(dormitory_id):
    dormitory = Dormitory.q.get(dormitory_id)
    rooms_list = dormitory.rooms
    return render_template('dormitories/dormitory_show.html',
        page_title=u"Wohnheim " + dormitory.short_name, rooms=rooms_list)


@bp.route('/create', methods=['GET', 'POST'])
@nav.navigate(u"Neues Wohnheim")
def dormitory_create():
    form = DormitoryForm()
    if form.validate_on_submit():
        myDormitory = Dormitory(short_name=form.short_name.data,
            street=form.street.data, number=form.number.data)
        session.add(myDormitory)
        session.commit()
        flash('Wohnheim angelegt', 'success')
        return redirect(url_for('.dormitories'))
    return render_template('dormitories/dormitory_create.html', form=form)


@bp.route('/room/delete/<room_id>')
def room_delete(room_id):
    Room.q.filter(Room.id == room_id).delete(
        synchronize_session='fetch')
    session.commit()
    flash('Raum gelöscht', 'success')
    return redirect(url_for('.dormitories'))


@bp.route('/room/show/<room_id>')
def room_show(room_id):
    room = Room.q.get(room_id)
    return render_template('dormitories/room_show.html',
        page_title=u"Raum " + str(room.dormitory.short_name) + u" " + \
                   str(room.level) + u"-" + str(room.number), room=room)


@bp.route('/room/create', methods=['GET', 'POST'])
@nav.navigate(u"Neuer Raum")
def room_create():
    form = RoomForm()
    if form.validate_on_submit():
        myRoom = Room(
            number=form.number.data,
            level=form.level.data,
            inhabitable=form.inhabitable.data,
            dormitory_id=form.dormitory_id.data.id)
        session.add(myRoom)
        session.commit()
        flash('Raum angelegt', 'success')
        return redirect(url_for('.room_show', room_id=myRoom.id))
    return render_template('dormitories/dormitory_create.html', form=form)
