from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2020, 5, 8)


def get_hundred_days_end_date(x):
    """Return a string of yyyy-mm-dd"""
    t = timedelta(days = 100)
    return (x + t)

def get_days_between_pb_start_first_joint_pycon(start_date, end_date):
    """Return the int number of days"""
    return (end_date - start_date).days

result1 = get_hundred_days_end_date(start_100days)
result2 = get_days_between_pb_start_first_joint_pycon(pybites_founded, pycon_date)
print ("You will finish 100 days of python on: " + str(result1))
print ("You have " + str(result2) + " days until pycon")