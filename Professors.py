from AbstractTable import AbstractTable


class Professors(AbstractTable):
    _table_name = "Professors"

    class Cols(AbstractTable.Cols):
        PROFESSOR_ID = "professor_id"
        PROFESSOR_NAME = "professor_name"
        PROFESSOR_EMAIL = "professor_email"
        PROFESSOR_POSITION = "professor_position"
        PROFESSOR_SCHOOL = "professor_school"
        RMP_PROFESSOR_DEPARTMENT = "rmp_professor_department"
        RMP_PROFILE_NAME = "rmp_profile_name"
        RMP_PROFILE_ID = "rmp_profile_id"
        PROFILE_PICTURE = "profile_piture"
        FACULTY_ID = "faculty_id"
        RMP_RATING_DISTRO = "rmp_rating_distro"


def main():
    print(Professors.get_multiple_records( {Professors.Cols.PROFESSOR_POSITION: "Professor"}, Professors.Cols.PROFESSOR_NAME, Professors.Cols.PROFESSOR_ID))


main()
