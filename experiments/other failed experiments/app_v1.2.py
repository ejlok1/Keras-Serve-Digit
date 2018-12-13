# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 16:55:46 2018

@author: User

http://flask.pocoo.org/docs/0.12/patterns/fileuploads/

"""

import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask, render_template,request, flash


 
UPLOAD_FOLDER = '/upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def index():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("index ori.html")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))



if __name__ == "__main__":
	#decide what port to run the app in
	port = int(os.environ.get('PORT', 5000))
	#run the app locally on the givn port
	app.run(host='localhost', port=port)  #app.run(host='0.0.0.0', port=port) #app.run(host='localhost', port=port)  
	#optional if we want to run in debugging mode
	#app.run(debug=True)
    
    
    
    
#    return '''
#    <!doctype html>
#    <title>Upload new File</title>
#    <h1>Upload new File</h1>
#    <form method=post enctype=multipart/form-data>
#      <p><input type=file name=file>
#         <input type=submit value=Upload>
#    </form>
#    '''
#
#@app.route('/predict/',methods=['GET','POST'])
#def predict():
#	#whenever the predict method is called, we're going
#	#to input the user drawn character as an image into the model
#	#perform inference, and return the classification
#	#get the raw data format of the image
#	imgData = request.get_data()
#	#encode it into a suitable format
#	convertImage(imgData)
#	#print "debug"
#	#read the image into memory
#	x = imread('output.png',mode='L')
#	#compute a bit-wise inversion so black becomes white and vice versa
#	x = np.invert(x)
#	#make it the right size
#	x = imresize(x,(28,28))
#	#imshow(x)
#	#convert to a 4D tensor to feed into our model
#	x = x.reshape(1,28,28,1)
#	#print "debug2"
#	#in our computation graph
#	with graph.as_default():
#		#perform the prediction
#		out = model.predict(x)
#		print(out)
#		print(np.argmax(out,axis=1))
#		#print "debug3"
#		#convert the response to a string
#		response = np.array_str(np.argmax(out,axis=1))
#		return response	
#    
    