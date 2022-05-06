import math

print(math.pi)
print(math.e)

radius = 5.0
area = (radius ** 2) * math.pi
theta = math.radians(60)

x = radius * math.cos(theta)
y = radius * math.sin(theta)

print("area: " + str(area))
print("x: " + str(x))
print("y: " + str(y))
