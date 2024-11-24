import os


class ModifyStudents:
    # method to add student to list
    @staticmethod
    def add_student(students,n,s,iden):
        students.append({"Name": n, "Surname": s, "ID": iden})
        return students

    # method to add student to file
    @staticmethod
    def add_student_to_file(path, path2,n,s,iden):
        student = [n,s,iden]
        if os.path.exists(path) and os.path.exists(path2):
            file = open(path, "a")
            file2 = open(path2, "a")
            file.write("\n" + ";".join(student))
            file2.write("\n" + student[0] + " " + student[1] + " - " + student[2])
        else:
            file = open(path, "a")
            file2 = open(path2, "a")
            file.write(";".join(student))
            file2.write(student[0] + " " + student[1] + " - " + student[2])

    @staticmethod
    def modify_student(students,n,s,iden):
        for student in students:
            if student["ID"] == iden:
                student["Name"] = n
                student["Surname"] = s
                return students
        print("Student not found.")


    @staticmethod
    def delete_student(students, iden):
          for i in range(len(students)):
              if students[i]["ID"] == iden:
                  del students[i]
                  return students
          print("Student not found.")







