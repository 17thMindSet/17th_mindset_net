# inconito17 nov. 2021

from flask import Flask, render_template, url_for,redirect,request,flash
import jyserver.Flask as jsf



app = Flask(__name__)


# @jsf.use(app)
#
# class App:
#     def __init__(self):
#         pass
#
#     def checkComment(self):
#
#         errorP=self.js.document.getElementById('errorP')
#         errorP.innerHTML = 'Please Fill all The  Fields!!'
#


# Go to the Home page
@app.route("/")
@app.route('/home')
def home():
    return render_template(
        'index.html', title='Home', desContent='Welcome to sofapad!!!!')


# HAndler the 404 error--------------
@app.errorhandler(404)
def pageNotFound(e):
    return render_template('error.html'), 404


@app.route('/sendMailSucces/<stats>', methods=['post','get'])
def sendMail(stats):
    stats = 'klk'
    if request.method=='POST':
        try:
            msg=''
            if request.form["email"]=='' or request.form['comment'] == '':
                msg=("Please Fill all The  Fields!!'")
                color='color:#ff0000'
                stats='error'




            else:
                msg = ("Comment sent succesfully!")
                color = 'color:#0000ff'
                stats='succes'


            return  render_template('index.html', msg=msg, color=color)

        except:
            return render_template('index.html')

    else:
        return redirect(url_for('home'))






# RUN THE SERVER__________________________________
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
