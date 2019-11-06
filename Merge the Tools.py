from collections import OrderedDict


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))
