from employee import Employee, HourlyEmployee, SalaryEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employee = []

    def add_employee(self, new_employee):
        self.employee.append(new_employee)

    def display_employees(self):
        print("Current employees:")
        for i in self.employee:
            print(i.first_name, i.last_name)
        print("-----------------")

    def pay_employees(self):
        print("Paying employees:")
        for i in self.employee:
            print("Paycheck for", i.first_name, i.last_name)
            print(f"Amount: ${i.calculate_paycheck():,.2f}")
            print("-----------")

def main():
    my_company = Company()

    employee1 = SalaryEmployee("Jim", "Portman", 10000)
    my_company.add_employee(employee1)
    employee2 = CommissionEmployee("Laura", "Smith", 9000, 10, 500)
    my_company.add_employee(employee2)
    employee3 = HourlyEmployee("Michael", "Bortman", 40, 500)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()
