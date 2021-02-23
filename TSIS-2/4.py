gain = [-4,-3,-2,-1,4,3,2]
mx = 0
i = 0
res = 0
for i in range(0, len(gain)):
    res += gain[i]
    if res > mx:
        mx = res
    i += 1
print(mx)