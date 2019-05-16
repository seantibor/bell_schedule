from bell_schedule import Period, BellSchedule
from datetime import datetime, timedelta
import pytest, arrow

timezone = 'US/Eastern'

@pytest.fixture(scope="module")
def pc_bellschedule():
    return BellSchedule.from_csv('test_input.csv', tz=timezone)

def test_create_period():
    start_time = arrow.Arrow(2019, 5, 12, 8, 20, tzinfo=timezone)
    end_time = arrow.Arrow(2019, 5, 12, 9, 2, tzinfo=timezone)
    period = Period(name='1', start_time=start_time, end_time=end_time)
    assert period.name == '1'
    assert period.start_time == start_time
    assert period.end_time == end_time

def test_add_period_by_attributes(pc_bellschedule):
    start_count = len(pc_bellschedule.periods)
    pc_bellschedule.add_period('X', datetime.now(), datetime.now())
    assert len(pc_bellschedule.periods) == start_count + 1

def test_add_period_by_namedtuple(pc_bellschedule):
    start_count = len(pc_bellschedule.periods)
    pc_bellschedule.add_period(period=Period('Y', arrow.now(), arrow.now()))
    assert len(pc_bellschedule.periods) == start_count + 1

def test_schedule_to_csv(pc_bellschedule):
    csv_file = 'test_output.csv'
    pc_bellschedule.to_csv(csv_file)

def test_csv_to_schedule(pc_bellschedule):
    csv_file = 'test_input.csv'
    pc_bellschedule = BellSchedule.from_csv(csv_file)
    assert isinstance(pc_bellschedule, BellSchedule)
    assert len(pc_bellschedule.periods) == 13

def test_current_period(pc_bellschedule):
    test_time = datetime(2019, 5, 14, 8, 25)
    period = pc_bellschedule.current_period(test_time)
    assert period.name == '1'

def test_no_current_period(pc_bellschedule):
    test_time = datetime(2019, 5, 14, 18, 25)
    period = pc_bellschedule.current_period(current_time=test_time)
    assert period is None

def test_remove_period_by_name(pc_bellschedule):
    start_count = len(pc_bellschedule.periods)
    pc_bellschedule.remove_period('X')
    assert len(pc_bellschedule.periods) == start_count - 1

def test_remove_period_by_namedtuple(pc_bellschedule):
    start_count = len(pc_bellschedule.periods)
    pc_bellschedule.remove_period(period_tup=Period('Y', datetime.now(), datetime.now()))
    assert len(pc_bellschedule.periods) == start_count - 1