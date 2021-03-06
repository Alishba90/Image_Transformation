from fileinput import filename
from operator import truediv
from flask import Flask, flash, request, redirect, send_file, url_for, render_template

import os
from werkzeug.utils import secure_filename

app = Flask(__name__) 
 
app.secret_key = "secret key"
UPLOAD_FOLDER = 'static/uploadimg/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 
@app.route('/')


def home():
    return render_template('index.html') 


@app.route('/', methods=['POST'])

def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        filename="static/uploadimg/"+filename
        print("hi")
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    filename="uploadimg/"+filename
    
    return redirect(url_for('static', filename=filename), code=301)


@app.route('/download')
def download():
    print("the path is " ,os.getcwd())
    address=os.getcwd()+url_for('static', filename="uploadimg/n.jpg")
    print("the address is ",address)
    
    return send_file("C:/Users/3BROS COMPUTERZ/Downloads/email.jpg",as_attachment=True)
    

if __name__ == "__main__":
    app.debug='true'
    app.run(port=5000)