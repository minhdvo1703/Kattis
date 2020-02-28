#input number of cases
n = int(input())
if n >=1 and n <= 20:
    for i in range(n):
        num = int(input())
        if num >=-10 and num <=10:
            if (num % 2) == 0:
                print(num, "is even");
            else:
                print(num, "is odd");