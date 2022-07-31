#Задача лп методом Эрроу-Гурвица

h = 0.001
e = 0.0001
x01 = 3
x02 = 4
alpha1 = 0
alpha2 = 0
x_last = 0
der_g1_x1 = -1
der_g1_x2 = -2
der_g2_x1 = -5
der_g2_x2 = -2
iterations = 0


def math_function(local_x1: float, local_x2: float) -> float:
    return -(local_x1 - 6) ** 2 - (local_x2 - 8) ** 2


def g1(local_x1: float, local_x2: float) -> float:
    return 16 - local_x1 - 2 * local_x2


def g2(local_x1: float, local_x2: float) -> float:
    return 40 - 5 * local_x1 - 2 * local_x2


def derivative_x1(local_x1: float) -> float:
    return -2 * local_x1 + 12


def derivative_x2(local_x2: float) -> float:
    return -2 * local_x2 + 16


def new_point(is_range: bool):
    global x01, x02, alpha1, alpha2
    if not is_range:
        alpha1 = max(0,alpha1 - h * g1(x01, x02))
        alpha2 = max(0, alpha2 - h * g2(x01, x02))
        x01 = max(0, x01 + h * (derivative_x1(x01) + alpha1 * der_g1_x1 + alpha2 * der_g2_x1))
        x02 = max(0, x02 + h * (derivative_x2(x02) + alpha1 * der_g1_x2 + alpha2 * der_g2_x2))
    else:
        alpha1 = alpha2 = 0
        x01 = max(0, x01 + h * derivative_x1(x01))
        x02 = max(0, x02 + h * derivative_x2(x02))


def main():
    x_last = math_function(x01, x02)
    new_point(True)
    while True:
        global iterations
        iterations += 1
        if g1(x01, x02) >= 0 and g2(x01, x02) >= 0:
            if abs(math_function(x01, x02) - x_last) < e:
                break
            x_last = math_function(x01, x02)
            new_point(True)
        else:
            new_point(False)


main()
print(f"Ответ: x1 = {x01}\t x2 = {x02}\nКоличество итераций для достижения "
      f"заданной точности: {iterations}")