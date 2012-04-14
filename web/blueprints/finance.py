# -*- coding: utf-8 -*-
# Copyright (c) 2012 The Pycroft Authors. See the AUTHORS file.
# This file is part of the Pycroft project and licensed under the terms of
# the Apache License, Version 2.0. See the LICENSE file for details.
"""
    web.blueprints.finance
    ~~~~~~~~~~~~~~

    This module defines view functions for /finance

    :copyright: (c) 2012 by AG DSN.
"""

from flask import Blueprint, render_template
from web.blueprints import BlueprintNavigation

bp = Blueprint('finance', __name__, )
nav = BlueprintNavigation(bp, "Finanzen")


@bp.route('/')
@bp.route('/journals')
@nav.navigate(u"Journale")
def journals():
    return render_template('finance/base.html', page_title=u"Journals")


@bp.route('/accounts')
@nav.navigate(u"Konten")
def accounts():
    return render_template('finance/base.html', page_title=u"Konten")


@bp.route('/transactions')
@nav.navigate(u"Transaktionen")
def transactions():
    return render_template('finance/base.html', page_title=u"Transaktionen")