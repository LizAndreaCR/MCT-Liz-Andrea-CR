suma=int(input("write a number:"))
w=int(input("write the number pf repetitions of the number:"))
while True:
  for x in range(w):
    suma=suma+3
    print(suma)

  x=input("Quieres que siga? ")
  if (x=="si"):
    continue
  else:
    break