# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 18:15:34 2018

@author: User

https://www.youtube.com/watch?v=bxFaa_FNdL4
https://github.com/ibrahimokdadov/upload_file_python

https://www.tutorialspoint.com/flask/flask_file_uploading.htm

"""

from flask import Flask, render_template, request
from werkzeug import secure_filename
from flask import Flask, request, redirect, url_for
app = Flask(__name__)
import os 


@app.route('/upload')
def index():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template('upload.html')

#
#UPLOAD_FOLDER = '/uploader'
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


#def allowed_file(filename):
#    return '.' in filename and \
#           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		


if __name__ == "__main__":
	#decide what port to run the app in
	port = int(os.environ.get('PORT', 5000))
	#run the app locally on the givn port
	app.run(host='localhost', port=port)  #app.run(host='0.0.0.0', port=port) #app.run(host='localhost', port=port)  
	#optional if we want to run in debugging mode
	#app.run(debug=True)
