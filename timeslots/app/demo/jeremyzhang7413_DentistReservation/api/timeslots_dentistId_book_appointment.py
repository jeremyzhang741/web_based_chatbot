# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class TimeslotsDentistidBookAppointment(Resource):

    def get(self, dentistId):

        return [], 200, None

    def post(self, dentistId):
        print(g.json)

        return {'reserved': False}, 200, None