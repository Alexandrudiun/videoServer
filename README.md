# Video Streaming Flask Application

This Flask application serves video files from a specified directory over HTTP, making it possible to stream video files to clients. It's designed to be a simple example of how to use Flask to stream video content.

## Features

- Streams video files from the server directory.
- Allows streaming of a default video file or a specified video file through URL parameters.
- Simple setup and minimal dependencies.

## Requirements

- Flask

## Installation

To set up the server, you will need Python installed on your system. If you don't have Python installed, please install Python 3 from the official website. Then, follow these steps:

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Create a virtual environment: python3 -m venv venv
4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
5. Install Flask: pip install Flask
   
## Usage

To run the server, execute the following command from the root of your project directory: python app.py


This will start the Flask server, making it accessible from `http://0.0.0.0:5000/` on your local network.

### Streaming Videos

To stream the default video, navigate to: http://0.0.0.0:5000/stream


To stream a specific video file, replace `filename` in the URL with your video file's name (the video file must be in the server's directory): http://0.0.0.0:5000/stream/filename


## Configuration

- **VIDEO_FOLDER**: Directory where video files are stored. It's currently set to the same directory as the script.
- **DEFAULT_VIDEO_FILE**: The name of the default video file to stream if no filename is specified in the request. Modify this in the script to your desired default video.

## Security Note

This application is designed for demonstration purposes and does not include security features necessary for production use. Ensure to implement authentication, validation, and other necessary security measures before using this in a production environment.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.






