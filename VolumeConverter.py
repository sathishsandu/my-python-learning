# Temp script for Volume Conversion
# need code for cubic-inches and cubic-feet

#volumes_uom_list = [liters, tablespoons, cubic_inches, cups, cubic_feet, gallons]

#convert_dict = {
#        tablespoons: {cups: Decimal('0.063'), liters: Decimal('0.015'), gallons: Decimal('0.004')},
#        cups: {tablespoons: Decimal('16'), liters: Decimal('0.247'), gallons: Decimal('0.063')},
#        liters: {tablespoons: Decimal('67.63'), cups: Decimal('4.23'), gallons: Decimal('0.26')},
#        gallons: {tablespoons: Decimal('256'), cups: Decimal('16'), liters: Decimal('3.79')}
#    }

# convert everything to tablespoons UOM
toT = { 'liters': (lambda l: l * 67.628),
        'gallons': (lambda g: g * 256),
        'cups': (lambda c: c * 16),
        'cubicInches': (lambda ci: ci * 1.10823),
        'cubicFeet': (lambda cf: cf * 1915.01),
        'tablespoons': (lambda t: t) }

magnitude, unit = input('<value> <tablespoons/cups/liters/gallons> ? ').split()
t = toT[unit](float(magnitude))
# noW convert back from tablespoons to each UOM
litersValue = t * 0.0147868
gallonsValue = t * 0.00390625
cupsValue =  t * 0.0625
cubicInchesValue = t * 0.902344
cubicFeetValue = t * 0.00052219
tablespoonsValue = t

print("litersValue is:", litersValue)
print("gallonsValue is:", gallonsValue)
print("cupsValue is:", cupsValue)
print("cubicInchesValue is:", cubicInchesValue)
print("cubicFeetValue is:", cubicFeetValue)
print("tablespoonsValue is:", tablespoonsValue)

