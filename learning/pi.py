# floating point formatting
import datetime

print("PI equals {0}".format(22 / 7))
example_of_variable = datetime.datetime.now()
test_variable = 1024
# 2 decimal places
print("PI equals {0:.2f}".format(22 / 7))
example_of_variable = datetime.datetime.now()
# 10 decimal places
print("PI equals {0:.10f}".format(22 / 7))
