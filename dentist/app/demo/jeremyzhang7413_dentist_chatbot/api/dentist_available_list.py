# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
import requests

from . import Resource,dentist_list
from .. import schemas


class DentistAvailableList(Resource):

    def get(self):
        available_ll = []
        url = "http://127.0.0.1:5000/jeremyzhang7413/DentistReservation/timeslots"
        data_0 = requests.get(url)
        data = data_0.json()
        for e in dentist_list:
            avail_1 = []
            for item in data:
                if e['id'] == item['dentistId']:
                    avail_1.append([item['timeId'],item['data'],item['timeslot']])
                    continue
            available_ll.append({'name':e['name'],'id':e['id'],'available':avail_1})
        return available_ll, 200, None
