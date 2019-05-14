from collections import namedtuple
import datetime as dt

Period = namedtuple('Period', ['name','start_time','end_time'])

class BellSchedule():
    
    def __init__(self):
        self.periods = {}

    def add_period(self, period_name: str=None, start_time: dt.datetime=None, end_time: dt.datetime=None, period: Period=None):
        if period:
            self.periods[period.name] = period
        else:
            self.periods[period_name] = Period(period_name, start_time, end_time)

    def remove_period(self, period_name: str=None, period_tup: Period=None):
        if period_tup:
            self.periods.pop(period_tup.name, None)
        else:
            self.periods.pop(period_name, None)

