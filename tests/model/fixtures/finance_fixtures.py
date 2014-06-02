# coding=utf-8
from datetime import datetime
from fixture import DataSet

__author__ = 'shreyder'


class FinanceAccountData(DataSet):
    class Dummy:
        name = u"Dummy"
        type = "ASSET"


class DormitoryData(DataSet):
    class Dummy:
        number = "01"
        short_name = "abc"
        street = "dummy"


class RoomData(DataSet):
    class Dummy:
        number = 1
        level = 1
        inhabitable = True
        dormitory = DormitoryData.Dummy


class UserData(DataSet):
    class Dummy:
        login = "dummy"
        name = u"Dummy"
        registration_date = datetime.now()
        room = RoomData.Dummy