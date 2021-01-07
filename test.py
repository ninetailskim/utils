a = ('aaa','bbb','ccc','ddd')

if a[1] in ['qqq','bbb','zzz']:
    print("yes")

if a[1] in ['qqq','ddd','zzz']:
    print("yes")
else:
    print("no")

print(a)
a = (a[0], 'eee', a[2], a[3])

print(a)