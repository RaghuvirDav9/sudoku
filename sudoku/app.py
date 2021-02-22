from flask import Flask, render_template, request,send_file
from werkzeug.utils import secure_filename
import os
import requests
import main
import cv2

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './Resources/'

@app.route('/')
def upload_f():
   return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
      # print(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
      # img=cv2.imread(str(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))))
      # cv2.imshow('demo',img)
      # cv2.waitKey(0)
      img=main.demo(str(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))))

      print(img)
      name=str(os.path.join(app.config['UPLOAD_FOLDER'],'done', secure_filename(f.filename)))
      print(name)
      cv2.imwrite(name,img)
      # cv2.imshow('new2', img)
      # cv2.waitKey(0)
      # resp=request.post()
      # response = requests.post(url='/', data=img.all())
      return send_file(name,mimetype='image/gif')
      # return 'file uploaded successfully'
      # return img

@app.route('/new1', methods = ['GET', 'POST'])
def new1():
   return render_template('new1.html')

# if __name__ == '__main__':
app.run(debug = True)