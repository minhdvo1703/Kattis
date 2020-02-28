import sys
#input
n,m = map(int,input().split())
if not ((0 <= n <= 1000) and (0 <= m <= 1000) and (n != m)):
  sys.exit()
if (m-n)>1:
  print("Dr. Chaz will have", m-n, "pieces of chicken left over!")
elif (m-n)==1:
  print("Dr. Chaz will have", m-n, "piece of chicken left over!")
elif (n-m)==1:
  print("Dr. Chaz needs", n-m, "more piece of chicken!")
else:
  print("Dr. Chaz needs", n-m, "more pieces of chicken!")
