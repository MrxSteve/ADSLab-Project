import datetime
class DateFormat():
    @classmethod
    def convert_date(self, date):
        return datetime.datetime.strptime(date, '%d/%m/%Y')