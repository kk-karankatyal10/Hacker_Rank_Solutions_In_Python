from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    elementFreq = defaultdict(int)
    freqCount = defaultdict(int)
    ans = []
    for i, j in queries:
        if i == 1:
            if freqCount[elementFreq[j]]:
                freqCount[elementFreq[j]] -= 1
            elementFreq[j] += 1
            freqCount[elementFreq[j]] += 1            
        elif i == 2:
            if elementFreq[j]:
                freqCount[elementFreq[j]] -= 1
                elementFreq[j] -= 1
                freqCount[elementFreq[j]] += 1
        else:
            # operation 3
            if j in freqCount and freqCount[j]:
                ans.append(1)
            else:
                ans.append(0)
    return ans
