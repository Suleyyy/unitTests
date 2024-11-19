from manageStudent import ModifyStudents
import os


class TestModify:

    @staticmethod
    def test_add_student():
        #Given

        student = []
        want = [{'ID':'ABC','Name':'Janusz','Surname':'Tracz'}]

        #When
        got = ModifyStudents.add_student(student, 'Janusz','Tracz','ABC')
        #Then
        assert got == want

    @staticmethod
    def test_add_student_to_file():
        #Given
        path = 'C:/Users/mikol/Desktop/unitTests/SON_ZAD2-main/GitProject/lists/temp.csv'
        path2 = 'C:/Users/mikol/Desktop/unitTests/SON_ZAD2-main/GitProject/lists/temp.txt'
        if not os.path.exists(path) and not os.path.exists(path2):
            want = 'John;Snow;ABC'
            want2 = 'John Snow - ABC'
            ModifyStudents.add_student_to_file(path, path2, 'John', 'Snow', 'ABC')
            file1 = open(path, 'r')
            file2 = open(path2, 'r')
            #When
            got1 = file1.read()
            got2 = file2.read()

            #Then
            assert got1 == want
            assert got2 == want2

            file1.close()
            file2.close()
            os.remove(path)
            os.remove(path2)
        else:
            want = 'John;Snow;ABC\nJanusz;Tracz;BCA'
            want2 = 'John Snow - ABC\nJanusz Tracz - BCA'
            ModifyStudents.add_student_to_file(path, path2, 'Janusz', 'Tracz', 'BCA')
            file1 = open(path, 'r')
            file2 = open(path2, 'r')
            # When
            got1 = file1.read()
            got2 = file2.read()

            # Then
            assert got1 == want
            assert got2 == want2

            file1.close()
            file2.close()
            os.remove(path)
            os.remove(path2)




