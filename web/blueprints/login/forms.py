# Copyright (c) 2012 The Pycroft Authors. See the AUTHORS file.
# This file is part of the Pycroft project and licensed under the terms of
# the Apache License, Version 2.0. See the LICENSE file for details.
from flaskext.wtf.form import Form
from wtforms.fields import TextField, PasswordField

class LoginForm(Form):
    login = TextField()
    password = PasswordField()
