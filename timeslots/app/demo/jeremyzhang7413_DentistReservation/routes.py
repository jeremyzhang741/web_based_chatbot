# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.timeslots import Timeslots
from .api.timeslots_cancel_appointment import TimeslotsCancelAppointment
from .api.timeslots_dentistId_book_appointment import TimeslotsDentistidBookAppointment


routes = [
    dict(resource=Timeslots, urls=['/timeslots'], endpoint='timeslots'),
    dict(resource=TimeslotsCancelAppointment, urls=['/timeslots/cancel_appointment'], endpoint='timeslots_cancel_appointment'),
    dict(resource=TimeslotsDentistidBookAppointment, urls=['/timeslots/<int:dentistId>/book_appointment'], endpoint='timeslots_dentistId_book_appointment'),
]