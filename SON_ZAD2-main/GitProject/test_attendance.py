from attendance import Attendance

class TestAttendance:


    def test_attendance_for_all(self):
        #GIVEN
        attendance = Attendance()
        student = {'Name':'John','Surname':'Snow','ID': 'ABC'}
        want = {'2024-11-24': {'John Snow': True}}
        #WHEN
        attendance.check_attendance_for_all('2024-11-24', student, True)
        got = attendance.presence
        #THEN
        assert got == want


    def test_download_attendance(self):
        # GIVEN
        attendance = Attendance()
        attendance.presence = {'2024-11-24': {'John Snow': True}}
        want = {'2024-11-24': {'John Snow': True}}
        # WHEN
        got = attendance.download_attendance('2024-11-24')
        # THEN
        assert got == want


    def test_clear_attendance(self):
        # GIVEN
        attendance = Attendance()
        attendance.presence = {'2024-11-24': {'John Snow': True}}
        want = {}
        # WHEN
        got = attendance.clear_attendance('2024-11-24')
        # THEN
        assert got == want


    def test_modify_attendance(self):
        # GIVEN
        attendance = Attendance()
        attendance.presence = {'2024-11-24': {'John Snow': True}}
        want = {'2024-11-24': {'John Snow': False}}
        # WHEN
        got = attendance.modify_attendance('2024-11-24', 'John Snow', False)
        # THEN
        assert got == want

    def test_no_attendance_exception(self):
        attendance = Attendance()
        attendance.presence = {}
        date = '2024-11-24'
        try:
            attendance.clear_attendance(date)
        except Exception as e:
            assert str(e) == f"No attendance data for {date}."

    def test_modify_attendance_no_student(self):
        attendance = Attendance()
        attendance.presence = {'2024-11-24': {'John Low': True}}
        date = '2024-11-24'
        student_name = 'John Snow'
        try:
            attendance.modify_attendance(date, 'John Snow', False)
        except Exception as e:
            assert str(e) == f"No student data for {student_name}."
