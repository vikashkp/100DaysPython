def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  num1 = float(input("what is the first number ?:"))
  
  isContinue = True
  while isContinue:
    for oprn in operations:
      print(oprn)
    opr = input("pick a operation type?:")
    num2 = float(input("what is the second number ?:"))
    result = operations[opr](num1,num2)
    
    print(f"{num1} {opr} {num2} = {result}")
    if input(f"TYpe 'y' to continue with answer {result}, type n to exit.:") == "y":
      num1=result
    else:
      isContinue = False
      calculator()

calculator()