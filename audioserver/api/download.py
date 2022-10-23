import flask
import pathlib
import audioserver


@audioserver.app.route('/download', methods=['GET'])
def handle_download():
    """Handle audio file download."""
    if 'name' not in flask.request.args or flask.request.args.get('name') == "":
        return flask.jsonify({
            'message': "please specify a file to download"
        }), 400
    
    origname = flask.request.args.get('name')

    connection = audioserver.model.get_db()

    cur = connection.execute(
        "SELECT filename "
        "FROM files "
        "WHERE origname == ?,"
        (origname, )
    )
    file = cur.fetchall()
    print(file)