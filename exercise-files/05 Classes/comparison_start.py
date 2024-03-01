# Use special methods to compare objects to each other


class Employee():
    """
    Every employee object with attributes :
    'fname', 'lname', 'level', 'yrsService'
    are keeps in list Employee.dept
    """
    dept = []
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService
        self.dept.append(self)

    # TODO: implement comparison functions by emp level
    def __str__(self) -> str:
        return f"{self.fname} {self.lname} : level {self.level}, service years {self.seniority}"

    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        return self.level == other.level and self.seniority == other.seniority

def main():
    # define some employees
    Tim=Employee("Tim", "Sims", 5, 9)
    John=Employee("John", "Doe", 4, 12)
    Jane=Employee("Jane", "Smith", 6, 6)
    Rebecca=Employee("Rebecca", "Robinson", 5, 13)
    Tyler=Employee("Tyler", "Durden", 5, 12)

    # TODO: Who's more senior?
    print(f"Is Tim more senior than Jane? : {bool(Tim>Jane)}")
    print(f"Is Tyler less senior than Rebecca? : {bool(Tyler < Rebecca)}")

    # TODO: sort the items
    Employee.dept=sorted(Employee.dept,reverse=True)
    print("The best employeeees are : ")
    for i,employeee in enumerate(Employee.dept,start=1):
        print(f"{i} : {employeee}")

if __name__ == "__main__":
    main()
