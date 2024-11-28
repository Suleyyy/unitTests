from importStudents import ImportStudents
import os

class TestImportStudents:


    def test_import_csv(self):
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
        os.remove(path)
        #THEN
        assert want == got


    def test_import_txt(self):
        # GIVEN
        path = os.getcwd()+ os.sep + 'lists\\temp.txt'
        students = []
        file = open(path, 'w')
        str1 = 'John Snow - ABC'
        file.write(str1)
        file.close()
        want = [{'Name': 'John', 'Surname': 'Snow', 'ID': 'ABC'}]
        # WHEN
        got = ImportStudents.txt(path, ["Name", "Surname", "ID"])
        os.remove(path)
        # THEN
        assert want == got

    def test_path_exception(self):
        try:
            ImportStudents.csv('', ["Name", "Surname", "ID"])
        except Exception as e:
            assert str(e) == "Path doesn't exist"


