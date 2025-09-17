from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/grid')
def grid_gallery():
    return render_template('gallery.html')

@app.route('/flex')
def flex_gallery():
    return render_template('flex.html')

if __name__ == '__main__':
    # Use Render’s assigned port or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
