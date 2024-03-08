from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    '''This is the main function that runs the application.'''
    port = int(os.environ.get('PORT', 5000)) #port number
    app.run(debug=True, host='0.0.0.0', port=port) #run the application