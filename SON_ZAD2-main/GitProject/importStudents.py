import os

class ImportStudents:
    @staticmethod
    def csv(path, student_details_structure):
        if os.path.exists(path):
            students = []

            file = open(path, "r")

            for line in file:
                line = line.rstrip()

                student_details_dict = {}

                student_details = line.split(";")

                for i in range(len(student_details_structure)):
                    student_details_dict[student_details_structure[i]] = student_details[i]

                students.append(student_details_dict)

            file.close()

            return students
        raise Exception("Path doesn't exist")

    @staticmethod
    def txt(path, student_details_structure):
        if os.path.exists(path):
            students = []

            file = open(path, "r")

            for line in file:
                line = line.rstrip()

                student_details_dict = {}

                student_details = [j for i in line.split(" - ") for j in i.split(" ")]

                for i in range(len(student_details_structure)):
                    student_details_dict[student_details_structure[i]] = student_details[i]

                students.append(student_details_dict)

            return students
        raise Exception("Path doesn't exist")

