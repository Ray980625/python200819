
maxscores = 0
minscores = 100
total = 0
names = []
scores = []

maxindex = 0
minindex = 0

for i in range(5):
    n = int(input('成績:'))
    scores.append(n)
    
    name = input('名字:')
    names.append(name)
    
    if n > maxscores:
        maxscores = n
        maxindex = i
    if n < minscores:
        minscores = n
        minindex = i
    total = total + n
    
s = total/len(scores)
print('總分:',total)
print('平均:',s)
print('最高分:',maxscores)
print('最低分:',minscores)
print(names[maxindex])
print(names[minindex])