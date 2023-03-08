# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
import logging
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


 
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
 

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    print("this is printed")
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
    return 'Hello World test6'

@app.route('/hello/<name>')
def hello_name(name):
   logging.info('This is an name value %s', name)
   return 'Hello %s!' % name



# main driver function
if __name__ == '__main__':
	app.run(host =  '0.0.0.0', port=5001, debug=True)
	# run() method of Flask class runs the application
	# on the local development server.
	# app.run()
