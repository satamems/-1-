class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_info(self):
        return f"Name: {self.name}, ID: {self.id}"
    


class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def get_info(self):
        return f"{super().get_info()}, Department: {self.department}"
    
    def manage_project(self):
        print(f"{self.name} is managing a project.")

    
class Technican(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization

    def get_info(self):
        return f"{super().get_info()}, Specialization: {self.specialization}"
    
    def perform_maintenance(self):
        print(f"{self.name} is performing maintenance tasks.")



class TechManager(Manager, Technican):
    def __init__(self, name, id, department, specialization):
        super().__init__(name, id, department)
        self.specialization = specialization  
        
        
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)


    def get_team_info(self):
        print(f"\nTeam of {self.name}:")
        for employee in self.team:
            print(employee.get_info())

    
    def get_info(self):
        return f"{super().get_info()}, Department: {self.department}, Specialization: {self.specialization}"
    

employee1 = Employee("Petya", 1)
employee2 = Employee("Vanya", 2)
manager = Manager("Volodya", 3, "Sales")
technician = Technican("Ignat", 4, "developer")
tech_manager = TechManager("Sergey", 5, "Engineering", "software engineer")


tech_manager.add_employee(employee1)
tech_manager.add_employee(employee2)   
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)

print(employee2.get_info())
manager.manage_project()
technician.perform_maintenance()
tech_manager.get_team_info()



