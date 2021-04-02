from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import render_template
app = Flask("__name__")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:password@localhost:5432/driverdheko"
db=SQLAlchemy(app)
class Car(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(120),unique=False)
    model=db.Column(db.String(120),unique=False)
    year=db.Column(db.String(120),unique=False) 
    brand=db.Column(db.String(120),unique=False)
    color=db.Column(db.String(120),unique=False)
    reg_number=db.Column(db.String(120),unique=False)   
    def __init__(self, name, model, year,brand,color,reg_number):
        self.name=name
        self.model=model
        self.year=year
        self.brand=brand
        self.color=color
        self.reg_number=reg_number
@app.route('/insert_car', methods=['POST'])
def insertCar():
    newName=request.form['name']
    newModel=request.form['model']
    newYear=request.form['year']
    newBrand=request.form['brand']
    newColor=request.form['color']
    newReg_number=request.form['reg_number']
    user = Car(newName,newModel,newYear,newBrand,newColor,newReg_number)
    db.session.add(user)
    db.session.commit()
    return "<p>Data is updated</p>"
@app.route('/display_cars')
def displayCars():
    car=Car.query.all()
    return render_template("list_cars.html",myCars=car)
@app.route('/remove_car/<id>')
def removeCar(id):
    obj = Car.query.filter_by(id=id).one()
    db.session.delete(obj)
    db.session.commit()
    return "car deleted sucessfully"
if __name__ == '__main__':
    app.run()