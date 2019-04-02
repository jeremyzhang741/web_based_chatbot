# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource, dentist_list
from .. import schemas


class DentistIdInformation(Resource):

    def get(self, Id):
        for item in dentist_list:
            if item['id'] == Id:
                return item, 200, None
        return "wrong id", 404

