import math

def rectangle():
    try:
        l = int(input("Enter the Length of a Rectangle :"))
        w = int(input("Enter the Width of a Rectangle :"))
        r_result = l*w
        print("=======================================")
        print("The Area of a Rectangle is : ", r_result)
        print("=======================================")
    except ValueError:
        print("INVALID INPUT!!, USE NUMBER ONLY")

def triangle():
    try:
        a = int(input("Enter the width of a Triangle :"))
        T = int(input("Enter the height of a Triangle: "))
        t_result = (a * T)/2
        print("=======================================")
        print("The Area of a Triangle is : ", t_result)
        print("=======================================")
    except ValueError:
        print("INVALID INPUT!!, USE NUMBER ONLY")

def circle():
    try:
        r = int(input("Enter the radius of a circle :"))
        c_result = math.pi * (r**2)
        print("=======================================")
        print("The Area of a Circle is : ", round(c_result , 2))
        print("=======================================")
    except ValueError:
        print("INVALID INPUT!!, USE NUMBER ONLY")

def trapezoidal():
    try:
        p = int(input("Enter the first length of a trapezoidal :"))
        s = int(input("Enter the second length of a trapezoidal :"))
        h = int(input("Enter the height of a trapezoidal :"))
        trap_result = ((p + s)*h)/2
        print("=======================================")
        print("The Area of a Trapezoidal is : ", trap_result)
        print("=======================================")
    except ValueError:
        print("INVALID INPUT!!, USE NUMBER ONLY!")
        

def show_menu():
    print("\n")
    print("This is a Simple Program to Calculate an Area of 2D Field")
    print("=========================================================")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Trapezoidal")
    print("0. Keluar")

    menu = input("Please Choose the Menu: ")
    print("\n")

    if menu == "1":
        rectangle()
    elif menu == "2":
        triangle()
    elif menu == "3":
        circle()
    elif menu == "4":
        trapezoidal()
    elif menu == "0":
        exit()
    else:
        print("WRONG MENU!")

if __name__ == "__main__":
    while (True):
        show_menu()