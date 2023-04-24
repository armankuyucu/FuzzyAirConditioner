very_cold, cold, warm, hot, very_hot = 0, 0, 0, 0, 0
dry, medium, wet = 0, 0, 0
slow, normal, fast = 0, 0, 0

try:
    room_temperature = float(input("°C room temperature: "))
    humidity = float(input("% humidity: "))
except ValueError as e:
    print("Invalid input:", e)
    exit()

# Check if inputs are valid
while humidity < 0 or humidity > 100:
    print("Humidity must be between 0 and 100, please try again")
    humidity = float(input("humidity: "))


def calculate_line_equation(first_point: tuple, second_point: tuple, x: float):
    """ Calculate line equation using two points
    :param first_point: tuple of x and y coordinates of first point
    :param second_point: tuple of x and y coordinates of second point
    :param x:   x coordinate of point to calculate
    :return: calculated y coordinate """
    m = (second_point[1] - first_point[1]) / (second_point[0] - first_point[0])
    b = first_point[1] - m * first_point[0]
    return m * x + b


# Calculate membership values for room temperature
if room_temperature <= 0:
    very_cold, cold, warm, hot, very_hot = 1, 0, 0, 0, 0

elif 0 < room_temperature <= 10:
    very_cold = calculate_line_equation((0, 1), (10, 0), room_temperature)
    cold = calculate_line_equation((0, 0), (10, 1), room_temperature)
    warm, hot, very_hot = 0, 0, 0

elif 10 < room_temperature <= 20:
    cold = calculate_line_equation((10, 1), (20, 0), room_temperature)
    warm = calculate_line_equation((10, 0), (20, 1), room_temperature)
    very_cold, hot, very_hot = 0, 0, 0

elif 20 < room_temperature <= 30:
    warm = calculate_line_equation((20, 1), (30, 0), room_temperature)
    hot = calculate_line_equation((20, 0), (30, 1), room_temperature)
    very_cold, cold, very_hot = 0, 0, 0

elif 30 < room_temperature <= 40:
    hot = calculate_line_equation((30, 1), (40, 0), room_temperature)
    very_hot = calculate_line_equation((30, 0), (40, 1), room_temperature)
    very_cold, cold, warm = 0, 0, 0

elif room_temperature > 40:
    very_cold, cold, warm, hot, very_hot = 0, 0, 0, 0, 1

# Calculate membership values for humidity
if 0 <= humidity <= 50:
    dry = calculate_line_equation((0, 1), (50, 0), humidity)
    medium = calculate_line_equation((0, 0), (50, 1), humidity)
    wet = 0

elif 50 < humidity <= 100:
    dry = 0
    medium = calculate_line_equation((50, 1), (100, 0), humidity)
    wet = calculate_line_equation((50, 0), (100, 1), humidity)


# Define rules
def fuzzy_rule(temperature_membership: float, humidity_membership: float):
    """ Calculate the fuzzy rule
    :param temperature_membership: membership value of room temperature
    :param humidity_membership: membership value of humidity
    :return: minimum of temperature and humidity membership values or 0 if one of them is 0 """
    if temperature_membership != 0 and humidity_membership != 0:
        return min(temperature_membership, humidity_membership)
    return 0


def rule1():
    return fuzzy_rule(very_cold, dry)


def rule2():
    return fuzzy_rule(very_cold, medium)


def rule3():
    return fuzzy_rule(very_cold, wet)


def rule4():
    return fuzzy_rule(cold, dry)


def rule5():
    return fuzzy_rule(cold, medium)


def rule6():
    return fuzzy_rule(cold, wet)


def rule7():
    return fuzzy_rule(warm, dry)


def rule8():
    return fuzzy_rule(warm, medium)


def rule9():
    return fuzzy_rule(warm, wet)


def rule10():
    return fuzzy_rule(hot, dry)


def rule11():
    return fuzzy_rule(hot, medium)


def rule12():
    return fuzzy_rule(hot, wet)


def rule13():
    return fuzzy_rule(very_hot, dry)


def rule14():
    return fuzzy_rule(very_hot, medium)


def rule15():
    return fuzzy_rule(very_hot, wet)


def sugeno():
    """ Calculate the Sugeno inference system """
    numerator = 0
    denominator = 0
    for i in range(1, 16):
        numerator += eval("rule" + str(i) + "()") * output_membership(eval("rule" + str(i) + "()"))
        denominator += eval("rule" + str(i) + "()")
    return numerator / denominator


def output_membership(x):
    if x <= 0.2:
        return 20
    elif 0.2 < x <= 0.4:
        return 40
    elif 0.4 < x <= 0.6:
        return 60
    elif 0.6 < x <= 0.8:
        return 80
    elif 0.8 < x <= 1:
        return 100


output = sugeno()
print(f"fan speed: {output}%")
