import os
from flask import Flask, request, send_file

UPLOAD_FOLDER = './upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/get_image/<picture_id>')
def get_image(picture_id):
    return send_file("C:\\Users\\Pygmalion\\Desktop\\testando\\upload\\"+str(picture_id)+".jpg", mimetype='image/gif')

@app.route('/send_image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        return path

        return 'ok'
    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''

app.run()