"""Insta485 package initializer."""
import flask
# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)
app.config.from_object('audioserver.config')

import audioserver.model  # noqa: E402  pylint: disable=wrong-import-position
import audioserver.api  # noqa: E402  pylint: disable=wrong-import-position
