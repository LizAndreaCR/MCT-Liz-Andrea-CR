while True:
  g1=int(input("Enter your grade"))
  g2=int(input("Enter your second grade"))
  g3=int(input("Enter your third grade"))

promedio=(g1+g2+g3)/3

print(("your average is, ",promedio))

if (promedio<6):
  print("you failed")

if(promedio>=6):
  print("you pass")

if (promedio>=9)
print("you won a medal")