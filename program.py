import hr
import Karyawan
import performansi

salary_employee = hr.GajiPegawai(1, 'Filla Kurnia', 15000000)
hourly_employee = hr.PegawaiJam(2, 'Riskon Silalahi', 40, 15)
comission_employee = hr.KomisiPegawai(3, 'Heru Santoso', 15000000, 250000)
payroll_system = hr.SistemPenggajian()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    comission_employee
])

manager = Karyawan.Manager(1, 'Agung Bagus Santoso', 3000000)
secertary = Karyawan.Secertary(2, 'Ulil Absor Maulana', 1500000)
sales_guy = Karyawan.SalesPerson(3, 'Dwi Maulana Hutapea', 1000000, 200000)
factory_worker = Karyawan.FactoryWorker(2, 'Lutfi Ardi Slamet', 40, 15)
employees = [
    manager,
    secertary,
    sales_guy,
    factory_worker
]

productivity_system = performansi.Performansi()
productivity_system.track(employees, 40)
payroll_system = hr.SistemPenggajian()
payroll_system.calculate_payroll(employees)


