
from collections import namedtuple, Counter
import csv


def car_instance():
	f = open('nyc_parking_tickets_extract-1.csv', 'r')
	next(f)
	
	d = csv.reader(f)
	
	cardata = namedtuple('car' , 'Summons_Number,Plate_ID,Registration_State,\
		Plate_Type,Issue_Date,Violation_Code,Vehicle_Body_Type,Vehicle_Make,Violation_Description')
	rows = (cardata(*line) for line in d)

	return rows
		

l = car_instance()

carmake =[]
for items in  list(l):
	carmake.append(items.Vehicle_Make)

	
stats = Counter(carmake)
print(dict(stats))

	


