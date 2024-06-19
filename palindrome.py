arr = [1,2,3,4,5,6,7,6,6,5,3,4,6,]

new = []
ret = []

for i in arr:
    if i in new:
        ret.append(i)
    else:
        new.append(i)
if not ret:
    print(-1)
else:
    print(ret)
