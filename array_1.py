s = 'oawuiey5ttrt134927856*&^%$'

a = 'sf'
b = 'se'
print(a + b)

num = ''
ss = ''
sp = ''
for i in s:
    if i >= 'a' and i<= 'z':
        ss += i
    elif i >= '0' and i<= '9':
        num += i
    else:
        sp += i
a = [ss , num , sp]
for j in a:
    print(j)








