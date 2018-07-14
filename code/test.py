"""mapping"""
import os    ##for directory
# set the directory
os.chdir('/Users/luho/Google Drive/myPyModule')
sys.path.append(r"/Users/luho/Google Drive/myPyModule/code")


w = [1,2,3,4,5,6]
v =['z','a','b','a','b','e']
testData = ['a','b','g']

import hongpy
import pandas as pd
"""mapping"""
tt = hongpy.singleMapping(w, v, testData, dataframe=False)
mm = hongpy.multiMapping(w, v, testData, dataframe=False)


"""split and combine"""
s1 = ['a&b','c']
s2 = ['r1','r2']

ss = pd.DataFrame({'ss1':s1, 'ss2':s2})
nn = hongpy.splitAndCombine(ss['ss1'], ss['ss2'], sep0="&")

"""autoUpdate"""
df1 = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                    'B' : ['A', 'B', 'C'] * 4,
                    'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2}
                   )

df2 = df1.iloc[[1,2]]
df2['C'] = ['good','good']


df1['C'] = hongpy.AutoUpdate(df2['C'], df2['A'], df1['C'], df1['A'])


##import the module from the code file

