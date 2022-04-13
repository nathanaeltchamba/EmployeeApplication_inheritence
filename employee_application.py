
from turtle import done


class Employee:

    all_employees = []
    
    def __init__(self, first_name, last_name, email, age):
        self.all_employees.append(self)# once a new employee is created, you can view your employees with "Employee.all"
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        
    def __repr__(self):
        return f'<Employee: {self.first_name} {self.last_name} {self.email} {self.age}>'


class Manager(Employee):
    def __init__(self, first_name, last_name,email, age):
        super().__init__(first_name, last_name, email, age)
        self.man_employees = []
        
            
    def add_employee(self, employee):
        self.man_employees.append(employee)
        
    def show_employees(self):
        print(self.man_employees)
            
    def remove_employee(self):
        self.man_employees.pop()

    def create_employee(self):
        print(f'Creating Employee for {self.first_name}')


        done = False
        while not done:
            prompt = input("Would you like to add an Employee?  'Y' for Yes  'N' for No. ").lower()

            if prompt == 'y':
                f_name = input("Enter Employee First Name:  ")
                l_name = input("Enter Employee Last Name:  ")
                mail = input("Enter Employee Email:  ")
                age_value = int(input("Enter Employee Age:  "))
                self.add_employee(Employee(f_name,l_name,mail,age_value))

            elif prompt == 'n':

                done = True

            # decision = input("Enter Employee First Name:  ")
            # decision = input("Enter Employee Last Name:  ")
            # decision = input("Enter Employee Email:  ")
            # decision = int(input("Enter Employee Age:  "))

            

        # first_name_emp = input("Enter Employee First Name:  ") 
        # last_name_em = input("Enter Employee Last Name:  ")
        # email_emp = input("Enter Employee Email:  ")
        # age_emp = int(input("Enter Employee Age:  "))

        # new_employee = Employee(first_name_emp, last_name_em, email_emp, age_emp)

        # self.add_employee(new_employee)

# Employee

# nate = Employee('Nate', 'Tchamba','natet@gmail.com', 24)
# josh = Employee('Josh', 'Fitzpatrick', 'jfitzpatrick@gmail.com', 23)
# karen = Employee('Karen', 'Smith', 'ksmiths@yahoo.com', 27)
# mylon = Employee('Mylon', 'Weathers', 'mylonw@gmail.com', 22)
# lauren = Employee('Lauren', 'Jackson', 'laurenjack@hotmail.com', 25)

# Managers

joe = Manager('Joe', 'Thomas', 'joet@gmail.com', 25)
mike = Manager('Mike', 'Davis', 'mdavis22@gmail.com', 28)

# jimi = Employee('Jimi', 'Hendrix', 'j@g.com', 28)

joe.create_employee()
joe.show_employees()


mike.create_employee()
mike.show_employees()

