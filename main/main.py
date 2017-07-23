from flask import Flask, flash, redirect, render_template, request, send_from_directory
import os
full_path = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_url_path='')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route("/")
def index():
    return render_template(
        'index.html', **locals())

if __name__ == "__main__":
    app.run(host='localhost', port=3000)