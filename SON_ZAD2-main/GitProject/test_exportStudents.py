from exportStudents import ExportStudents

class testExportStudents:
    mock = ExportStudents.csv
    mock2 = ExportStudents.txt

    def test_csv(self):
        #Given
        path = 'C:/Users/mikol/Desktop/unitTests/SON_ZAD2-main/GitProject/lists/temp.csv'
        students = [{'Name': 'John', 'Surname': 'Snow'}, {'Name': 'Janusz', 'Surname': 'Tracz'}]
        self.mock(path, students)
        want = ['John;Snow\nJanusz;Tracz']
        file = open(path, 'r')
        #When
        got = file.read()
        #Then
        assert want == got
