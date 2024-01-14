from flask import Flask, request, send_file
import os
import time


app = Flask(__name__)

audio_path = '/home/dev/transmitter/output.txt'
last_request_time = 0


def check_audio_updated():
    return os.path.getmtime(audio_path)


@app.route('/recieve_text', methods=['GET'])
def receive_text():
    global last_request_time
   # data = request.json
    #received_text = data.get('text')
    
    # Replace this part with your Discord bot logic to process received_text
    # For demonstration, let's assume you have an MP3 file named 'audio.mp3'
    # You can replace this with the path to your generated MP3 file
    
    # Check if the MP3 file exists
    if os.path.exists(audio_path):
        last_modified_time = check_audio_updated()
        if last_modified_time > last_request_time:
            last_request_time = time.time()
            return send_file(audio_path, as_attachment=True)
        else:
            return "Audio file not updated", 304
    else:
        return 'Audio file not found on the server', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4050)  # Run the Flask app on localhost:5000

