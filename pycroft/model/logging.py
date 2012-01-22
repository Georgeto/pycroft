# -*- coding: utf-8 -*-
# Copyright (c) 2011 The Pycroft Authors. See the AUTHORS file.
# This file is part of the Pycroft project and licensed under the terms of
# the Apache License, Version 2.0. See the LICENSE file for details.
"""
    pycroft.model.logging
    ~~~~~~~~~~~~~~

    This module contains the classes LogEntry, UserLogEntry, TrafficVolume.

    :copyright: (c) 2011 by AG DSN.
"""
from base import ModelBase
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Boolean, BigInteger, Integer, DateTime
from sqlalchemy.types import Text


class LogEntry(ModelBase):
    # variably sized string
    message = Column(Text, nullable=False)
    # created
    timestamp = Column(DateTime, nullable=False)

    # many to one from LogEntry to User
    author = relationship("User",
                backref=backref("log_entries"))
    author_id = Column(Integer, ForeignKey("user.id"), nullable=False)


class UserLogEntry(ModelBase):
    # many to one from UserLogEntry to User
    user = relationship("User",
                backref=backref("user_log_entries"))
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)