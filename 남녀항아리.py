import csv

f=open('gender.csv')
data= csv.reader(f)

# header= next(data)
# print(header)

m=[]
f=[]

for row in  data :
  if '신도림' in row[0]:
    for i in range(0,101):
      m.append(int(row[i+3]))
      f.append(-int(row[-(i+1)]))
f.reverse()

# print(m)
# print(f)

import matplotlib.pyplot as plt
plt.rc("font",family= 'Gulim')
plt.rcParams['axes.unicode_minus']= False
plt.title('신도림 지역의 남녀 성별인구 분포')
plt.barh(range(101),m, label='남성')
plt.barh(range(101),f, label  ='여성')
plt.legend(title='성별')
plt.show()