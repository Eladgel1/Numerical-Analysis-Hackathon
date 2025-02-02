import math


# Formula 1
def form_1(l):
    return 4.86 + 0.018 * l


# Formula 2
def form_2(l):
    return l / 3000


# Formula 3
def form_3(l):
    return 0.0047 + 0.0023 * math.log(l) + 0.000043 * pow(math.log(l), 2)


# Formula 4
def form_4(l):
    return 42 + 0.0015 * pow(l, 4/3)


# Formula 5
def form_5(l):
    return 0.069 + 0.00156 * l + 0.00000047 * pow(l ,2)


# L Values
values = [2928, 1250, 396, 9000, 1200, 7502]

# Formulas Values
form1_values = [form_1(v) for v in values]
form2_values = [form_2(v) for v in values]
form3_values = [form_3(v) for v in values]
form4_values = [form_4(v) for v in values]
form5_values = [form_5(v) for v in values]

print("Formula 1 Values =", form1_values)
print("Formula 2 Values =", form2_values)
print("Formula 3 Values =", form3_values)
print("Formula 4 Values =", form4_values)
print("Formula 5 Values =", form5_values)