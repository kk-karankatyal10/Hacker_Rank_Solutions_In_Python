def print_rangoli(size):
    for i in range(size):
        s = "-".join(chr(ord('a')+size-j-1) for j in range(i+1))
        print((s+s[::-1][1:]).center(size*4-3, '-'))

    for i in range(size-1):
        s = "-".join(chr(ord('a')+size-j-1) for j in range(size-i-1))
        print((s+s[::-1][1:]).center(size*4-3, '-'))
