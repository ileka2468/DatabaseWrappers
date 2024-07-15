import inspect
from supabase_client import SupaBaseClient


class AbstractTable:
    _table_name = ""  # Default value, should be overridden by subclasses

    class Cols:
        ALL = "*"

    _db = SupaBaseClient.instance()

    @classmethod
    def get_all(cls, *selected_columns) -> list:
        cls._validate_columns(selected_columns)
        return cls._db.from_(cls._table_name).select(','.join(selected_columns) if selected_columns else cls.Cols.ALL).execute().data

    @classmethod
    def get_single_record(cls, where_map: dict, *selected_columns) -> dict:
        cls._validate_columns(selected_columns)
        assert isinstance(where_map, dict) and len(where_map) > 0, \
            "Where map must be a dictionary and have at least one key value pair"

        quoted_columns = [f'"{column}"' for column in selected_columns]
        code = f"cls._db.from_('{cls._table_name}').select({','.join(quoted_columns)}){cls._generate_equalities(where_map)}"
        return eval(code)[0]

    @classmethod
    def get_multiple_records(cls, where_map: dict, *selected_columns) -> list:
        cls._validate_columns(selected_columns)
        assert isinstance(where_map, dict) and len(where_map) > 0, \
            "Where map must be a dictionary and have at least one key value pair"
        quoted_columns = [f'"{column}"' for column in selected_columns]
        code = f"cls._db.from_('{cls._table_name}').select({','.join(quoted_columns)}){cls._generate_equalities(where_map)}"
        return eval(code)

    @classmethod
    def insert(cls, insert_map: dict):
        cls._db.from_(cls._table_name).insert(insert_map).execute()

    @classmethod
    def _generate_equalities(cls, dictionary: dict) -> str:
        code = ""
        for key, value in dictionary.items():
            code += f'.eq("{key}", {cls._value_context(value)})'
        return code + ".execute().data"

    @classmethod
    def _value_context(cls, value):
        if isinstance(value, str):
            return f"'{value}'"
        return value

    @classmethod
    def _validate_columns(cls, columns: tuple):
        members = [variable[1] for variable in cls._get_members()]
        for column in columns:
            if column not in members:
                raise ValueError(f"Column {column} not found in acceptable columns: {members}")

    @classmethod
    def _get_members(cls):
        members = []
        for i in inspect.getmembers_static(cls.Cols):
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]):
                    members.append(i)
        return members
