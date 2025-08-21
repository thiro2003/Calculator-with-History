import os
import datetime
while True:
  choise=input("""
        
        ------:CHOOSE THE OPTION:------
        1.Addition
        2.Substration
        3.Division
        4.Multiplication
        5.See History
        6.Exit
    """)
  if(choise=="1"):
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print(f"The sum of {num1} and {num2} is {num1 + num2}")
    with open("history.txt","a") as f:
      f.write(f"Added {num1} and {num2} to get {num1 + num2}  ")
      f.write(f"Operation performed on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
  elif(choise=="2"):      
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print(f"The difference of {num1} and {num2} is {num1 - num2}")  
    with open("history.txt","a") as f:
      f.write(f"Subtracted {num2} from {num1} to get {num1 - num2}\n")
      f.write(f"Operation performed on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
  elif(choise=="3"):      
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    if num2 == 0:
      print("Error: Division by zero is not allowed.")
    else:
      print(f"The division of {num1} and {num2} is {num1 / num2}")
      with open("history.txt","a") as f:
        f.write(f"Divided {num1} by {num2} to get {num1 / num2}\n")
        f.write(f"Operation performed on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
  elif(choise=="4"):      
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print(f"The multiplication of {num1} and {num2} is {num1 * num2}")
    with open("history.txt","a") as f:
      f.write(f"Multiplied {num1} and {num2} to get {num1 * num2}\n")
      f.write(f"Operation performed on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
      
  elif(choise=="5"):
    with open("history.txt","r") as f:
      history=f.read()
      print(f"""
            
            ------:HISTORY--------
            
            {history}
            """)
      
    break 
  elif(choise=="6"):
    print("Exiting the calculator. Goodbye!")
    break 