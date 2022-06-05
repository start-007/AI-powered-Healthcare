import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,accuracy_score
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from joblib import dump,load
if __name__=="__main__":

  df = pd.read_csv("diseaseDetectData\Training.csv")
  df.describe()
  #print (df.describe())


  df.drop('Unnamed: 133', axis=1, inplace=True)

  x = df.drop('prognosis', axis = 1)
  y = df['prognosis']
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

  tree = DecisionTreeClassifier()

  tree.fit(x_train, y_train)

  pred = tree.predict(x_test)
  acc = tree.score(x_test, y_test)

  print("Acurray on test set: {:.2f}%".format(acc*100))

  fi = pd.DataFrame(tree.feature_importances_*100, x_test.columns, columns=['Importance'])
  fi.sort_values(by='Importance',ascending=False, inplace=True)

  zeros = np.array(fi[fi['Importance'] <= 1.750000].index)

  training_new = df.drop(columns=zeros, axis=1)

  test = pd.read_csv("diseaseDetectData\Training.csv")
  test_new = test.drop(columns=zeros, axis=1)
  test_new=test_new.drop('Unnamed: 133', axis=1)
  test_new.shape[1]
  print (test_new.shape[1])
  print (test_new.columns)
  x_new = training_new.drop('prognosis', axis = 1)
  y_new = training_new.prognosis
  x_train_new, x_test_new, y_train_new, y_test_new = train_test_split(x_new, y_new, test_size=0.3, random_state=42) 
  tree.fit(x_train_new, y_train_new)
  x_test_new.to_csv("diseaseDetectData/newTest.csv")
  dump(tree, 'diseaseDetectModel.joblib')
  print(x_test_new.shape)
  tree = tree.fit(x_train_new, y_train_new)
  tree.predict(x_test_new)
  
  acc_new = tree.score(x_test_new, y_test_new)
  print(acc_new*100)
  #dump(tree, 'diseaseDetectModel.joblib')load('diseaseDetectModel.joblib')
