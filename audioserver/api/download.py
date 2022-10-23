import flask
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
        "WHERE origname == ?",
        (origname, )
    )
    files = cur.fetchall()
    if len(files) < 1:
        return flask.jsonify({
            'message': "File not found"
        }), 404
    elif len(files) > 1:
        return flask.jsonify({
            'message': "multiple files found"
        })

    return flask.send_from_directory(audioserver.app.config["UPLOAD_FOLDER"], files[0]['filename'], as_attachment=True, download_name=origname)
