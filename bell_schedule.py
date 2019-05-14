from collections import namedtuple
import datetime as dt
import csv

Period = namedtuple('Period', ['name','start_time','end_time'])

class BellSchedule():
    
    def __init__(self):
        self.periods = {}

    def add_period(self, period_name: str=None, start_time: dt.datetime=None, end_time: dt.datetime=None, period: Period=None) -> None:
        if period:
            self.periods[period.name] = period
        else:
            self.periods[period_name] = Period(period_name, start_time, end_time)

    def remove_period(self, period_name: str=None, period_tup: Period=None) -> None:
        if period_tup:
            self.periods.pop(period_tup.name, None)
        else:
            self.periods.pop(period_name, None)

    def get_period(self, period_name: str) -> Period:
        return self.periods[period_name]

    def as_list_of_dicts(self) -> list:
        return [{'period_name': period.name, 'start_time': period.start_time, 'end_time': period.end_time} for period in self.periods.values()]

    @classmethod
    def from_csv(cls, filename: str):
        bell_schedule = BellSchedule()
        with open(filename) as infile:
            bellreader = csv.DictReader(infile)
            for row in bellreader:
                bell_schedule.add_period(row['period_name'], dt.datetime.strptime(row['start_time'], '%Y-%m-%d %H:%M'), dt.datetime.strptime(row['end_time'], '%Y-%m-%d %H:%M'))

        return bell_schedule

    def to_csv(self, filename: str) -> None:
        with open(filename, 'w') as outfile:
            fieldnames = ['period_name', 'start_time', 'end_time']
            bellwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
            bellwriter.writeheader()
            for row in self.as_list_of_dicts():
                bellwriter.writerow(row)

    def current_period(self, current_time=dt.datetime.now()):
        for period in self.periods.values():
            if period.start_time < current_time and current_time < period.end_time:
                return period
        return None
