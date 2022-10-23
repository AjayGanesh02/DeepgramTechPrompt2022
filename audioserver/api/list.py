import flask
import audioserver


@audioserver.app.route('/list', methods=['GET'])
def show_list():
    """Show user list of files."""
    minduration = flask.request.args.get('minduration', default=0, type=int)
    maxduration = flask.request.args.get('maxduration')

    connection = audioserver.model.get_db()
    cur = None
    if maxduration is not None:
        cur = connection.execute(
            "SELECT origname "
            "FROM files "
            "WHERE duration > ? "
            "AND duration < ?",
            (minduration, maxduration, )
        )
    else:
        cur = connection.execute(
            "SELECT origname "
            "FROM files "
            "WHERE duration > ?",
            (minduration, )
        )
    results = cur.fetchall()
    if results is None or len(results) == 0:
        return flask.jsonify({
            'message': "No files fit the criteria"
        })
    
    processed = {'files': []}
    for result in results:
        processed['files'].append(result['origname'])
    
    return flask.jsonify(processed)