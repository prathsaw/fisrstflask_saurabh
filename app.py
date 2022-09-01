# from flask import Flask,render_template
# app=Flask(__name__,template_folder='application1/templates') # if app.py is ran from outside application1 folder
# #                                                               #  we need to explicitly specify the path for template folder
# # # app=Flask(__name__)

# # @app.route('/')
# @app.route('/about')
# def third():
#     return render_template('about.html')

# @app.route('/pune')
# def first():
#     return '<p>hello pune</p>'

# @app.route('/pune/')
# def sixth():
#     return '<p>hello punekar</p>'

# @app.route('/pune/<name>',methods=['GET'])
# def second(name):
#     return render_template("firstpage.html",name=name) # only filename in given template folder gets render


#     #****************** file path(relative/absolute) won't open render_template file ****************
#     # return render_template('C:/Users/saura/new_application/application1/templates/firstpage.html',name=name)
#     # return render_template("C:\\Users\\saura\\new_application\\application1\\templates\\firstpage.html",name=name)
#     # return render_template("application1\\templates\\firstpage.html",name=name)

# @app.route('/maha')
# def fourth():
#     with open((r'C:\Users\saura\OneDrive\Desktop\bwp.html'),'r') as f:
#         d=f.read()
#         print(type(d))

#     return d # can open any file using file path but cant use file on development server in actual scenario
        
# @app.route('/<name1>/<name2>/')
# def fifth(name1,name2):
#     return render_template('secondpage.html',name1=name1,name2=name2)
# if __name__=='__main__':
    # app.run(debug=True)


from application1 import create_app
import os
config_name=os.getenv('FLASK_CONFIG','development')
app=create_app(config_name)

# from application1 import create_app
# app=create_app()
if __name__=='__main__':
    app.run(debug=True,port=8000)


