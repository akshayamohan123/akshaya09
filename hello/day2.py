from flask import *

app=Flask(__name__)

@app.route('/admin')
def admin1():
    return 'welcome admin'

@app.route('/student')
def student1():
    return 'welcome student'

@app.route('/teacher')
def teacher1():
    return 'welcome teacher'

@app.route('/user/<uname>')
def user(uname):
    if uname=='admin':
        return redirect(url_for('admin1'))
    elif uname=='student':
        return redirect(url_for('student1'))
    elif uname=='teacher':
        return redirect(url_for('teacher1'))
    else:
        return 'invalid user'


# @app.route('/<job>')
# def mypage(job):
#     # return 'my html page'
#     name=input('enter your name')
#     return render_template('d1.html',uname=name,j=job)


@app.route('/mul')
def mult():
    num=int(input('enter num:'))
    return render_template('mul.html',unum=num)



if __name__=="__main__":
    app.run(debug=True)
