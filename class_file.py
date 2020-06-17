class Employee:
    #global no_of_employees
    no_of_employees=0
    #salarylist is empty list
    salarylist = []
    def __init__(self, name,family,salary,department):
        self.name = name
        self.family = family
        self.salary = salary
        self.salarylist.append(salary)
        self.department = department
        Employee.no_of_employees +=1

    def average(self):
        sum_num = 0
        for t in self.salarylist:
            sum_num = sum_num + t

        avg = sum_num / len(self.salarylist)
        return avg


class FullTimeEmployee(Employee):
    pass

p1 = FullTimeEmployee("John","Medavarapu",256,"software developer")
p2 = FullTimeEmployee("ram","prasad",780,"software developer")
p3 = FullTimeEmployee("suresh","Medava",782,"software developer")
print("Average value : "+str(p1.average()))

print("no Of Employees : "+str(p1.no_of_employees))
#accessing the data members of a class
print(p1.name)
print(p1.salarylist)

