def isnumber(s):
    try:
        n = float(s)
        return True
    except ValueError:
        return False

while True:
  inpt=input('>\n')
  inpuut=inpt.split()
  stick=[]
  breaker=False
  for i in range(len(inpuut)):
    if inpuut[i]=="+":
      stick.append(stick.pop()+stick.pop())
    elif inpuut[i]=="-":
      stick.append(-stick.pop()+(stick.pop()))
    elif inpuut[i]=="/":
      stick.append(1/stick.pop()*stick.pop())
    elif inpuut[i]=="*":
      stick.append(stick.pop()*stick.pop())
    elif inpuut[i]=="^":
      stick.append(stick.pop()**stick.pop())
    elif inpuut[i]=="n":
      stick.append(-1*stick.pop())
    elif inpuut[i]=="i":
      stick.append(1/stick.pop())
    elif inpuut[i]=="sqrt":
      stick.append(stick.pop()**0.5)
    elif inpuut[i]=="p":
      print(stick)
    elif inpuut[i]=="x":
      breaker=True
      break
    elif isnumber(inpuut[i]):
      stick.append(float(inpuut[i]))
    else:
      print("that input contained the invalid integer or operation {}".format(inpuut[i]))
  if breaker:
    break
  print(stick)