import bell_schedule as bs
import arrow

default_bs = bs.BellSchedule.from_csv("test_input.csv", schedule_date=arrow.now().date(), tz='US/Eastern', )

current_period = default_bs.current_period()

print(current_period)
print(F"The current period is {current_period.name} and it ends {current_period.end_time.humanize()}")