from flask import Flask, render_template, url_for

app = Flask(__name__)

#region [Region] variables
success_response = 'success'
fail_response = 'error'
#endregion

#region [Region] View loader endpoints

@app.route('/')
def indexView():
    url_for('static', filename='js/round-slider.js')
    url_for('static', filename='js/index.js')
    return render_template('index.html')

@app.route('/stream')
def streamView():
    return render_template('stream.html')

@app.route('/gallery')
def galleryView():
    return render_template('gallery.html')

#endregion

#region [Region] Controllers

@app.route("/<percent>")
def setLightSensitivity(percent):
    #TODO: Call LED IoT function
    return success_response

#endregion
