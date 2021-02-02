# a = ('aaa','bbb','ccc','ddd')

# if a[1] in ['qqq','bbb','zzz']:
#     print("yes")

# if a[1] in ['qqq','ddd','zzz']:
#     print("yes")
# else:
#     print("no")

# print(a)
# a = (a[0], 'eee', a[2], a[3])

# print(a)

class AAA():
    def __init__(self, x):
        super(AAA, self).__init__()
        self.x = x


    def __iter__(self):
        for i in self.x:
            yield i

    def __call__(self):
        return self.__iter__() 

aaa = AAA([1,2,3,4,5,6,7,8,9,0])

for i, a in enumerate(aaa):
    print(i, '   ', a ) 

for i, a in enumerate(aaa()):
    print(i, '   ', a)