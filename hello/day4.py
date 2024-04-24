from flask import *
from flask_mail import *
app=Flask(__name__)
app.secret_key="a"

@app.route('/',methods=['GET','POST'])
def index():
    er=None
    if request.method=="GET":
        return render_template('mydp.html')
    else:
        er="hhhhh"
        f=request.files['dp']
        f.save(f.filename)
        a=1
        if a==1:
            flash('successfully saved')
        else:
            flash('error')
        return render_template('mydp.html',error=er)



app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='achuaks2000@gmail.com'
app.config['MAIL_PASSWORD']='htbu splg sumk dbuh'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)

@app.route('/sm')
def smail():
    msg=Message('subject',sender='achuaks2000@gmail.com',recipients=['akshayamohan911@gmail.com'])
    msg.body='hi my first message in flask'
    mail.send(msg)
    return 'success'




if __name__=="__main__":
    app.run(debug=True)