from flask import Flask, render_template, redirect, url_for
import sys
print(sys.version)      # Full version information string
print(sys.version_info) # Structured tuple (major, minor, micro)

app = Flask(__name__)

# Global variables shared by all users
left_counter = 0
right_counter = 0

@app.route('/')
def index():
    # Variables 'left' and 'right' here must match the {{ }} in your HTML
    return render_template('index.html', left=left_counter, right=right_counter)

@app.route('/left_click')
def left_click():
    global left_counter
    left_counter += 1
    return render_template('trol.html')

@app.route('/right_click')
def right_click():
    global right_counter
    right_counter += 1
    return render_template('trol.html')

if __name__ == '__main__':
    app.run(debug=True)
