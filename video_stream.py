from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)
# Assuming the video files are located in the same directory as this script
VIDEO_FOLDER = os.path.dirname(os.path.abspath(__file__))
# Specify your default video file name here
DEFAULT_VIDEO_FILE = 'Hacksaw.Ridge.2016.Hybrid.720p.BluRay.DD+5.1.x264-playHD.mkv'

@app.route('/stream', defaults={'filename': DEFAULT_VIDEO_FILE})
@app.route('/stream/<filename>')
def stream_file(filename):
    # Ensure the path is safe and the file exists
    file_path = os.path.join(VIDEO_FOLDER, filename)
    if not os.path.isfile(file_path):
        abort(404)  # File not found
    return send_from_directory(VIDEO_FOLDER, filename)

if __name__ == '__main__':
    # Make the server available on your LAN
    app.run(host='0.0.0.0', port=5000, debug=False)
