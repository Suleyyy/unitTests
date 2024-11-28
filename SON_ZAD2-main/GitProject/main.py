from importStudents import ImportStudents
from manageStudent import ModifyStudents

path = "lists/student_list.csv"
path2 = "lists/student_list.txt"

lista = ImportStudents.csv(path, ["Name", "Surname", "ID"])
'''
for student in lista:
    print(student.get("Name"), student.get("Surname"), student.get("ID"))

'''
lista2 = ImportStudents.txt(path2, ["Name", "Surname", "ID"])
'''
for student in lista2:
    print(student.get("Name"), student.get("Surname"), student.get("ID"))
'''

#lista2 = ModifyStudents.add_student(lista2, 'Vernon','Roche','3452SDD')

for student in lista2:

    print(student.get("Name"), student.get("Surname"), student.get("ID"))

ModifyStudents.add_student_to_file(path, path2,'Kazimierz','Tracz','CDE1234')
#ModifyStudents.modify_student(path, path2, lista)

#ModifyStudents.delete_student(path, path2, lista)

