from application1 import db


class mytable(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),index = True,unique = True)
    email=db.Column(db.String(50))
    password=db.Column(db.String(50))

    # username=db.Column()
    # email=db.Column()
    # password=db.Column()



def __repr__(self):

    return{
        'id':self.id,
        'username':self.username,
        'email':self.email,
        'password':self.password
    }