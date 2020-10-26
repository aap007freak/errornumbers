from ErrorNumber import ErrorNumber


def dms_to_decimal(degrees, minutes):
 return degrees + minutes / 60

phi_1 = ErrorNumber(dms_to_decimal(2, 15), dms_to_decimal(0,1))
phi_2 = ErrorNumber(dms_to_decimal(286, 45), dms_to_decimal(0,1))
print(phi_2.minus(phi_1))
