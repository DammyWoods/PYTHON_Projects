#This program test the use of defensive programming to address unexpected events and user inputs
print("This simple calculator helps to calculate two numbers using your preferred operator\n")
num1 = 0
num2 = 0
choice = 0
file = None

#user needs to perform at least 1 calculation first before option 2 to read from file can be chosen in subsequent trials
print("Perform a calculation on your first trial and then choose to either perform a calculation again on your 2nd trial \nor simply read your previous equations from a file\n")

while True:
    try:
        choice = int(input("Enter 1 to perform a new calculation or Enter 2 to read equations from a file: "))
        if (choice == 1):
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            operators = input("Enter the operators (+, *, /, -, **): ")

            if (operators == '+') :
                print(f"{num1} + {num2} = {num1 + num2}")
                with open('equations.txt', 'a') as file:
                    file.write(f"{num1} + {num2} = {num1 + num2}")
                    file.write("\n")
            elif (operators == '*'):
                print(f"{num1} * {num2} = {num1 * num2}")
                with open('equations.txt', 'a') as file:
                    file.write(f"{num1} * {num2} = {num1 * num2}")
                    file.write("\n")
            elif (operators == '/') :
                try:
                    print(f"{num1} / {num2} = {num1 / num2}")
                    with open('equations.txt', 'a') as file:
                        file.write(f"{num1} / {num2} = {num1 / num2}")
                        file.write("\n")
                except ZeroDivisionError:
                    print("This number cannot be divided by zero")
            elif (operators == '-') :
                print(f"{num1} - {num2} = {num1 - num2}")
                with open('equations.txt', 'a') as file:
                    file.write(f"{num1} - {num2} = {num1 - num2}")
                    file.write("\n")
            elif (operators == '**') :
                print(f"{num1} ** {num2} = {num1 ** num2}")
                with open('equations.txt', 'a') as file:
                    file.write(f"{num1} ** {num2} = {num1 ** num2}")
                    file.write("\n")
            else:
                print("You have not entered the correct operator. Please choose from the listed operators")
                continue

        elif (choice == 2):
            while True:
                file_name = input("Enter filename as 'equations.txt': ")
                try:
                    content = ""
                    with open (file_name, 'r+' ) as file: 
                        for line in file:
                            content += line
                        print(content)
                        break

                except FileNotFoundError:
                    message = "Sorry this file " + file_name + "does not exist"
                    print(message)
                    continue
            break        
        else:
            print("You have not entered a valid number, Enter '1' or '2'... \n")
            continue

    except ValueError:
        print("You have not entered a valid number, Please check your entry again")
        continue

    continue