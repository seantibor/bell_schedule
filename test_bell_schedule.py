from bell_schedule import Period, BellSchedule
from datetime import datetime, timedelta
import pytest

@pytest.fixture(scope="module")
def pc_bellschedule():
    return BellSchedule()

def test_create_period():
    start_time = datetime(2019, 5, 12, 8, 20)
    end_time = datetime(2019, 5, 12, 9, 2)
    period = Period(name='1', start_time=start_time, end_time=end_time)
    assert period.name == '1'
    assert period.start_time == start_time
    assert period.end_time == end_time

def test_add_period_by_attributes(pc_bellschedule):
    start_count = len(pc_bellschedule.periods)
    pc_bellschedule.add_period('1', datetime.now(), datetime.now())
    assert len(pc_bellschedule.periods) == start_count + 1

def test_add_period_by_namedtuple(pc_bellschedule):
    start_count = len(pc_bellschedule.periods)
    pc_bellschedule.add_period(period=Period('2', datetime.now(), datetime.now()))
    assert len(pc_bellschedule.periods) == start_count + 1

def test_remove_period_by_name(pc_bellschedule):
    start_count = len(pc_bellschedule.periods)
    pc_bellschedule.remove_period('1')
    assert len(pc_bellschedule.periods) == start_count - 1