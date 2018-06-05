# convert miles to killomiters
# 1 mile = 1.6 killometers

# My solution
miles = input("Enter number of miles : ")

miles = int(miles)

killomiters = miles * 1.60934

print('That\'s', killomiters)

# Instructors solution differed in one way
print("{} Miles is Equals to {} Kilometers".format(miles, killomiters))