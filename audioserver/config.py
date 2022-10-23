"""AudioServer development configuration."""
import pathlib
# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'
# File Upload to var/uploads/
AS_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = AS_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['wav', 'mp3', 'm4a', 'flac', 'mp4'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
DATABASE_FILENAME = AS_ROOT/'var'/'audioserver.sqlite3'
