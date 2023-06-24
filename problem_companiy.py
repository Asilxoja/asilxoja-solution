class Employe:
    # Ismini Familiuaysini 
    def set_name(self, name: str) -> str:
        if isinstance(name, str):
            self.name = name
    
    def set_surname(self, surname: str) -> str:
        if isinstance(surname, str):
            self.surname = surname
    # Tug'ilgan kunini
    def set_birth_day(self, birth_day: str) -> str:
        if isinstance(birth_day, str):
            self.birth_day = birth_day
    # ish xaqi
    def set_salary(self, salary: float) -> float:
        if isinstance(salary, float):
            self.salary = salary
    # Ishga kelgan sanasi
    def set_kelgan_sandi(self, date: str) -> str:
        if isinstance(date, str):
            self.date = date
    # ishdagi reytinggi ?
    def set_reyting(self, rating: float) -> float:
        if isinstance(rating, float):
            self.rating = rating
    # Yoshini qaytaradi ? 
    def set_age_returns(self, age: int) -> int:
        if isinstance(age, int):
            self.age = age
    
    def set_now_year(self, year: int) -> int:
        if isinstance(year, int):
            self.year = year
    
    def set_return(self) -> int:
        self.sums = self.year - self.age
    # Yillik_daromadni belgilang
    def set_Annual_income(self, income: float) -> float:
        if isinstance(income, float):
            self.income = income
    # Necha yidan beri ishlayapti ?
    def set_necha_yildan_beri_ishlayapti(self, years: str) -> str:
        if isinstance(years, str):
            self.years = years
    # ///////GET//////
    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_birth_day(self):
        return self.birth_day
    
    def get_now_year(self):
        return self.year
    
    def get_salary(self):
        return self.salary
    
    def get_kelgan_sandi(self):
        return self.date
    
    def get_reyting(self):
        return self.rating
    
    def get_return(self):
        return self.sums
    
    def get_Annual_income(self):
        return self.income
    
    def get_necha_yildan_beri_ishlayapti(self):
        return self.years

class Company:
    def __init__(self):
        self.name = ""
        self.director = ""
        self.profit = 0.0
        self.people = []

    def set_company_name(self, name: str):
        if isinstance(name, str):
            self.name = name

    def set_director(self, director: str):
        if isinstance(director, str):
            self.director = director

    def set_profit(self, profit: float):
        if isinstance(profit, float):
            self.profit = profit

    def add_people(self, people):
        self.people.append(people)

    def remove_people(self, people):
        self.people.remove(people)


if __name__ == "__main__":
    employee = Employe()
    employee.set_name(input("Enter Name: "))
    employee.set_surname(input("Enter Surname: "))
    employee.set_birth_day(input("Enter Birth day: "))
    employee.set_now_year(int(input("Enter now year: ")))
    employee.set_salary(float(input("Enter salary: ")))
    employee.set_kelgan_sandi(input("kelgan sanasni kriting: "))
    employee.set_reyting(float(input("Enter reyting: ")))
    employee.set_age_returns(int(input("Enter age: ")))
    employee.set_return()
    employee.set_Annual_income(float(input("Enter Income: ")))
    employee.set_necha_yildan_beri_ishlayapti(input("Start date: "))

    print(f"Employee Name: {employee.get_name()}, Employee Surname: {employee.get_surname()}\n"
          f"Employee Birth day: {employee.get_birth_day()}, Now year: {employee.get_now_year()}\n"
          f"Salary: {employee.get_salary()}, Start date: {employee.get_necha_yildan_beri_ishlayapti()}")

    company = Company()
    n = int(input("How many employees do you want to add: "))
    for _ in range(n):
        company.set_company_name(input("Company Name: "))
        company.set_director(input("Enter Director: "))
        company.set_profit(float(input("Enter Profit: ")))
        company.add_people(input("Add Employee: "))