print('Area And Volume Calculator')

width = float(input('enter width: '))
height = float(input('enter height: '))
depth = float(input('enter depth: '))

area = width * height
volume = area * depth

print('The shape has a width of {}\nThe shape has a height of {}\nThe shape has a depth of {}'.format(width, height, depth))
print('The shape has a total Area of', area)
print('The shape has a total Volume of', volume)
