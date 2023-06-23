class SistemPenggajian:
    def calculate_payroll(self, employees):
        print('Penghitungan Penggajian')
        print('=======================================================')
        for employee in employees:
            print(f'Penggajian untuk \t: {employee.id} - {employee.name}')
            print(f' - Check jumlahnya \t: {employee.calculate_payroll()}')
            print('')
            
class Pegawai:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
class GajiPegawai(Pegawai):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
        
    def calculate_payroll(self):
        return self.weekly_salary
    
class PegawaiJam(Pegawai):
    def __init__(self, id, name, hour_worked, hour_rate):
        super().__init__(id, name)
        self.hour_worked = hour_worked
        self.hour_rate = hour_rate
        
    def calculate_payroll(self):
        return self.hour_worked * self.hour_rate
    
class KomisiPegawai(GajiPegawai):
    def __init__(self, id, name, weekly_salary, comission):
        super().__init__(id, name, weekly_salary)
        self.comission = comission
        
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.comission
        
    