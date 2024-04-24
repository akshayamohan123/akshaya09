from flask import *

app=Flask(__name__)
app.secret_key="aa"


@app.route('/GStudReg',methods=['GET'])
def mygetmthd():
    name=request.args.get('fname')
    email=request.args.get('em')
    phone=request.args.get('ph')
    print(name,email,phone)
    return 'success'



@app.route('/PStudReg',methods=['POST'])
def mypostmthd():
    name=request.form['fname']
    email=request.form['em']
    phone=request.form['ph']
    print(name,email,phone)
    return 'success post method'

@app.route('/')
def reg():
    return render_template('d4.html')

@app.route('/succ',methods=['POST','GET'])
def get_data():
    if request.method=='POST':
        data=request.form
        return data
    else:
        return render_template('day2.html')

@app.route('/sc')
def set_cook():
    res=make_response("<h1>Cookie is set</h1>")
    res.set_cookie('fname','ammu')
    return res


@app.route('/gc')
def get_cook():
    name=request.cookies.get('fname')
    return name

@app.route('/ss')
def set_ss():
    res=make_response('session is set')
    session['phone']=8374982
    return res

@app.route('/gs')
def get_ss():
    if "phone" in session:
        return str(session['phone'])



@app.route('/lgn',methods=['POST','GET'])
def my_loggin():
    if request.method=='POST':
        email=request.form['em']
        password=request.form['pass1']
        print(email,password)
        if password=='admin':
            session['emil']=email
            return render_template('q2.html')
          
        else:
                return 'invalid password'
    else:
        return render_template('q.html')
    
@app.route('/eg')
def emlget():
    if 'emil' in session:
        return render_template('viewpro.html',e=session['emil'])
    else:
        return("<script>window.alert('error!!!');window.location.href='/lgn'</script>")
    
@app.route('/out')
def logouts():
    del session['emil']
    return redirect(url_for('my_loggin'))
    


    



if __name__=="__main__":
    app.run(debug=True)