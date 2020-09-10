# Problem: https://www.hackerrank.com/challenges/bon-appetit/problem
# Score: 10/10

def bonAppetit(bill, k, b):
    total = sum(bill)
    actual = int((total - bill[k])/2)
    if b == actual:
        print("Bon Appetit")
    else:
        print(b - actual)
