import os
import re



class ModifyStudents:

    name_pattern = r'^[A-Z][a-z]{2,}$'
    id_pattern = r'^[0-9A-Z]{9}$'

    # method to add student to list
    @staticmethod
    def add_student(students,n,s,iden):
        if re.match(ModifyStudents.name_pattern, n) and re.match(ModifyStudents.id_pattern, iden) and re.match(ModifyStudents.name_pattern, s):
            students.append({"Name": n, "Surname": s, "ID": iden})
            return students
        raise Exception('Data are not acceptable')

    # method to add student to file
    @staticmethod
    def add_student_to_file(path, path2,n,s,iden):
        if re.match(ModifyStudents.name_pattern, n) and re.match(ModifyStudents.id_pattern, iden) and re.match(ModifyStudents.name_pattern, s):
            student = [n,s,iden]
            if os.path.exists(path) and os.path.exists(path2):
                file = open(path, "a")
                file2 = open(path2, "a")
                file.write("\n" + ";".join(student))
                file2.write("\n" + student[0] + " " + student[1] + " - " + student[2])
                return
            else:
                file = open(path, "a")
                file2 = open(path2, "a")
                file.write(";".join(student))
                file2.write(student[0] + " " + student[1] + " - " + student[2])
                return
        raise Exception('Data are not acceptable')

    @staticmethod
    def modify_student(students,n,s,iden):
        for student in students:
            if student["ID"] == iden:
                student["Name"] = n
                student["Surname"] = s
                return students
        raise Exception("Student not found")


    @staticmethod
    def delete_student(students, iden):
          for i in range(len(students)):
              if students[i]["ID"] == iden:
                  del students[i]
                  return students
          raise Exception("Student not found.")







