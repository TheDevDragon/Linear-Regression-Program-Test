#This program is used to find the Linear Regression of a data set in order to better understand the data collected

#This function calculates for the y value using the slope intercept formula
def get_y(m,x,b):
    y = m * x + b
    return y

#Testing Code Block: Get Y Function
get_y(3,0,8) == 8
get_y(4,15,9) == 36

#---------------------------------------

#Here we calculate for the error by finding the distance
#Using the abs() function we can find the distance by finding the difference bewtween y and y_point
def calculate_error(m,b,point):
    x_point, y_point = point
    y = m * x_point + b
    distance = abs(y - y_point)
    return distance

#Testing Code Block 2: Calcualte Error Function

#this is a line that looks like y = x, so (6, 6) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (6, 6)))
#the point (5, 6) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (5, 6)))
#the point (6, 6) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (6, 6)))
#the point (6, 6) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (6, 6)))

#-----------------------------------------

#This function should iterate through each point in points and calculate the error from the point to the line
def calculate_all_error(m,b,datapoints):
    total_error = 0
    for point in datapoints:
        point_error = calculate_error(m,b,point)
        total_error += point_error
    return total_error 

#Testing Code Block 3: Calculate All Errors Function

#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))

#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))

#--------------------------------------------

#Creates a list of possible slope values ranging from -10 to 10
possible_ms = [m * 0.1 for m in range(-10, 10)]

#Creates a list of possible intercept values ranging from -20 to 20
possible_bs = [b * 0.1 for b in range(-20, 20)]

#Sample data set
datapoints = [(3,2),(2,4),(4,8),(5,3),(4,6)]

#This code block checks for the smallest possible error within a given data set 
smallest_error = float("inf")
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m,b,datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error

print(best_m, best_b, smallest_error)