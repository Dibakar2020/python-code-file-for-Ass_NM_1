Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2**16
65536
2/5
0.4
2//5
0
2/5.0
0.4
'delhi'+'mumbai'
'delhimumbai'
S='mumbai'
'navi'+S
'navimumbai'
S*5
'mumbaimumbaimumbaimumbaimumbai'
S[:0]
''
'Coastal {0} and landlocked {1}.'.format('Mumbai', 'Delhi')
'Coastal Mumbai and landlocked Delhi.'
>>> ('x',)[0]
'x'
>>> ('x','y')[1]
'y'
>>> L = [1,2,3] + [4,5,6]
>>> L
[1, 2, 3, 4, 5, 6]
>>> L[:]
[1, 2, 3, 4, 5, 6]
>>> L[:0]
[]
>>> L[-2]
5
>>> L[-2:]
[5, 6]
>>> ([1,2,3] + [4,5,6])[2:4]
[3, 4]
>>> [L[2], L[3]]
[3, 4]
>>> L.reverse()
>>> L
[6, 5, 4, 3, 2, 1]
>>> L.sort(); L
[1, 2, 3, 4, 5, 6]
>>> L.index(4)
3
>>> {'a':1, 'b':2}['b']
2
>>> D = {'x':1, 'y':2, 'z':3 }
>>> D['w'] = 0
>>> D['x'] + D['w']
1
>>> D[(1,2,3)] = 4
>>> list(D.keys()), list(D.values()), (1,2,3) in D
(['x', 'y', 'z', 'w', (1, 2, 3)], [1, 2, 3, 0, 4], True)
>>> [[]], ["",[],(),{},None]
([[]], ['', [], (), {}, None])
>>> x = [2,3]
>>> x[1] = 4
>>> x = (2,3)
>>> x[1] = 4
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    x[1] = 4
TypeError: 'tuple' object does not support item assignment
