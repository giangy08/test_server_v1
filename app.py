from flask import Flask, request, werkzeug

app = Flask(__name__)
app.secret_key = "my_secret_key_1"

#selecting a route for our app
@app.route('/dataexchange',methods = ['POST'])
def dataexchange():
   if request.method == 'POST':
       imagefile = Flask.request.files['image']
       filename = werkzeug.utils.secure_filename(imagefile.filename)
       print("\nReceived image File name : " + imagefile.filename)
       imagefile.save(filename)
       return "Image Uploaded Successfully"
       #se questo codice va bene, poi bisogna inglobare quello di Matteo e fare il return della nuova immagine direttamente

@app.route('/connection_test')
def prova():
       return "Collegamento al server effettuato!"

if __name__ == '__main__':
    app.run(debug=True)
