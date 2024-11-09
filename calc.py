import sys 

def add(num1 , num2):
    add = num1 + num2
    return add
def sub(num1 , num2):   
    sub(num1 - num2)
    return sub
def mul(num1 , num2):
    mul = num1 * num2
    return mul
num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    output =(num1 + num2)
    print(output)

if operation == "sub":
    output =(num1 - num2)
    print(output )

## After run the python_file_name argument_1 add argument_2
## example pyhton calc.py 3 add 8
   result = 11.0 because float
