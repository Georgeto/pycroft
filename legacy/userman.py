# Copyright (c) 2015 The Pycroft Authors. See the AUTHORS file.
# This file is part of the Pycroft project and licensed under the terms of
# the Apache License, Version 2.0. See the LICENSE file for details.
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, scoped_session, with_polymorphic

from conn import conn_opts
import userman_model as model

name = "userman"

engine = create_engine('postgresql://{userman-user}@127.0.0.1:{userman-port}'
                       '/userman'.format(**conn_opts), client_encoding='latin1')
session = scoped_session(sessionmaker(bind=engine))

relevant_tables = [model.FinanzKonten,
                   model.FinanzBuchungen,
                   #model.FinanzKonten,
                   model.FinanzKontoTyp,
                   with_polymorphic(model.BankKonto, [model.BkBuchung])
                   ]

'''
 Relevant tables:
 public | bank_konto              | table    | postgres
 public | bk_buchung              | table    | postgres
 public | finanz_buchungen        | table    | postgres
 public | finanz_konten           | table    | postgres
 public | finanz_konto_typ        | table    | postgres
'''

