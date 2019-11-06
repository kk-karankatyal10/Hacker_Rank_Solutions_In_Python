inp1 = int(input())
inp2 = int(input())
a = divmod(inp1, inp2)

for i in range(len(a)):
    print(a[i])
print(a, end= "")
