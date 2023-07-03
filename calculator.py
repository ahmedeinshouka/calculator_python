logo = f"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations={"+":add,"-":subtract,"*":multiply,"/":divide}
def calculator():
 line="---------------------------------------------------------------------------------------------------------------------\n"
 print(line)
 num1=float(input("What's the first number?: "))
 num2=float(input("What's the secound number?: "))
 
 print(line)
 for operator in operations:

    print(operator+"\n")
 print(line)
 operation_symbol=input("Pick an operation from the line above: ")
 calculation_function=operations[operation_symbol]
 first_answer=calculation_function(num1,num2)
 print(line)
 print(f"{num1} {operation_symbol} {num2} = {first_answer}")
 print(line)
 continue_calculation=input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit and 'e' to exit the program .: ")
 print(line)
 if continue_calculation=="n":
     calculator()
 elif continue_calculation=="y":
  while continue_calculation=="y":
    print(line)
    print(line)
    for operator in operations:

     print(operator+"\n")
    operation_symbol=input("Pick another operation: ")
    print(line)
    num3=float(input("What's the next number?: "))
    print(line)
    calculation_function=operations[operation_symbol]
    secound_answer=calculation_function(first_answer,num3)
    print(line)
    print(f"{first_answer} {operation_symbol} {num3} = {secound_answer}")
    first_answer=secound_answer
    print(line)
    continue_calculation=input(f"Type 'y' to continue calculating with {secound_answer}, or type 'n' to exit and 'e' to exit the program .: ")
    if continue_calculation=="n":
        calculator()
    elif continue_calculation=="e":
        break
 elif continue_calculation=="e":
      pass
 else:
     print("please check your enter again")
calculator()