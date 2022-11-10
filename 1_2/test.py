with open('recipes.txt', 'rt') as file:
    departments = []
    for line in file:
        department_name = line.strip()
        employees_count = int(file.readline())
        employees = []
        for _ in range(employees_count):
            emp = file.readline().strip().split(' | ')
            name, last_name, birth_date, city = emp
            employees.append({'name': name,
                              'last_name': last_name,
                              'birth_date': birth_date,
                              'city': city})
        file.readline()
        dep = {'name': department_name,
               'employees_count': employees_count,
               'employees': employees}
        departments.append(dep)

print(departments)