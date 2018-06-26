
import time
import sys

#f name
#l name
#age
#emp id
#mail id

em_list = []

class employee:
    def __init__(self,f_name,l_name,age,Emp_id):
        self.Attendance = True
        self.First_name = f_name
        self.Last_name = l_name
        self.Name = self.First_name + self.Last_name
        self.Age = age
        self.Employee_id = Emp_id
        self.mail_id = self.First_name + self.Last_name + "@company.com"

def Create_Employee():
    f_name = input("Enter First Name:")
    l_name = input("Enter Last Name:")
    age = input("Enter Age:")
    Employee_code = input("Enter Employee code:")
    emp_obj = employee(f_name,l_name,age,Employee_code)
    return emp_obj

def View_Employee_Details():
    emp_code = input("Enter Your Employee Code:")

    for obj in em_list:
        if emp_code == obj.Employee_id:
            print("Employee Name: {}".format(obj.Name))
            print("Employee Age : {}".format(obj.Age))

def Attendance_Details():
    emp_code = input("Enter Your Employee Code:")

    for obj in em_list:
        if emp_code == obj.Employee_id:
            if obj.Attendance:
                print("Employee Name : {}".format(obj.Name))
                print("In-Time :" + time.ctime())
                obj.Attendance = False

            else:
                print("Employee Name : {}".format(obj.Name))
                print("Out-Time :" + time.ctime())
                obj.Attendance = True



while True:
    print("Enter 1 For New Employee Details:")
    print("Enter 2 To View Employee Details:")
    print("Enter 3 For Attendance:")

    option = int(input())

    if option == 1:
        em_list.append(Create_Employee())

    elif option == 2:
        View_Employee_Details()

    elif option == 3:
        Attendance_Details()


    else:
        print("Invalid Input!")








