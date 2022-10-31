from flask import Flask, request

app = Flask(__name__)
app.secret_key = "ciaone"

#selecting a route for our app

@app.route('/dataexchange',methods = ['POST'])
def dataexchange():
   if request.method == 'POST':
       return "Collegamento al server effettuato!"

@app.route('/prova')
def prova():
       return "Collegamento al server effettuato!"

if __name__ == '__main__':
    app.run(debug=True)