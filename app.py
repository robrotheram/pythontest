from flask import Flask
from flask import render_template
import os
from random import choice


app = Flask(__name__)


@app.route('/')
def index():
    salutation = choice(salutations)
    return render_template('index.html', salutation=salutation)

salutations = [
    'Hey there, hi there, ho there.',
    'I am a banana.',
    'Go Patriots!',
    'Brian is nerf herder.']


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
