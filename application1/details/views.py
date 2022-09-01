# from flask import Flask,render_template,request,Blueprint,jsonify
# import json

# mod=Blueprint('users',__name__)

# dispaly={"id":3,
# "name":"ankur",
# "password":"anku2000"
# }

# with open('application1\\data\\data.json','r+') as data:
#     # json.dump(d,data)
#     data=json.load(data)

# @mod.route('/pune')
# def fifth():
#     return "<p>hello punekar</p>"

# @mod.route('/')
# @mod.route('/admin')
# def first():
#     return render_template('firstpage.html')

# @mod.route('/admin/<name>')
# def second(name):
#     return render_template('secondpage.html',name=name)


# @mod.route('/data')
# def third():
#     return jsonify(data)


# @mod.route('/display')
# def fourth():
#     return render_template('display.html',display=dispaly)


# @mod.route('/login')
# def user_login():
#     return render_template('login.html')







# from flask import Flask, render_template, request,redirect,url_for
# from flask_mysqldb import MySQL
# app = Flask(__name__)


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'ankit@123'
# app.config['MYSQL_DB'] = 'ankit'

# mysql = MySQL(app)

# @app.route("/",methods=["GET"])
# def log_in_():
#     return render_template("index.html")

# @app.route("/log_in_success",methods=["GET"])
# def log_in_success():
#     return render_template('log_in.html')

# @app.route("/for_log_in",methods=["GET"])
# def for_log_in():
#     return render_template("log_in.html")

# @app.route("/sign_up",methods=["GET","POST"])
# def sign_up():
#     if request.method=="POST":
#         name=request.form.get('fname')
#         pswd=request.form.get('pwd')
#         mail=request.form.get('lmail')
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO WEBSITE (name,password,email) VALUES (%s,%s,%s)" , (name,pswd,mail))
#         mysql.connection.commit()
#         cur.close()
#         return redirect(url_for("log_in_success"))


# import json
# data=json.load(open(,'r'))
# @mod.route('/json_sample',methods=['POST'])
# def json_example():
#     user_data=request.get_json()
#     new_user_id=data[-1]['id']+1
#     responce=user_data
#     responce['id']=new_user_id
#     data.append(responce)
#     json.dump(data,open(,'w'))
# #     return jsonify(responce)
   
# from markupsafe import escape

# @mod.route("/<name>")
# def hello(name):
#     # return f"Hello, {escape(name)}!"
#     return escape(render_template('escape.html',name=name))



# from flask import Flask,render_template,request,Blueprint,jsonify
# import json

# mod=Blueprint('users',__name__)

# posts=json.load(open("application1\data\post.json"))
# with open ("application1//data//post.json",'r') as data:
#     posts=json.loads(data.read())


# new_data={
#     "id":3,
#     "name":'Prashant',
#     "description":'Flask'

# }
# with open ("application1//data//post.json",'r+') as data:
#     posts=json.loads(data.read())
#     posts.append(new_data)
#     data=json.dumps(posts)
#     posts=json.loads(data)

# import json





#     print(type(posts))
# print(posts)
# posts=[{"id":1,
# "name":"saurabh",
# "description":"python flask"},
# {"id":2,
# "name":"keshav",
# "description":"html"}
# ]


# import datetime
# @mod.route('/blog')
# def blog():
#     return render_template('blog.html',posts=posts,date=(datetime.datetime.now()).strftime("%x %H-%M %p"))


# if __name__ == '_main_':
#     mod.run(debug=True)


from flask import Blueprint,jsonify,request,json
from application1 import db
from application1.details.models import mytable
# import json

mod=Blueprint('details',__name__,url_prefix='/saurabh')


@mod.route('/',methods=['GET'])
def fetch_users():
    users=mytable.query.all()
   # print(users)
   # print(type(users))
    response=[x.__repr__() for x in users]
    # print(response)
    # response=users.__repr__()
    # print(response)

    return jsonify(response)

