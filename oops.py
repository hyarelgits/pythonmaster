print("EMPLOYEE MANAGEMENT SYSTEM")

# Parent Class
class Employee:

    def __init__(self, emp_id, name, salary):
        print("Employee Constructor Called")

        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Employee ID :", self.emp_id)
        print("Employee Name :", self.name)
        print("Salary :", self.salary)


# Child Class
class Manager(Employee):

    def __init__(self, emp_id, name, salary, department):

        super().__init__(emp_id, name, salary)

        self.department = department

    def display_manager(self):
        print("Department :", self.department)


print("\nCreating Employee Object")

e1 = Employee(101, "Rahul", 50000)

e1.display_employee()

print("\nCreating Manager Object")

m1 = Manager(201, "Priya", 80000, "IT")

m1.display_employee()

m1.display_manager()
