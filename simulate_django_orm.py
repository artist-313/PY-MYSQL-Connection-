import mysql.connector 
conn=mysql.connector.connect(host="localhost",user="root",password="root",use_pure=True,database="DjangoORM")
cur=conn.cursor()
# cur.execute("create database DjangoORM")
# print("data base created")

# cur.execute('''create table employee(id int primary key auto_increment,
# name varchar(20),
# designation varchar(30),
# salary decimal(10,2))
# ''')
# print("table created")



class Employee:
    def create(self,*args,**kwargs):
        cols=""
        placeholder=""
        for col in kwargs.keys():
            if cols!="":
                cols+=","
                placeholder+=","
            cols+=col
            placeholder+="%s"
        query=f"insert into employee({cols}) values({placeholder})"
        values=tuple(kwargs.values())
        cur.execute(query,values)
        conn.commit()
    def list(self,*args,**kwargs):
        cur.execute("select * from employee") 
        # for emp in cur:
        #     print(emp)
        print(cur.fetchall())
    def retreive(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"select * from employee where {key}={kwargs.get(key)}")
        
            print(cur.fetchall())

        
    def update(self,*args,**kwargs):
        print(args)
        print(kwargs)
        for key in kwargs:
            cur.execute(f"update employee set {key}='{kwargs.get(key)}' where id={args[0]}")
            conn.commit()
        


         
    def delete(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"delete from employee where id={args[0]}")
            conn.commit()

    def filter(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"select *from employee where {key}='{kwargs.get(key)}'")
            print(cur.fetchall())

employee=Employee()
while True:
    print("1.create emloyee")
    print("2.list all employees")
    print("3.Employee details view")
    print("4.update employee")
    print("5.delete Employee ")
    print("6.filter")
    print("7.exit")
    choice=int(input("enter a choice:"))
    if choice==1:
        name=input("Enter your name:")
        desig=input("enter your designation:")
        salary=int(input("enter your salary:"))
        employee.create(name=name,designation=desig,salary=salary)
    elif choice==2:
        employee.list()
    elif choice==3:
        # print("")
        id=int(input("enter the employee id:"))
        employee.retreive(id=id)
    elif choice==4:
        id=int(input("enter the id of employee:"))
        print("1.update name:")
        print("2.update designation:")
        print("3.update place:")
        choice=int(input("enter your choice:"))
        if choice==1:
            name=input("Enter the new name:")
            employee.update(id,name=name)
        elif choice==2:
            desig=input("enter the new designation:")
            employee.update(id,designation=desig)
        elif choice==3:
            salary=float(input("enter the new salary:"))
            employee.update(id,salary=salary)
        else:
            print("invalid choice")
    elif choice==5:
        id=int(input("enter the id:"))
    
        employee.delete(id)
    elif choice==6:
        print("filter options")
        print("1.filter by name:")
        print("2.filter by designation:")
        print("3.filter by place:")
        choice=int(input("enter your choice:"))
        if choice==1:
            name=input("Enter the name:")
            employee.filter(name=name)
        elif choice==2:
            desig=input("Enter the designation:")
            employee.filter(designation=desig)
        elif choice==3:
            salary=float(input("Enter the salary:"))
            employee.filter(salary=salary)
    elif choice==7:
        break 
    else:
        print("invalid choice")

    conn.close()
