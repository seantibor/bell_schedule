from collections import namedtuple, OrderedDict
import datetime as dt
import csv
import arrow

Period = namedtuple('Period', ['name','start_time','end_time'])
datetime_format = 'YYYY-M-D H:mm'

class BellSchedule():
    
    def __init__(self, tz: dt.tzinfo=None):
        self.periods = OrderedDict()
        self.tz = tz

    def add_period(self, period_name: str=None, start_time: dt.datetime=None, end_time: dt.datetime=None, period: Period=None) -> None:
        if period:
            self.periods[period.name] = period
        else:
            self.periods[period_name] = Period(period_name, arrow.Arrow.fromdatetime(start_time, tzinfo=self.tz), arrow.Arrow.fromdatetime(end_time, tzinfo=self.tz))

    def remove_period(self, period_name: str=None, period_tup: Period=None) -> None:
        if period_tup:
            self.periods.pop(period_tup.name, None)
        else:
            self.periods.pop(period_name, None)

    def get_period(self, period_name: str) -> Period:
        return self.periods[period_name]

    def as_list_of_dicts(self) -> list:
        return [period._asdict() for period in self.periods.values()]

    @classmethod
    def from_csv(cls, filename: str, tz: dt.tzinfo=None):
        bell_schedule = BellSchedule()
        with open(filename) as infile:
            bellreader = csv.DictReader(infile)
            for row in bellreader:
                bell_schedule.add_period(row['name'], arrow.get(row['start_time'], datetime_format), arrow.get(row['end_time'], datetime_format))

        return bell_schedule

    def to_csv(self, filename: str) -> None:
        with open(filename, 'w') as outfile:
            fieldnames = ['name', 'start_time', 'end_time']
            bellwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
            bellwriter.writeheader()
            for row in self.as_list_of_dicts():
                bellwriter.writerow(row)

    def current_period(self, current_time=dt.datetime.now()):
        current_time = arrow.Arrow.fromdatetime(current_time, tzinfo=self.tz)
        for period in self.periods.values():
            if period.start_time < current_time and current_time < period.end_time:
                return period
        return None
