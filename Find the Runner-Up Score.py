if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr = list(set(arr))
ar = len(arr) # length of array
arr = sorted(arr) # sorted
print(arr[ar-2], end = "")
