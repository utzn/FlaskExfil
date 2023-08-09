from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploaded_files'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/download', methods=['GET'])
def download_file():
    # Send lorem ipsum txt file
    print(request.headers)
    print(request.get_data())
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

@app.route('/upload', methods=['POST'])
def upload_file():

    print(request.headers)
    print(request.get_data())

    # Read data from the POST body
    file_content = request.data

    if not file_content:
        return 'No data provided'

    # Define a filename. You can customize this part based on your requirements.
    # For instance, you can send the desired filename as a header or a URL parameter.
    # For simplicity, I'm using a default name here.
    filename = os.path.join(UPLOAD_FOLDER, 'uploaded_file.txt')

    # Save the content to the file
    with open(filename, 'wb') as file:
        file.write(file_content)

    return 'File uploaded successfully'


if __name__ == '__main__':
    # To run this, you'll need a SSL certificate
    # Generate a self-signed certificate using OpenSSL or get one from Let's Encrypt
    context = ('path_to_cert.pem', 'path_to_key.pem')
    app.run(host='0.0.0.0', port=80, ssl_context=None, threaded=True, debug=True)
