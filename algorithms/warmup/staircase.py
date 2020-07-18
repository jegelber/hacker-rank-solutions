# Problem: https://www.hackerrank.com/challenges/staircase/problem
# Score: 10/10

def staircase(n):
    for i in range(n):
        temp=''
        for j in range(n):
            if (i+j+1) >= n:
                temp+="#"
            else:
                temp+=" "
        print(temp)
        del temp
