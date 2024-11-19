import os


class ModifyStudents:
    # method to add student to list
    @staticmethod
    def add_student(students,n,s,id):
        name = n
        surname = s
        student_id = id
        students.append({"Name": name, "Surname": surname, "ID": student_id})

    # method to add student to file
    @staticmethod
    def add_student_to_file(path, path2):
        student = [input("Enter student's name: "), input("Enter student's surname: "), input("Enter student's ID: ")]
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
    def modify_student(students,n,s):
        student_id = input("Enter student's ID to modify: ")
        for student in students:
            if student["ID"] == student_id:
                student["Name"] = n
                student["Surname"] = s
                return
        print("Student not found.")


    @staticmethod
    def delete_student(students, id):
          for student in students:
              if students["ID"] == id:
                  del students[id]
                  return
          print("Student not found.")







