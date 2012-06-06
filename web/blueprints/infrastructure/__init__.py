# -*- coding: utf-8 -*-
"""
    web.blueprints.infrastructure
    ~~~~~~~~~~~~~~

    This module defines view functions for /infrastructure

    :copyright: (c) 2012 by AG DSN.
"""

from flask import Blueprint, flash, redirect, render_template, url_for
from pycroft.helpers import host_helper
from pycroft.model.hosts import Switch
from pycroft.model.ports import SwitchPort
from pycroft.model.session import session
from web.blueprints.navigation import BlueprintNavigation
from web.blueprints.infrastructure.forms import SwitchPortForm

bp = Blueprint('infrastructure', __name__, )
nav = BlueprintNavigation(bp, "Infrastruktur")


@bp.route('/subnets')
@nav.navigate(u"Subnetze")
def subnets():
    return render_template('infrastructure/base.html')


@bp.route('/switches')
@nav.navigate(u"Switche")
def switches():
    switches_list = Switch.q.all()
    return render_template('infrastructure/switches_list.html',
            switches=switches_list)


@bp.route('/switch/show/<switch_id>')
def switch_show(switch_id):
    switch = Switch.q.get(switch_id)
    switch_port_list = switch.ports
    switch_port_list = host_helper.sort_ports(switch_port_list)
    return render_template('infrastructure/switch_show.html',
        page_title=u"Switch: " + switch.name, 
        switch=switch, switch_ports=switch_port_list)


@bp.route('/switch/<switch_id>/switch_port/create', methods=['GET', 'POST'])
def switch_port_create(switch_id):
    form = SwitchPortForm()
    switch = Switch.q.get(switch_id)
    if form.validate_on_submit():
        new_switch_port = SwitchPort(name=form.name.data,
                switch_id = switch_id)
        session.add(new_switch_port)
        session.commit()
        flash('Neuer Switch Port angelegt', 'success')
        return redirect(url_for('.switch_show', switch_id = switch_id))
    return render_template('infrastructure/switch_port_create.html', 
            form=form, switch_id = switch_id,
            page_title = u"Neuer Switch Port für " + switch.name)


@bp.route('/vlans')
@nav.navigate(u"Vlans")
def vlans():
    return render_template('infrastructure/base.html')
