# Deploy a Keras Model to the web


## Overview

The original project is based on Siraj's repo and based on [this](https://youtu.be/f6Bf3gl4hWY) video on Youtube. Basically I'm building a model that recognizes handwritten digit images (MNIST).  Using the simple [Keras](http://keras.io/) Library, we wrap it into a Webapp using the [Flask](http://flask.pocoo.org/) Micro Framework. And in GCP i'm using ComputeEngine which is easy to deploy even without using a container (Docker)

After testing in locally, we go to Google Cloud, activate the ComputeEngine App and host / serve up our solution! The website is [here](https://digit-recogniser-123.appspot.com/#)


## Dependencies

```
mkdir Digit-Recogniser 
conda create --name Digit-Recogniser python=3.5 pip numpy
activate Digit-Recogniser
pip install -r requirements.txt
```

## Usage

Once dependencies are installed, test to make sure it works on your localhost before going to Google Cloud. In command line:

```
cd Digit-Recogniser
activate Digit-Recogniser
python app.py
```

It's serving a saved Keras model to you via Flask. On the web browser the address is 
```http://localhost:5000)``` 
thou you need to change it on the app.py file. 

## Credits

The credits for this code go to [moinudeen](https://github.com/moinudeen) who is the original author of this project. 

## Further improvements 
- Documentation of the Google Cloud hosting process 
- Enable app to work on tablets and smartphones 
- Get it to work on Dockers (and gRPC) 
- Get it to work on Kubeflow 
- Check again to see if GCP actually charges me for hosting this.... time will tell I suppose 
- Deploy the real project, but that probably will be another seperate repository