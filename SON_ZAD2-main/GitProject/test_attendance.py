from attendance import Attendance

class TestAttendance:

    @staticmethod
    def test_attendance_for_all():
        #GIVEN
        attendance = Attendance()
        student = {'Name':'John','Surname':'Snow','ID': 'ABC'}
        want = {'2024-11-24': {'John Snow': True}}
        #WHEN
        attendance.check_attendance_for_all('2024-11-24', student, True)
        got = attendance.presence
        #THEN
        assert got == want

    @staticmethod
    def test_download_attendance():
        # GIVEN
        attendance = Attendance()
        attendance.presence = {'2024-11-24': {'John Snow': True}}
        want = {'2024-11-24': {'John Snow': True}}
        # WHEN
        got = attendance.download_attendance('2024-11-24')
        # THEN
        assert got == want

    @staticmethod
    def test_clear_attendance():
        # GIVEN
        attendance = Attendance()
        attendance.presence = {'2024-11-24': {'John Snow': True}}
        want = {}
        # WHEN
        got = attendance.clear_attendance('2024-11-24')
        # THEN
        assert got == want

    @staticmethod
    def test_modify_attendance():
        # GIVEN
        attendance = Attendance()
        attendance.presence = {'2024-11-24': {'John Snow': True}}
        want = {'2024-11-24': {'John Snow': False}}
        # WHEN
        got = attendance.modify_attendance('2024-11-24', 'John Snow', False)
        # THEN
        assert got == want



