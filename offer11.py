l = [3,4,5,1,2]
i = 0
j = len(l)-1
while i < j:
    m = (i+j)//2
    if l[m] > l[j]:
        i = m + 1
    elif l[m] < l[j]:
        j = m
    else:
        j -= 1
print(l[i])