from errornumbers import ErrorNumber as EN
from errornumbers.ErrorNumberFunctions import sin
import math

#in degrees
alpha = EN(60, 0.5)
delta = EN(40, 1.2)

radian_alpha = alpha.timesc(math.pi).divided_byc(180)
radian_delta = delta.timesc(math.pi).divided_byc(180)


numerator = sin( radian_alpha.plus(radian_delta).divided_byc(2))
denominator = sin(radian_alpha.divided_byc(2))

n = numerator.divided_by(denominator)

n_degrees = n.timesc(180).divided_byc(math.pi)
print(n)
