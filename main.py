# inconito17 nov. 2021

from flask import Flask, render_template, url_for,redirect
import jyserver.Flask as jsf



app = Flask(__name__)

@jsf.use(app)

class App:
    def __init__(self):
        pass

    def checkComment(self):

        email = self.js.document.getElementById('email').value
        comment = self.js.document.getElementById('comment').value

        if email == '' or comment == '':
            errorP=self.js.document.getElementById('errorP')
            errorP.innerHTML = 'Please Fill all The  Fields!!'
        else:
            @app.route('/succes')
            def succes():
                print('salut')
                return redirect(url_for('home'))













# Go to the Home page
@app.route("/")
@app.route('/home')
def home():
    return App.render(render_template(
        'index.html', title='Home', desContent='Welcome to sofapad!!!!'))


# HAndler the 404 error--------------
@app.errorhandler(404)
def pageNotFound(e):
    return render_template('error.html'), 404


@app.route('/sendMailSucces', methods=['post'])
def succesMail():
    return 'mail sent'



# RUN THE SERVER__________________________________
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
