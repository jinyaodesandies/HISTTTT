from flask import Flask, render_template, request
from API import timeline
import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/timeline', methods=['POST'])
def show_timeline():
    event = request.form['event']
    events = eval(timeline(event))  # Convert the string representation of the list back to a list
    return render_template('index.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)
