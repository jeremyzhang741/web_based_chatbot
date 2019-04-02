# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import jeremyzhang7413_chatbot


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        jeremyzhang7413_chatbot.bp,
        url_prefix='/jeremyzhang7413/chatbot')
    return app

if __name__ == '__main__':
    create_app().run("0.0.0.0",port=5002,debug=True)