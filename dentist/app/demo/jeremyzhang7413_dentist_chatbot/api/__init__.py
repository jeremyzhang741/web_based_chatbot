# -*- coding: utf-8 -*-
from __future__ import absolute_import

import flask_restful as restful

from ..validators import request_validate, response_filter

dentist_list = [{"name": "Jim",
    "id": 123122,
    "age": 45,
    "specialization": "Paediatric Dentistry",
    "education": "PHD"},
    {"name": "Alan",
    "id": 123152,
    "age": 46,
    "specialization": "Orthodontics",
    "education": "PHD"},
    {"name": "Jane",
    "id": 132112,
    "age": 42,
    "specialization": "Oral Surgery",
    "education": "PHD"}]

class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]