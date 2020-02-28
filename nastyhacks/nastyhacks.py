n = int(input())
for i in range(n):
  num = list(map(int, input().split()))
  if (num[0] < (num[1]-num[2])):
   print("advertise");
  elif(num[0] == (num[1]-num[2])):
    print("does not matter");
  else:
    print("do not advertise");

  
