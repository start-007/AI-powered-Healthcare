
import pandas as pd
from joblib import load

def predictDisease(arr):
  tree=load('diseaseDetectModel.joblib')
  
  x=pd.read_csv("diseaseDetectData/newTest.csv")
  a=list(x.columns);
  a.pop(0)

  print(type(arr))
  x_test_new=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
  for j in range(0,len(arr)):
    for i in range(0,len(x_test_new[0])):
      if(a[i]==arr[j]):
        x_test_new[0][i]=1

  x_test_new=pd.DataFrame(x_test_new)
  x_test_new.set_axis(a,axis=1)
  print(x_test_new)
  return str(tree.predict(x_test_new)[0])
  


