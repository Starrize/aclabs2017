CURRENT_YEAR = 2017
from datetime import datetime, date, time
class Person(object):
	def __init__(self,year,month = 0,day = 0):
		self._year = year
		
	def get_age(self):
		#return CURRENT_YEAR - self.year
		now = datetime.now()
		delta = datetime.timedelta(365 * self.year)
		diff = now - delta
		fmt = "{years} years {months} months {days} days"
		output = fmt.format(years = diff.year, months = diff.month, days = diff.day)
		return output
		#return datetime.now() - datetime.delta(year = self.year)
	
	def get_age1(self):
		if datetime.now().month - self.month > 0:
			extra = extra + 1
		if datetime.now.month == self.month and datetime.now().day - self.day:
			extra = extra + 1
		return datetime.now().year - self.year + extra
	
	@classmethod
	def from_string(cls, datestring):
		date = datetime.strptime(datestring,'%Y/%m/%d')
		return cls(year = date.year, month = date.month, day = date.day)