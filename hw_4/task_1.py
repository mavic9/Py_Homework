# Author: Viktor Mamontov
# Count of salary for employees with three parameters

from sys import argv

if len(argv) < 4:
    print("Enter completed data (salary per hour, hours and bonus)!")
else:
    sal = (float(argv[1]) * float(argv[2])) + float(argv[3])
    print(sal)
