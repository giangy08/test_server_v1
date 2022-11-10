from flask import Flask, request, werkzeug

app = Flask(__name__)
app.secret_key = "my_secrek_key_1"

#selecting a route for our app

@app.route('/connection_test')
def prova():
       return "Collegamento al server effettuato!"

if __name__ == '__main__':
    app.run(debug=True)
