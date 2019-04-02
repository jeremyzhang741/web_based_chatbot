# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource, timeslots_list
from .. import schemas


class Timeslots(Resource):

    def get(self):
        result = []
        for item in timeslots_list:
            if item['reserved'] == False:
                result.append(item)

        return result, 200, None

    def post(self):
        data = request.get_json(force=True)
        for item in timeslots_list:
            if item['dentistId'] == data['dentistId']:
                if item['timeId'] == data['timeId']:
                    if item['reserved'] == False:
                        item['reserved'] = True
                        return item, 200
                    else:
                        return 'time already booked', 400
        return 'wrong input', 400




    def put(self):
        data = request.get_json(force=True)
        for item in timeslots_list:
            if item['timeId'] == data['timeId']:
                if item['reserved'] == True:
                    item['reserved'] = False
                    return 'successful cancel', 200, None
                else:
                    return 'this timeslot not been reserved', 400
        return 'wrong input', 400