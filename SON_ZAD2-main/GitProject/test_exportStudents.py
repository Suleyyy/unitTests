from exportStudents import ExportStudents
import os

class TestExportStudents:

    def test_csv(self):
        #Given
        mock = ExportStudents.csv
        path = os.getcwd() + os.sep +'lists\\temp.csv'
        with open(path, 'w') as file:
            pass
        students = [{'Name': 'John', 'Surname': 'Snow', 'ID':'ABC123456'}, {'Name': 'Janusz', 'Surname': 'Tracz', 'ID':'BCA123456'}]
        mock(path, students)
        want = 'John;Snow;ABC123456\nJanusz;Tracz;BCA123456'
        file = open(path, 'r')
        #When
        got = file.read()
        file.close()
        os.remove(path)
        #Then
        assert want == got


    def test_txt(self):
        #Given
        mock = ExportStudents.txt
        path = os.getcwd() + os.sep +'lists\\temp.csv'
        with open(path, 'w') as file:
            pass
        students = [{'Name': 'John', 'Surname': 'Snow', 'ID':'ABC123456'}, {'Name': 'Janusz', 'Surname': 'Tracz', 'ID':'BCA123456'}]
        mock(path, students)
        want = 'John Snow - ABC123456\nJanusz Tracz - BCA123456'
        file = open(path, 'r')
        #When
        got = file.read()
        file.close()
        os.remove(path)
        #Then
        assert want == got

    def test_path_exception(self):
        mock = ExportStudents.csv #/txt
        try:
            students = [{'Name': 'John', 'Surname': 'Snow', 'ID': 'ABC123456'},
                        {'Name': 'Janusz', 'Surname': 'Tracz', 'ID': 'BCA123456'}]
            mock('',students)
        except Exception as e:
            assert str(e) == 'Path does not exist'

    def test_empty_exception(self):
        #GIVEN
        mock = ExportStudents.csv
        students = [{'Name': '', 'Surname': '', 'ID': ''},
                    {'Name': '', 'Surname': '', 'ID': ''}]
        path = os.getcwd() + os.sep + 'lists\\temp.csv'
        with open(path, 'w'):
            pass
        #WHEN
        try:
            mock(path,students)
        except Exception as e:
        #THEN
            assert str(e) == 'Trying to export empty list'




