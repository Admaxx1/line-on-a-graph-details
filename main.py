
print('I need two points that are on a perfectly straight line but please dont use 0s')



point_one_x = input('Type in the x-coordinate for the first point: ')
point_one_y = input('Type in the y-coordinate for the first point: ')

point_two_x = input('Type in the x-coordinate for the second point: ')
point_two_y = input('Type in the y-coordinate for the second point: ')

x_difference = (int(point_one_x)-int(point_two_x))
y_difference = (int(point_one_y)-int(point_two_y))
try:
    yintercept = int(point_one_y) - int(point_one_x) * y_difference/x_difference




    print('slope: '+str(y_difference/x_difference))



    print('y intercept: '+str(yintercept))
    point_one_y1 = 0
    point_one_y1 = (y_difference/x_difference)*int(point_one_x)+yintercept
    xintercept = point_one_y1
    print('x intercept: '+str(xintercept))
except ZeroDivisionError:
    print('It seems like there is a zero in your coordinates')

except NameError:
    print('')





























