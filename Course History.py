from AbstractTable import AbstractTable


class CourseHistory(AbstractTable):
    _table_name = "Course History"

    class Cols(AbstractTable.Cols):
        CH_ID = "ch_id"
        CH_COURSE = "course"
