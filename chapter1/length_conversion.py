# Convert meters to British length units

x = 640 # meters

centimetersPerInch = 2.54
inchesPerFoot = 12
feetPerYard = 3
yardsPerMile = 1760

a = float(x) * 100 / centimetersPerInch # inches
b = float(a) / inchesPerFoot # feet
c = float(b) / feetPerYard # yards
d = float(c) / yardsPerMile # miles

print "%d meters is equal to %.2f inches, %.2f feet, %.2f yards, or %.4f miles" % (x, a, b, c, d)

'''
python length_conversion.py
640 meters is equal to 25196.85 inches, 2099.74 feet, 699.91 yards, or 0.3977 miles
'''
