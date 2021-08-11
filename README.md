# EPAi-03-Session-13

## Generators and Iteration Tools 

### Assignmnet 1. Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer, then it should be stored as an integer, etc.

```python
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
```

### Assignment 2. Calculate the number of violations by car make.

```python
l = car_instance()

carmake =[]
for items in  list(l):
	carmake.append(items.Vehicle_Make)

	
stats = Counter(carmake)
print(dict(stats))
```
