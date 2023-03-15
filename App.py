from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "Secret Key"

"""app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:#Ashrith123@localhost/north_wind'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy=(app)"""

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='#Ashrith123'
app.config['MYSQL_DB']='north_wind'
mysql=MySQL(app)


@app.route("/emp")
def index1():
    cursor=mysql.connection.cursor()
    cursor.execute("select * from employees")
    data=cursor.fetchall()
    cursor.close()
    return render_template("index1.html",employees=data)
    #return render_template("index1.html")

@app.route("/insert", methods=['POST'])
def insert():
    if request.method=='POST':
        EmployeeID=request.form['EmployeeID']
        FirstName=request.form["FirstName"]
        LastName=request.form["LastName"]

        #db.session.execute("INSERT INTO employees (emp_no, first_name, last_name) VALUES (%s, %s, %s)",(emp_no, first_name, last_name))
        #db.session.commit()
        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO employees (EmployeeID,FirstName, LastName) VALUES (%s, %s, %s)",(EmployeeID,FirstName,LastName))
        mysql.connection.commit()
        
        return redirect(url_for('index1'))
    
@app.route("/update", methods=['POST','GET'])
def update():
    if request.method=='POST':
        EmployeeID=request.form['EmployeeID']
        FirstName=request.form["FirstName"]
        LastName=request.form["LastName"]

        #db.session.execute("INSERT INTO employees (emp_no, first_name, last_name) VALUES (%s, %s, %s)",(emp_no, first_name, last_name))
        #db.session.commit()
        cursor=mysql.connection.cursor()
        cursor.execute("UPDATE employees SET FirstName=%s,LastName=%s where EmployeeID=%s",(FirstName, LastName,EmployeeID))
        mysql.connection.commit()
        
    

        return redirect(url_for('index1'))
      
@app.route('/delete/<string:EmployeeID>', methods=['GET'])
def delete(EmployeeID):
    

    cursor=mysql.connection.cursor()
    cursor.execute("delete from employees where EmployeeID=%s",(EmployeeID,))
    mysql.connection.commit()
        
    return redirect(url_for('index1'))

#=====================================================================================================

@app.route("/product")
def index2():
    cursor=mysql.connection.cursor()
    cursor.execute("select * from products")
    data=cursor.fetchall()
    cursor.close()
    return render_template("index2.html",products=data)
    

@app.route("/insert2", methods=['POST'])
def insert2():
    if request.method=='POST':
        ProductID=request.form['ProductID']
        ProductName=request.form["ProductName"]
        SupplierID=request.form["SupplierID"]

        #db.session.execute("INSERT INTO employees (emp_no, first_name, last_name) VALUES (%s, %s, %s)",(emp_no, first_name, last_name))
        #db.session.commit()
        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO products (ProductID,ProductName, SupplierID) VALUES (%s, %s, %s)",(ProductID,ProductName,SupplierID))
        mysql.connection.commit()
        
        return redirect(url_for('index2'))
    
@app.route("/update2", methods=['POST','GET'])
def update2():
    if request.method=='POST':
        ProductID=request.form['ProductID']
        ProductName=request.form["ProductName"]
        SupplierID=request.form["SupplierID"]

        #db.session.execute("INSERT INTO employees (emp_no, first_name, last_name) VALUES (%s, %s, %s)",(emp_no, first_name, last_name))
        #db.session.commit()
        cursor=mysql.connection.cursor()
        cursor.execute("UPDATE products SET ProductName=%s,SupplierID=%s where ProductID=%s",(ProductName, SupplierID,ProductID))
        mysql.connection.commit()
        
    

        return redirect(url_for('index2'))
      
@app.route('/delete2/<string:ProductID>', methods=['GET'])
def delete2(ProductID):
    

    cursor=mysql.connection.cursor()
    cursor.execute("delete from products where ProductID=%s",(ProductID,))
    mysql.connection.commit()
        
    return redirect(url_for('index2'))

#==============================================================================================

@app.route("/orders")
def index3():
    cursor=mysql.connection.cursor()
    cursor.execute("select * from Orders")
    data=cursor.fetchall()
    cursor.close()
    return render_template("index3.html",orders=data)
    

@app.route("/insert3", methods=['POST'])
def insert3():
    if request.method=='POST':
        OrderID=request.form['OrderID']
        EmployeeID=request.form["EmployeeID"]
        CustomerID=request.form["CustomerID"]

        #db.session.execute("INSERT INTO employees (emp_no, first_name, last_name) VALUES (%s, %s, %s)",(emp_no, first_name, last_name))
        #db.session.commit()
        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO Orders (OrderID,CustomerID,EmployeeID) VALUES (%s, %s, %s)",(OrderID,CustomerID,EmployeeID))
        mysql.connection.commit()
        
        return redirect(url_for('index3'))
    
@app.route("/update3", methods=['POST','GET'])
def update3():
    if request.method=='POST':
        OrderID=request.form['OrderID']
        EmployeeID=request.form["EmployeeID"]
        CustomerID=request.form["CustomerID"]

        #db.session.execute("INSERT INTO employees (emp_no, first_name, last_name) VALUES (%s, %s, %s)",(emp_no, first_name, last_name))
        #db.session.commit()
        cursor=mysql.connection.cursor()
        cursor.execute("UPDATE Orders SET CustomerID=%s,EmployeeID=%s where OrderID=%s",(CustomerID,EmployeeID,OrderID))
        mysql.connection.commit()
        
    

        return redirect(url_for('index3'))
      
@app.route('/delete3/<string:OrderID>', methods=['GET'])
def delete3(OrderID):
    

    cursor=mysql.connection.cursor()
    cursor.execute("delete from Orders where OrderID=%s",(OrderID,))
    mysql.connection.commit()
        
    return redirect(url_for('index3'))

#=======================================================================================================

@app.route('/index4/<string:OrderID>', methods=['GET'])
def index4(OrderID):
    cursor=mysql.connection.cursor()
    cursor.execute("select Address,CompanyName,ContactName from Customers,Orders where Customers.CustomerID=Orders.CustomerID and Orders.OrderID=%s",(OrderID,))
    data=cursor.fetchall()
    cursor.close()
    return render_template("index4.html",details=data)

if __name__== "__main__":
    app.run(debug=True)


