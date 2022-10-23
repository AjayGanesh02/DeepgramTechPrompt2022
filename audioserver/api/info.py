import flask
import audioserver

@audioserver.app.route('/info', methods=['GET'])
def show_info():
    """Handle showing audio metadata."""
    origname = flask.request.args.get('name')

    connection = audioserver.model.get_db()
    cur = None
    if origname is None:
        cur = connection.execute(
            "SELECT origname, duration, filetype, uploaded "
            "FROM files",
            ()
        )
    else:
        cur = connection.execute(
            "SELECT origname, duration, filetype, uploaded "
            "FROM files "
            "WHERE origname == ?",
            (origname, )
        )
    results = cur.fetchall()
    if results is None or len(results) == 0:
        return flask.jsonify({
            'message': "No files fit the criteria."
        })
    output = {'results': results}

    return flask.jsonify(output)
    