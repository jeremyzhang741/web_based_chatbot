# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.dentist_available_list import DentistAvailableList
from .api.dentist_Id_information import DentistIdInformation


routes = [
    dict(resource=DentistAvailableList, urls=['/dentist/available_list'], endpoint='dentist_available_list'),
    dict(resource=DentistIdInformation, urls=['/dentist/<int:Id>/information'], endpoint='dentist_Id_information'),
]