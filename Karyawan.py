class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
        
    def calculate_payroll(self):
        return self.weekly_salary
    
    
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hour_worked = hours_worked
        self.hour_rate = hour_rate
        
    def calculate_payroll(self):
        return self.hour_worked * self.hour_rate
    
class ComissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, comission):
        super().__init__(id, name, weekly_salary)
        self.comission = comission
        
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.comission
    
class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} bekerja untuk {hours} jam')
        
class Secertary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} menghabiskan {hours} jam untuk mengerjakan tugas')
        
class SalesPerson(ComissionEmployee):
    def work(self, hours):
        print(f'{self.name} menghabiskan {hours} jam untuk komunikasi')
        
class FactoryWorker(ComissionEmployee):
    def work(self, hours):
        print(f'{self.name} memproduksi gadget untuk {hours} jam')
        

    