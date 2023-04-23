very_cold = 0
cold = 0
warm = 0
hot = 0
very_hot = 0

dry = 0
medium = 0
wet = 0

slow = 0
normal = 0
fast = 0

negative_slope = -1 / 10
positive_slope = 1 / 10

room_temperature = float(input("room temperature: "))
humidity = float(input("humidity: "))

while humidity < 0 or humidity > 100:
    humidity = float(input("humidity: "))

# Calculate membership values for room temperature

if room_temperature <= 0:
    very_cold = 1
    cold = 0
    warm = 0
    hot = 0
    very_hot = 0

elif 0 < room_temperature <= 10:
    very_cold = negative_slope * room_temperature + 1
    cold = positive_slope * room_temperature
    warm = 0
    hot = 0
    very_hot = 0

elif 10 < room_temperature <= 20:
    cold = negative_slope * room_temperature + 2
    warm = positive_slope * room_temperature - 1
    very_cold = 0
    hot = 0
    very_hot = 0

elif 20 < room_temperature <= 30:
    warm = negative_slope * room_temperature + 3
    hot = positive_slope * room_temperature - 2
    very_cold = 0
    cold = 0
    very_hot = 0

elif 30 < room_temperature <= 40:
    hot = negative_slope * room_temperature + 4
    very_hot = positive_slope * room_temperature - 3
    very_cold = 0
    cold = 0
    warm = 0

elif room_temperature > 40:
    very_hot = 1
    very_cold = 0
    cold = 0
    warm = 0
    hot = 0

# Calculate membership values for humidity

if humidity <= 40:
    dry = 1
    medium = 0
    wet = 0

elif 40 < humidity <= 50:
    dry = negative_slope * humidity + 5
    medium = positive_slope * humidity - 4
    wet = 0

elif 50 < humidity < 70:
    dry = 0
    medium = 1
    wet = 0

elif 70 < humidity <= 80:
    dry = 0
    medium = negative_slope * humidity + 8
    wet = positive_slope * humidity - 7

elif humidity > 80:
    dry = 0
    medium = 0
    wet = 1


# Defining rules

def rule1():
    if very_cold != 0 and dry != 0:
        print("rule1")
        return min(very_cold, dry)
    return 0


def rule2():
    if very_cold != 0 and medium != 0:
        print("rule2")
        return min(very_cold, medium)
    return 0


def rule3():
    if very_cold != 0 and wet != 0:
        print("rule3")
        return min(very_cold, wet)
    return 0


def rule4():
    if cold != 0 and dry != 0:
        print("rule4")
        return min(cold, dry)
    return 0


def rule5():
    if cold != 0 and medium != 0:
        print("rule5")
        return min(cold, medium)
    return 0


def rule6():
    if cold != 0 and wet != 0:
        print("rule6")
        return min(cold, wet)
    return 0


def rule7():
    if warm != 0 and dry != 0:
        print("rule7")
        return min(warm, dry)
    return 0


def rule8():
    if warm != 0 and medium != 0:
        print("rule8")
        return min(warm, medium)
    return 0


def rule9():
    if warm != 0 and wet != 0:
        print("rule9")
        return min(warm, wet)
    return 0


def rule10():
    if hot != 0 and dry != 0:
        print("rule10")
        return min(hot, dry)
    return 0


def rule11():
    if hot != 0 and medium != 0:
        print("rule11")
        return min(hot, medium)
    return 0


def rule12():
    if hot != 0 and wet != 0:
        print("rule12")
        return min(hot, wet)
    return 0


def rule13():
    if very_hot != 0 and dry != 0:
        print("rule13")
        return min(very_hot, dry)
    return 0

def rule14():
    if very_hot != 0 and medium != 0:
        print("rule14")
        return min(very_hot, medium)
    return 0


def rule15():
    if very_hot != 0 and wet != 0:
        print("rule15")
        return min(very_hot, wet)
    return 0


# Define the Sugeno inference system
def sugeno():
    numerator = rule1() * output_membership(rule1()) + rule2() * output_membership(rule2()) + rule3() * output_membership(
        rule3()) + rule4() * output_membership(rule4()) + rule5() * output_membership(
        rule5()) + rule6() * output_membership(rule6()) + rule7() * output_membership(
        rule7()) + rule8() * output_membership(rule8()) + rule9() * output_membership(
        rule9()) + rule10() * output_membership(rule10()) + rule11() * output_membership(
        rule11()) + rule12() * output_membership(rule12()) + rule13() * output_membership(
        rule13()) + rule14() * output_membership(
        rule14()) + rule15() * output_membership(rule15())
    denominator = rule1() + rule2() + rule3() + rule4() + rule5() + rule6() + rule7() + rule8() + rule9() + rule10() + rule11() + rule12() + rule13() + rule14() + rule15()
    return numerator / denominator


def output_membership(x):
    if x is None:
        return 0
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
print(output)
