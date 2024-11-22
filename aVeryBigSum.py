# aVeryBigSum.py
def aVeryBigSum(ar):
    # Write your code here
    arr = list(map(int, ar))
    result = sum(arr)
    return result


n = int(input())
ar = input().split()
print(aVeryBigSum(ar))
