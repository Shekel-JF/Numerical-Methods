from math import *

def derivative(f, x, h):
    f_x1 = eval(f)
    x += h
    f_x2 = eval(f) 
    return (f_x2 - f_x1) / h

def derivative2(f, x, h):
    x -= h
    f_x1 = eval(f)
    x = x + 2 * h
    f_x2 = eval(f) 
    return (f_x2 - f_x1) / (2 * h)


def main(args):
    f = input("Podaj funkcję f(x): ")
    x = float(input("Punkt dla pochodnej funkcji f(x): "))
    h = float(input("Rozmiar elementarnego przesunięcia: "))
    
    print("Pierwsze przybliżenie pochodnej funkcji {f} w punkcie {x} dla h = {h} jest równe: {derivative}".format(f = f, x = x, h = h, derivative = derivative(f, x, h)))
    print("Drugie przybliżenie pochodnej funkcji {f} w punkcie {x} dla h = {h} jest równe: {derivative2}".format(f = f, x = x, h = h, derivative2 = derivative2(f, x, h)))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))