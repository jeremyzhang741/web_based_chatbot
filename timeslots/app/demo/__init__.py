# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import jeremyzhang7413_DentistReservation


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        jeremyzhang7413_DentistReservation.bp,
        url_prefix='/jeremyzhang7413/DentistReservation')
    return app

if __name__ == '__main__':
    create_app().run("0.0.0.0",debug=True)