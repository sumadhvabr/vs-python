l=[1,2,3,4,5]
l_iter=iter(l)
print(l_iter)
print(next(l_iter))

print(l_iter.__next__())
print(l_iter.__next__())
print(l_iter.__next__())
print(l_iter.__next__())
# print(l_iter.__next__())
# print(l_iter.__next__())
l_iter=iter(l)
print(next(l_iter))



str='python pr'
s_iter=iter(str)
type(str),type(s_iter)
print(type(str),type(s_iter))


t=(1,2,3,4,5)
t_iter=iter(t)
type(t),type(t_iter)
print(type(t),type(t_iter))


d={1:2,3:4,5:6,7:8}
d_iter=iter(d)

print(type(d),type(d_iter))






import itertools as it
seq=it.cycle(['A','B','C','D','E'])

for _ in range(5):
    print(next(seq))


for _ in range(5):
    print(next(seq))    