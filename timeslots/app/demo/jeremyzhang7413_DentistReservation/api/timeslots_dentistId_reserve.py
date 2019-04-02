# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource,timeslots_list
from .. import schemas


class TimeslotsDentistidReserve(Resource):

    def get(self, dentistId):
        result = []
        flag = 1
        for item in timeslots_list:
            if item['dentistId'] == dentistId:
                flag = 0
                if item['reserved'] == False:
                    result.append(item)
        if flag == 1:
            return 'wrong dentist ID input', 400
        return result, 200, None

    def post(self, dentistId):
        data = request.get_json(force=True)
        for item in timeslots_list:
            if item['dentistId'] == dentistId:
                if item['timeId'] == data['timeId']:
                    if item['reserved'] == False:
                        item['reserved'] = True
                        return item, 200
                    else:
                        return 'time already booked', 400
        return 'wrong input', 400
