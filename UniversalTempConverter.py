toK = { 'Celsius': (lambda c: c + 273.15),
        'Fahrenheit': (lambda f: (f + 459.67) / 1.8),
        'Rankine': (lambda r: r / 1.8),
        'Kelvin': (lambda k: k) }

# while True:
magnitude, unit = input('<value> <Kelvin/Rankine/Fahrenheit/Celsius> ? ').split()
k = toK[unit](float(magnitude))
print(k)
#print("%g Kelvin = %g Celsius = %g Fahrenheit = %g Rankine degrees."
#      % (k, k - 273.15, k * 1.8 - 459.67, k * 1.8))
CelsiusVaue = k - 273.15
FahrenheitValue = k * 1.8 - 459.67
RankenValue =  k * 1.8
KelvinValue = k 
print("Celsius value:", CelsiusVaue)
print("FahrenheitValue value:", FahrenheitValue)
print("RankenValue value:", RankenValue)
print("KelvinValue value:", KelvinValue)

KelvinValueRounded = round(KelvinValue, 1)
print("KelvinValue Rounded to tenth:", KelvinValueRounded)