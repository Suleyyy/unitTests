from manageStudent import ModifyStudents
import os


class TestModify:


    def test_add_student(self):
        #Given

        student = []
        want = [{'ID':'ABC123456','Name':'Janusz','Surname':'Tracz'}]

        #When
        got = ModifyStudents.add_student(student, 'Janusz','Tracz','ABC123456')
        #Then
        assert got == want

    def test_add_student_to_file(self):
        #Given
        path = 'temp.csv'
        path2 = 'temp.txt'
        if not os.path.exists(path) and not os.path.exists(path2):
            want = 'John;Snow;ABC123456'
            want2 = 'John Snow - ABC123456'
            ModifyStudents.add_student_to_file(path, path2, 'John', 'Snow', 'ABC123456')
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
            want = 'John;Snow;ABC\nJanusz;Tracz;BCA123456'
            want2 = 'John Snow - ABC\nJanusz Tracz - BCA123456'
            ModifyStudents.add_student_to_file(path, path2, 'Janusz', 'Tracz', 'BCA123456')
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

    def test_modify_student(self):
        #GIVEN
        student = [{'Name':'Janusz','Surname':'Tracz','ID':'ABC'}]
        want = [{'Name':'John','Surname':'Snow','ID':'ABC'}]
        #WHEN
        got = ModifyStudents.modify_student(student,'John','Snow', 'ABC')
        #THEN
        assert got == want

    def test_delete_student(self):
        # GIVEN
        student = [{'Name': 'Janusz', 'Surname': 'Tracz', 'ID': 'ABC'}]
        want = []
        # WHEN
        got = ModifyStudents.delete_student(student, 'ABC')
        # THEN
        assert got == want

    def test_regex(self):
        try:
            student = []
            ModifyStudents.add_student(student, '', '', '')
        except Exception as e:
            assert str(e) == 'Data are not acceptable'

    def test_no_student(self):
        try:
            student = []
            ModifyStudents.modify_student(student, 'Janusz', 'Tracz', '1234ASDFA')
        except Exception as e:
            assert str(e) == 'Student not found'




