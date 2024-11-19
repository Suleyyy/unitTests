from exportStudents import ExportStudents
import os

class TestExportStudents:

    @staticmethod
    def test_csv():
        #Given
        mock = ExportStudents.csv
        path = 'C:/Users/mikol/Desktop/unitTests/SON_ZAD2-main/GitProject/lists/temp.csv'
        students = [{'Name': 'John', 'Surname': 'Snow', 'ID':'ABC'}, {'Name': 'Janusz', 'Surname': 'Tracz', 'ID':'BCA'}]
        mock(path, students)
        want = 'John;Snow;ABC\nJanusz;Tracz;BCA'
        file = open(path, 'r')
        #When
        got = file.read()
        #Then
        assert want == got
        file.close()
        os.remove(path)

    @staticmethod
    def test_txt():
        #Given
        mock = ExportStudents.txt
        path = 'C:/Users/mikol/Desktop/unitTests/SON_ZAD2-main/GitProject/lists/temp.txt'
        students = [{'Name': 'John', 'Surname': 'Snow', 'ID':'ABC'}, {'Name': 'Janusz', 'Surname': 'Tracz', 'ID':'BCA'}]
        mock(path, students)
        want = 'John Snow - ABC\nJanusz Tracz - BCA'
        file = open(path, 'r')
        #When
        got = file.read()
        #Then
        assert want == got
        file.close()
        os.remove(path)