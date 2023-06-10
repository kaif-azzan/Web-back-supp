from flask import Flask,render_template,request,url_for,redirect,session
import mysql.connector

con=mysql.connector.connect(host='sql12.freesqldatabase.com',user='sql12624932',password='wflDn3qeE9',database='sql12624932')
if con.is_connected:
    print("db connected")

app=Flask(__name__,template_folder='template')

@app.route('/',methods=['GET','POST'])
def login():
    if request.method=="POST":
        first=[]
        second=[]
        uname=request.form['uname']
        upass=request.form['pas']   
        cursor=con.cursor()
        cursor.execute("SELECT `username`,`password` FROM `stupid`")
        rec=cursor.fetchall()
        cursor.close()
        for i in range(len(rec)):
            first.append(rec[i][0])
            second.append(rec[i][1])
        if uname in first:
            if upass in second:
                return redirect(url_for('confirm'))
            else:
                 return ("user not signed up password")
        else:
                return("User not signed up username")
    else:
            return render_template("index.html")
       

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/process',methods=['POST','GET'])
def process():
    uname=request.form['namez']
    pas=request.form['paz']
    if request.method=="POST":
        cursor=con.cursor()
        cred=[]
        cursor.execute("SELECT username FROM `stupid`")
        record=cursor.fetchall()
        maxx=len(record)
        for i in range(maxx):
            cred.append(record[i][0])
        if uname in cred:
            return("not possible to log you in sorry")
        else:
            cursor.execute("INSERT INTO `stupid`(`username`,`password`) VALUES (%s,%s)",(uname,pas))
            con.commit()
            cursor.close()
            return redirect(url_for('login'))
        
@app.route('/confirm')
def confirm():
    return("success go sleep now")

if __name__=='__main__':
    app.run(debug=True)