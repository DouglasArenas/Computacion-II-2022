import sys
import getopt
(opt, arg) = getopt.getopt(sys.argv[1:], 'o:n:m:')

for (op, ar) in opt:
    if op in '-o':
        operator = ar
    elif op == '-n':
        num1 = ar
    elif op == '-m':
        num2 = ar
    else:
        print("Invalid option")

if operator == "+":
    print(f"{num1} + {num2} = ", int(num1) + int(num2))

elif operator == "-":
    print(f"{num1} {operator} {num2} = ", int(num1) - int(num2))

elif operator == "*":
    print(f"{num1} {operator} {num2} = ", int(num1) * int(num2))

elif operator == "/":
    if num2 != 0:
        print(f"{num1} {operator} {num2} = ", int(num1) / int(num2))
    else:
        print("Syntax error")
else:
    print("Invalid option")



