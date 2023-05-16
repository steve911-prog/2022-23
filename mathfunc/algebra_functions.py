formula_s = {
    "(a-b)**2" : "a**2 - 2*a*b + b**2",
    "(a+b)**2":"a**2 + 2*a*b + b**2",
    "a**2+b**2": "(a-b)**2 +2*a*b",
    "(a+b)**2+(a-b)**2": "2*(a**2 + b**2)",
    "(a+b)**3": "a**3 + 3*a**2*b + 3*a*b**2 + b**3",
    "a**3-b**3": "(a-b)*(a**2 + a*b + b**2)",
    "a**4-b**4": "(a-b)*(a+b)*(a**2 + b**2)",
    "(a+b+c)**2": "a**2 + b**2 + c**2 + 2*a*b + 2*b*c +2*c*a",
}

def get_argument(argument):
    try:
        global arg
        arg = float(input(f"Please enter {argument}: "))
    except:
        print("Hey, that's not a number :)")
        get_argument(argument)

    return arg
def count(formulas, formula , a=0, b=0,  c=0, h=0):
    result = eval(formulas[formula])
    print(result)

    user(formulas)
    #return result
    #Google about using EVAL command


def user(formulas):
    formula_ = input("Please enter formula or type 'f' to get all commands: ").lower().replace(" ", "")
    formula_ = formula_.replace(" ", "")

    if formula_ == "exit":
        return 0
    elif formula_ == "f":
        for i in formulas:
            print(i)

        user(formulas)
    elif formula_ not in formulas:
        print("Sorry, here is no such formula. You can type 'f' to get all commands.")
        user(formulas)

    a_ = get_argument("a")
    b_ = get_argument("b")


    if formula_ == "(a + b + c)**2":
        c_ = get_argument("c")
        count(formulas, formula_, a_, b_, c_)
    else:
        count(formulas, formula_, a_, b_)



user(formula_s)





#(a+b)**2 = a**2 + 2*a*b + b**2
#(a-b)**2 = a**2 - 2*a*b + b**2
####### (a-b)**2 = (a+b)**2 - 4*a*b
#a**2 + b**2 = (a-b)**2 + 2*a*b
#(a+b)**2 + (a-b)**2 = 2*(a**2 + b**2)
#(a+b)**3 = a**3 + 3a**2*b + 3*a*b**2 + b**3
#a**3 - b**3 = (a-b)(a**2 + ab + b**2)
#a**4 - b**4 = (a-b)(a+b)(a**2 + b**2)
#(a + b + c)**2 = a**2 + b**2 + c**2 + 2ab + 2bc +2ca


























