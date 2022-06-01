class Date():
    def __init__(self, str_DMY: str = ''):
        self.str_DMY = str_DMY

    def __str__(self):
        return self.str_DMY

    @classmethod
    def parce(cls, date = ''):
        dmy = date.split('-')
        return Date.validate(dmy[0], dmy[1], dmy[2])

    @staticmethod
    def validate(day: int = 0, month: int = 0, year: int = 0) -> list:
        day = Date.clear_int_str(day)
        month = Date.clear_int_str(month)
        year = Date.clear_int_str(year)

        return (day if day > 0 and day <= 31 else 1,
                month if day > 0 and day <= 12 else 1,
                year if day > 1900 and day <= 2100 else 1900)

    @staticmethod
    def clear_int_str(some_str: str = '') -> int:
        int_out = int(some_str)
        return int_out if int_out > 0 else 0


print(Date('5-10-2002'))
print(Date.validate(5, 10, 2002))
print(Date.parce('5-10-2002'))
