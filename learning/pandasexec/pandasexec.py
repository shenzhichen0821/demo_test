# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


a = pd.Series([1,2,3,4,5,6], dtype='int')
print(a)
date = pd.date_range('20180821', periods=6)
print(date.dtype)

#dataframe
b = pd.DataFrame(np.random.randn(6,6), index=date, columns=a)
print(b)

#dataframe dict
c = pd.DataFrame({
    'A':1,
    'B':2,
    'C':np.array([3] * 4, dtype=np.int16)
})
print(c)

# describe, sort
print(b.describe())
print(b.T)
print(b.sort_index(axis=0, ascending=False))
print(b.sort_values(by=3, ascending=False))

#slice
print("\n111111111111")
print(b.loc['20180822'])
print(b.loc['20180822', [2,3]])
print(b.iloc[1:3, 2:4])
print(b.ix[:3,[2,3]])
print(b[b[2]>0.5])

#去除nan的行或列
print("\n2222222222222")
c = b.copy()
c.iloc[0,1] = np.nan
c.iloc[1,2] = np.nan
print(c)
print(c.dropna(axis=1, how='any'))
print(c.fillna(value='sb'))
print(c.isnull())
print(np.any(c.isnull()))

#合并
print("\n3333333333333")
d0 = pd.DataFrame(np.ones((3,4)) * 0, columns=['a','b','c','d'])
d1 = pd.DataFrame(np.ones((3,4)) * 1, columns=['a','b','c','d'])
d2 = pd.DataFrame(np.ones((3,4)) * 2, columns=['a','b','c','d'])
print(pd.concat([d0,d1,d2], ignore_index=True, axis=0))
print(pd.concat([d0,d1,d2], ignore_index=False, axis=1))
print(d0.append([d1,d2], ignore_index=True))

#merge
print("\n444444444444")
e0 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3'],
                   'key1':['K1','K2','K3','K4']})
e1 = pd.DataFrame({'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3'],
                   'key1': ['K2', 'K3', 'K4', 'K5']})
print(pd.merge(e0,e1, on=['key1'], how='outer', indicator="ind_col"))

#plot
print("\n555555555555")
data = pd.Series(np.random.randn(1000))
data = data.cumsum()
data.plot()
plt.show()

print("\n6666666666666")
data_1 = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list('ABCD'))
data_1 = data_1.cumsum()

ax = data_1.plot.scatter(x='A', y='B', color='DarkBlue', label='Class1')
data_1.plot.scatter(x='A', y='C', color='DarkGreen', label='Class2', ax=ax)
plt.show()
