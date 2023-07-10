a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [2, 3, 4]
c = []

i = 0
if b[i] in a:
    s = a.index(b[i])

for j in range(len(b)):
    c.append(a[s])
    s += 1

print(c)

if c == b:
    print("b属于a的连续子列表。")
else:
    print("b不属于a的连续子列表。")

