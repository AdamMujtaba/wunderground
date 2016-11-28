from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2015, 01, 01)
end_date = date(2015, 12, 31)
for single_date in daterange(start_date, end_date):
    print 'history_' + single_date.strftime("%Y-%m-%d")