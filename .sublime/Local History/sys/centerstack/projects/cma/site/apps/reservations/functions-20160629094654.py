from datetime import datetime, date
import calendar

def monthdiff(start_period, end_period, decimal_places = 2):
	if start_period > end_period:
		raise Exception('Start is after end')
	if start_period.year == end_period.year and start_period.month == end_period.month:
		days_in_month = calendar.monthrange(start_period.year, start_period.month)[1]
		days_to_charge = end_period.day - start_period.day+1
		diff = round(float(days_to_charge)/float(days_in_month), decimal_places)
		return diff
	months = 0
	if start_period.day > 1:
		last_day_in_start_month = calendar.monthrange(start_period.year, start_period.month)[1]
		days_to_charge = last_day_in_start_month - start_period.day	+1
		months = months + round(float(days_to_charge)/float(last_day_in_start_month), decimal_places)
		start_period = datetime(start_period.year, start_period.month+1, 1)
	last_day_in_last_month = calendar.monthrange(end_period.year, end_period.month)[1]
	if end_period.day != last_day_in_last_month:
		months = months + round(float(end_period.day) / float(last_day_in_last_month), decimal_places)
		last_day_in_previous_month = calendar.monthrange(end_period.year, end_period.month - 1)[1]
		end_period = datetime(end_period.year, end_period.month - 1, last_day_in_previous_month)
	if start_period != end_period:
		months = months + (end_period.year - start_period.year) * 12 + (end_period.month - start_period.month) + 1
	diff = round(months, decimal_places)
	return diff


	assert monthdiff(datetime(2015,1,1), datetime(2015,1,31)) == 1
	assert monthdiff(datetime(2015,1,1), datetime(2015,02,01)) == 1.04
	assert monthdiff(datetime(2014,1,1), datetime(2014,12,31)) == 12
	assert monthdiff(datetime(2014,7,1), datetime(2015,06,30)) == 12
	assert monthdiff(datetime(2015,1,10), datetime(2015,01,20)) == 0.35
	assert monthdiff(datetime(2015,1,10), datetime(2015,02,20)) == 0.71 + 0.71
	assert monthdiff(datetime(2015,1,31), datetime(2015,02,01)) == round(1.0/31.0,2) + round(1.0/28.0,2)
	assert monthdiff(datetime(2013,1,31), datetime(2015,02,01)) == 12*2 + round(1.0/31.0,2) + round(1.0/28.0,2)