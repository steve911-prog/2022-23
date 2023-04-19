from math import sqrt
formul_a_s = {
    "pythagoras_theorem":       "a**2 + b**2 = c**2",
    "heron_s_formula":          "sqrt(p*(p-a)*(p-b)*(p-c))", #p = (a+b+c) / 2

    "area_rectangle":           "a*b",
    "area_triangle_h":          "0.5*a*h",
    "area_quadrat":             "a**2",

    "sin":               "a/c",
    "cos":               "b/c",
    "tg":                "a/b",
    "ctg":               "b/a",
}

def user(formulas):
    formula_ = input("Please enter formula or type 'f' to get all commands: ").lower().replace(" ", "")
    # formula_ = formula_.replace(" ", "")
    # print(formula_)
    if formula_ == "exit":
        return 0
    elif formula_ == "f":
        print("FUNCTION              " ,"FORMULA")
        for i in formulas:
            print(i, " " * (22 - (len(i)-1)) , formulas[i])
        print("Please, enter formula, not a name.")
        user(formulas)

    elif formula_ not in formulas:
        print("Sorry, here is no such formula. You can type 'f' to get all commands.")
        user(formulas)

    eval(f"{formula_}()")
    user(formulas)
def get_argument(argument):
    try:
        global arg
        arg = float(input(f"Please enter {argument}: "))
    except:
        print("Hey, that's not a number :)")
        get_argument(argument)

    return arg


def area_rectangle():
    a = get_argument("a")
    b = get_argument("b")

    result = a * b
    print(result, "cm")
    return result

def heron_s_formula():
    a = get_argument("a")
    b = get_argument("b")
    c = get_argument("c")

    p = a+b+c
    result = sqrt(p*(p-a)*(p-b)*(p-c))
    print(result,"cm^2")
    return result

def area_triangle_h():
    a = get_argument("a")
    h = get_argument("h")
    result = 0.5*a*h
    print(result,"cm^2")
    return result

def area_quadrat():
    a = get_argument("a")
    result = a**2
    print(result,"cm^2")
    return result

#
#WRITE CODE RETURNING WHOLE STEP-BY-STEP SOLUTION
#
def pythagoras_theorem():
    arg = input("What argument in Pythagoras theorem would you like to find? (a, b or c):  ")
    list = {
        "a": "sqrt(c**2 - b**2)",
        "b": "sqrt(c**2 - a**2)",
        "c": "sqrt(a**2 + b**2)",
    }

    if arg.lower() == "a":
        b = get_argument("b")
        c = get_argument("c")

        result = eval(list["a"])
        print(f"a = {result}")
        return result
    elif arg.lower() == "b":
        a = get_argument("a")
        c = get_argument("c")

        result = eval(list["b"])
        print(f"b = {result}")
        return result
    elif arg.lower() == "c":
        a = get_argument("a")
        b = get_argument("b")

        result = eval(list["c"])
        print(f"c = {result}")
        return result


# def sincos_conditions(arg, list, sin_or_cos):


def sin():
    #sin alpha = a/c
    # c - hipotenuza, a - long katet, b - short katet alpha - corner opposite to a
    print("If you would like to find sinus of grad, it is not available yet unfortunately.")
    arg = input("Which corner's sinus of ROVNIY triangle would you like to get? \n "
                "(a)lpha - opp. to a , (b)eta - opp. to b : ").lower()
    #arg = arg.lower()

    list = {
        "alpha": "a/c",
        "beta":  "b/c",
    }

    # sincos_conditions(arg_, list_, "sin")
    if arg == "a" or arg == "alpha":
        a = get_argument("a")
        c = get_argument("c")

        result = eval(list["alpha"])
        print(f"sin(alpha) = {result}")
        return result

    elif arg == "b" or arg == "beta":
        b = get_argument("b")
        c = get_argument("c")

        result = eval(list["beta"])
        print(f"sin(beta) = {result}")
        return result
    else:
        print("Sorry, I didn't got you.")
        sin()



def cos():
    #cos alpha = b/c
    # c - hipotenuza, a - long katet, b - short katet alpha - corner opposite to a
    print("If you would like to find cosinus of GRADUS, it is not available yet unfortunately.")
    arg = input("Which corner's cosinus of ROVNIY triangle would you like to get? \n "
                "(a)lpha - opp. to a , (b)eta - opp. to b : ").lower()
    # arg = arg.lower()

    list = {
        "alpha": "b/c",
        "beta": "a/c",
    }
    # sincos_conditions(arg, list, "cos")
    if arg == "a" or arg == "alpha":
        b = get_argument("b")
        c = get_argument("c")

        result = eval(list["alpha"])
        print(f"cos(alpha) = {result}")
        return result

    elif arg == "b" or arg == "beta":
        a = get_argument("a")
        c = get_argument("c")

        result = eval(list["beta"])
        print(f"cos(beta) = {result}")
        return result
    else:
        print("Sorry, I didn't got you.")
        sin()




def ctgtg_conditions(arg, list, ctg_or_tg):
    if arg == "a" or arg == "alpha":
        a = get_argument("a")
        b = get_argument("b")

        result = eval(list["alpha"])
        print(f"{ctg_or_tg}(alpha) = {result}")
        return result
    elif arg == "b" or arg == "beta":
        a = get_argument("a")
        b = get_argument("b")

        result = eval(list["beta"])
        print(f"{ctg_or_tg}(beta) = {result}")
        return result

    else:
        print("Sorry, I didn't got you.")
        if ctg_or_tg.lower() == "tg":
            tg()
        elif ctg_or_tg.lower() == "ctg":
            ctg()
        else:
            print("Invalid argument in ctg_or_tg.")
            user(formul_a_s)

def tg():
    #tg alpha = a/b
    # c - hipotenuza, a - long katet, b - short katet alpha - corner opposite to a
    print("If you would like to find TANGENS of grad, it is not available yet unfortunately.")
    arg = input("Which corner's TANGENS of ROVNIY triangle would you like to get? \n "
                "(a)lpha - opp. to a , (b)eta - opp. to b : ").lower()
    # arg = arg.lower()

    list_ = {
        "alpha": "a/b",
        "beta":  "b/a",
    }

    ctgtg_conditions(arg, list_, "tg")

def ctg():
    #tg alpha = a/b
    # c - hipotenuza, a - long katet, b - short katet alpha - corner opposite to a
    print("If you would like to find COTANGENS of grad, it is not available yet unfortunately.")
    argument = input("Which corner's COTANGENS of ROVNIY triangle would you like to get? \n "
                "(a)lpha - opp. to a , (b)eta - opp. to b : ").lower()
    # arg = arg.lower()

    list = {
        "alpha": "b/a",
        "beta":  "a/b",
    }

    ctgtg_conditions(argument, list, "ctg")

user(formul_a_s)




# def start():
#     a = input("Algebra or geometry? (a/g): ")
#     if a.lower() == "a":
#         user(formula_s)
#     elif a.lower() == "g":
#         user(formul_a_s)
#     else:
#         print("Try again :)")
#         start()
# start()





























