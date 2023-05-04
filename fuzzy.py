import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership functions
# Antecedent means input and Consequent means output
temp = ctrl.Antecedent(np.arange(-100, 100, 1), 'temp')  # create temperature range from 0 to 40
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')  # create humidity range from 0 to 100
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')  # create fan speed range from 0 to 100
ac_temp = ctrl.Consequent(np.arange(18, 31, 1), 'ac_temp')  # create ac temperature range from 18 to 30

temp['very cold'] = fuzz.trapmf(temp.universe, [-100, -100, 0, 10])
temp['cold'] = fuzz.trimf(temp.universe, [0, 10, 20])
temp['warm'] = fuzz.trimf(temp.universe, [10, 20, 30])
temp['hot'] = fuzz.trimf(temp.universe, [20, 30, 40])
temp['very hot'] = fuzz.trapmf(temp.universe, [30, 40, 100, 100])

humidity.automf(names=['dry', 'medium', 'wet'])

# Create fan speed output membership functions
fan_speed['very slow'] = fuzz.trimf(fan_speed.universe, [0, 0, 20])  # left, center, and right points of the triangle
fan_speed['slow'] = fuzz.trimf(fan_speed.universe, [0, 20, 40])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [20, 40, 60])
fan_speed['fast'] = fuzz.trimf(fan_speed.universe, [40, 60, 80])
fan_speed['very fast'] = fuzz.trapmf(fan_speed.universe, [60, 80, 100, 100])

# Create temperature output membership functions
ac_temp['very cold'] = fuzz.trimf(ac_temp.universe, [18, 18, 21])
ac_temp['cold'] = fuzz.trimf(ac_temp.universe, [18, 21, 24])
ac_temp['warm'] = fuzz.trimf(ac_temp.universe, [21, 24, 27])
ac_temp['hot'] = fuzz.trimf(ac_temp.universe, [24, 27, 30])
ac_temp['very hot'] = fuzz.trapmf(ac_temp.universe, [27, 30, 30, 30])

# Define fuzzy rules
rule1 = ctrl.Rule(temp['very cold'] & humidity['dry'], (fan_speed['very fast'], ac_temp['very hot']))
rule2 = ctrl.Rule(temp['very cold'] & humidity['medium'], (fan_speed['very fast'], ac_temp['very hot']))
rule3 = ctrl.Rule(temp['very cold'] & humidity['wet'], (fan_speed['fast'], ac_temp['very hot']))
rule4 = ctrl.Rule(temp['cold'] & humidity['dry'], (fan_speed['fast'], ac_temp['hot']))
rule5 = ctrl.Rule(temp['cold'] & humidity['medium'], (fan_speed['fast'], ac_temp['hot']))
rule6 = ctrl.Rule(temp['cold'] & humidity['wet'], (fan_speed['medium'], ac_temp['hot']))
rule7 = ctrl.Rule(temp['warm'] & humidity['dry'], (fan_speed['slow'], ac_temp['warm']))
rule8 = ctrl.Rule(temp['warm'] & humidity['medium'], (fan_speed['very slow'], ac_temp['warm']))
rule9 = ctrl.Rule(temp['warm'] & humidity['wet'], (fan_speed['very slow'], ac_temp['warm']))
rule10 = ctrl.Rule(temp['hot'] & humidity['dry'], (fan_speed['medium'], ac_temp['cold']))
rule11 = ctrl.Rule(temp['hot'] & humidity['medium'], (fan_speed['medium'], ac_temp['cold']))
rule12 = ctrl.Rule(temp['hot'] & humidity['wet'], (fan_speed['fast'], ac_temp['cold']))
rule13 = ctrl.Rule(temp['very hot'] & humidity['dry'], (fan_speed['fast'], ac_temp['very cold']))
rule14 = ctrl.Rule(temp['very hot'] & humidity['medium'], (fan_speed['very fast'], ac_temp['very cold']))
rule15 = ctrl.Rule(temp['very hot'] & humidity['wet'], (fan_speed['very fast'], ac_temp['very cold']))

fuzzy_ctrl = ctrl.ControlSystem(
    rules=[rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15])
fuzzy_system = ctrl.ControlSystemSimulation(fuzzy_ctrl)

room_temp = float(input('Room temperature: '))
while not -100 <= room_temp <= 100:
    print('Room temperature must be between -100 and 100!')
    room_temp = float(input('Room temperature: '))

humidity = float(input('Humidity: '))
while not 0 <= humidity <= 100:
    print('Humidity must be between 0 and 100!')
    humidity = float(input('Humidity: '))

fuzzy_system.input['humidity'] = humidity
fuzzy_system.input['temp'] = room_temp


# Compute the fuzzy system
fuzzy_system.compute()

print(f"fan speed: {fuzzy_system.output['fan_speed']}, ac temp: {fuzzy_system.output['ac_temp']}")
fan_speed.view(sim=fuzzy_system)
ac_temp.view(sim=fuzzy_system)
