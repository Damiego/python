class Students:

    def __init__(self, first, last, matric_no):
        self.first = first
        self.last = last
        self.matric_no = matric_no
        self.email = first + '.' + last + '@School.com'

emp_1 = Students('john', 'jake', 20/481)
emp_2 = Students('jane', 'jones', 20/738)

print (emp_1.email)
print(emp_2.email)

#Generating student email address using there first and last name 