import flask
import uuid
import pathlib
import audioserver
from tinytag import TinyTag


def allowed_file(filename):
    """Check if file is allowed filetype."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in audioserver.app.config['ALLOWED_EXTENSIONS'] and \
           TinyTag.is_supported(filename)


@audioserver.app.route('/upload', methods=['POST'])
def handle_upload():
    """Handle audio file upload."""
    if 'file' not in flask.request.files:
        return flask.jsonify({
            'message': "file not found in request"
        }), 400
    fileobj = flask.request.files['file']

    if fileobj.filename == '':
        return flask.jsonify({
            'message': "file not found"
        }), 400
    filename = fileobj.filename

    if not allowed_file(filename):
        return flask.jsonify({
            'message': "Invalid file extension"
        }), 400

    # file naming procedure
    stem = uuid.uuid4().hex
    file_suffix = pathlib.Path(filename).suffix
    uuid_filename = f"{stem}{file_suffix}"

    path = audioserver.app.config["UPLOAD_FOLDER"]/uuid_filename
    fileobj.save(path)

    tag = TinyTag.get(path)

    connection = audioserver.model.get_db()

    connection.execute(
        "INSERT INTO files (filename, origname, duration, filetype) "
        "VALUES (?, ?, ?, ?)",
        (uuid_filename, filename, int(tag.duration),
         filename.rsplit('.', 1)[1].lower(), )
    )
    return flask.jsonify({
        'message': "success"
    }), 201
