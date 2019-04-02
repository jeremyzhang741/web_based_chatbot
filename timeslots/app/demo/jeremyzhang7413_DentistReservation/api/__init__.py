# -*- coding: utf-8 -*-
from __future__ import absolute_import

import flask_restful as restful

from ..validators import request_validate, response_filter

timeslots_list = [{"dentistId": 123122,
    "timeId": 10032,
    "data": "2019-03-26",
    "timeslot": "9:00-10:00",
    "reserved": False},
    {"dentistId": 123122,
     "timeId": 10033,
     "data": "2019-03-26",
     "timeslot": "10:00-11:00",
     "reserved": True},
    {"dentistId": 123122,
     "timeId": 10034,
     "data": "2019-03-26",
     "timeslot": "11:00-12:00",
     "reserved": False},
    {"dentistId": 123152,
     "timeId": 10035,
     "data": "2019-03-26",
     "timeslot": "14:00-15:00",
     "reserved": True},
    {"dentistId": 123152,
     "timeId": 10036,
     "data": "2019-03-26",
     "timeslot": "15:00-16:00",
     "reserved": True},
    {"dentistId": 123152,
     "timeId": 10037,
     "data": "2019-03-26",
     "timeslot": "16:00-17:00",
     "reserved": True},
    {"dentistId": 123122,
     "timeId": 10041,
     "data": "2019-03-27",
     "timeslot": "9:00-10:00",
     "reserved": False},
    {"dentistId": 123122,
     "timeId": 10042,
     "data": "2019-03-27",
     "timeslot": "10:00-11:00",
     "reserved": True},
    {"dentistId": 123122,
     "timeId": 10043,
     "data": "2019-03-27",
     "timeslot": "11:00-12:00",
     "reserved": False},
    {"dentistId": 132112,
     "timeId": 10044,
     "data": "2019-03-27",
     "timeslot": "14:00-15:00",
     "reserved": False},
    {"dentistId": 132112,
     "timeId": 10045,
     "data": "2019-03-27",
     "timeslot": "15:00-16:00",
     "reserved": False},
    {"dentistId": 132112,
     "timeId": 10046,
     "data": "2019-03-27",
     "timeslot": "16:00-17:00",
     "reserved": False},
    {"dentistId": 123152,
     "timeId": 10051,
     "data": "2019-03-28",
     "timeslot": "9:00-10:00",
     "reserved": True},
    {"dentistId": 123152,
     "timeId": 10052,
     "data": "2019-03-28",
     "timeslot": "10:00-11:00",
     "reserved": True},
    {"dentistId": 123152,
     "timeId": 10053,
     "data": "2019-03-28",
     "timeslot": "11:00-12:00",
     "reserved": True},
    {"dentistId": 132112,
     "timeId": 10054,
     "data": "2019-03-28",
     "timeslot": "14:00-15:00",
     "reserved": False},
    {"dentistId": 132112,
     "timeId": 10055,
     "data": "2019-03-28",
     "timeslot": "15:00-16:00",
     "reserved": False},
    {"dentistId": 132112,
     "timeId": 10056,
     "data": "2019-03-28",
     "timeslot": "16:00-17:00",
     "reserved": True}
                  ]

class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]