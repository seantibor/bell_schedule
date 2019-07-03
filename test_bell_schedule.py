from bell_schedule import Period, BellSchedule
import datetime as dt
import pytest, arrow
import os
from freezegun import freeze_time

timezone = "US/Eastern"
test_date = "2019-05-15 08:25"


@freeze_time(test_date)
@pytest.fixture(scope="module")
def pc_bellschedule():
    return BellSchedule.from_csv(
        "test_input.csv", schedule_date=arrow.get(test_date).date(), tz=timezone
    )


def test_create_period():
    start_time = arrow.Arrow(2019, 5, 12, 8, 20, tzinfo=timezone)
    end_time = arrow.Arrow(2019, 5, 12, 9, 2, tzinfo=timezone)
    period = Period(name="1", start_time=start_time, end_time=end_time)
    assert period.name == "1"
    assert period.start_time == start_time
    assert period.end_time == end_time


@freeze_time(test_date)
def test_add_period_by_attributes(pc_bellschedule):
    start_count = len(pc_bellschedule.periods)
    pc_bellschedule.add_period("X", dt.datetime.now(), dt.datetime.now())
    assert len(pc_bellschedule.periods) == start_count + 1

@freeze_time(test_date)
def test_add_period_by_namedtuple(pc_bellschedule):
    start_count = len(pc_bellschedule.periods)
    test_period = Period("Y", arrow.now(), arrow.now())
    pc_bellschedule.add_period(period=test_period)
    assert len(pc_bellschedule.periods) == start_count + 1
    assert pc_bellschedule.get_period('Y') == test_period


def test_schedule_to_csv(pc_bellschedule):
    csv_file = "test_output.csv"
    pc_bellschedule.to_csv(csv_file)

def test_schedule_to_json(pc_bellschedule):
    print(pc_bellschedule.to_json())
    assert '2019-05-15T08:21:00-04:00' in pc_bellschedule.to_json()


@freeze_time(test_date)
def test_csv_to_schedule(pc_bellschedule):
    csv_file = "test_input.csv"
    pc_bellschedule = BellSchedule.from_csv(
        csv_file, schedule_date=dt.date.today(), tz=timezone
    )
    assert isinstance(pc_bellschedule, BellSchedule)
    assert len(pc_bellschedule.periods) == 13

@freeze_time(test_date)
def test_current_period(pc_bellschedule):
    test_time = dt.datetime.now()
    period = pc_bellschedule.current_period(test_time)
    assert period.name == "1"

def test_no_current_period(pc_bellschedule):
    test_time = dt.datetime(2019, 5, 14, 18, 25)
    period = pc_bellschedule.current_period(current_time=test_time)
    assert period is None


def test_remove_period_by_name(pc_bellschedule):
    start_count = len(pc_bellschedule.periods)
    pc_bellschedule.remove_period("X")
    assert len(pc_bellschedule.periods) == start_count - 1

@freeze_time(test_date)
def test_remove_period_by_namedtuple(pc_bellschedule):
    start_count = len(pc_bellschedule.periods)
    pc_bellschedule.remove_period(
        period_tup=Period("Y", dt.datetime.now(), dt.datetime.now())
    )
    assert len(pc_bellschedule.periods) == start_count - 1
