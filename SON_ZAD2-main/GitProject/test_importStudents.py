from importStudents import ImportStudents
import os

class TestImportStudents:

    @staticmethod
    def test_import_csv():
        #GIVEN
        path = 'temp.csv'
        students = []
        file = open(path, 'w')
        str1 = 'John;Snow;ABC'
        file.write(str1)
        file.close()
        want = [{'Name':'John', 'Surname':'Snow', 'ID':'ABC'}]
        #WHEN
        got = ImportStudents.csv(path, ["Name", "Surname", "ID"])
        #THEN
        assert want == got
        os.remove(path)

    @staticmethod
    def test_import_txt():
        # GIVEN
        path = 'temp.txt'
        students = []
        file = open(path, 'w')
        str1 = 'John Snow - ABC'
        file.write(str1)
        file.close()
        want = [{'Name': 'John', 'Surname': 'Snow', 'ID': 'ABC'}]
        # WHEN
        got = ImportStudents.txt(path, ["Name", "Surname", "ID"])
        # THEN
        assert want == got
        os.remove(path)
