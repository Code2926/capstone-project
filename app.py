from flask import Flask, render_template

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
    app.run(debug=True)
