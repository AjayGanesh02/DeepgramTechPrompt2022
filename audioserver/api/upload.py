import flask
import audioserver

@audioserver.app.route('/')
def show_index():
    """Display / route."""
    return flask.jsonify({
        'message': "success"
    })