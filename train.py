import json
from pickletools import optimize
from sklearn.model_selection import learning_curve
import torch
import torch.nn as nn
from torch.utils.data import Dataset,DataLoader
from model import NeuralNet

from tqdm import trange
from nltkFuncs import tokenize,bagOfWords,stem
import numpy as np

with open("intents.json","r") as f:
  intents=json.load(f)

allWords=[]
tags=[]
xy=[]

for intent in intents["intents"]:
  tag=intent["tag"]
  tags.append(tag)
  for pattern in intent['patterns']:
    w=tokenize(pattern)
    allWords.extend(w)
    xy.append((w,tag))

ignoreWords=['?',".","!",","]

allWords=[stem(w) for w in allWords if w not in ignoreWords]
allWords=sorted(set(allWords))
tags=sorted(set(tags))

x_train=[]
y_train=[]

for (pattern_sentence,tag) in xy:
  bag=bagOfWords(pattern_sentence,allWords)
  x_train.append(bag)
  label=tags.index(tag)
  y_train.append(label)

x_train=np.array(x_train)
y_train=np.array(y_train,dtype=np.int64)

class ChatDataset(Dataset):
  def __init__(self):
    self.n_samples=len(x_train)
    self.x_data=x_train
    self.y_data=y_train
  
  def __getitem__(self,idx):
    return self.x_data[idx],self.y_data[idx]
  
  def __len__(self):
    return self.n_samples

#hyper parameters
batch_size=25
hidden_size=50
output_size=len(tags)
input_size=len(x_train[0])
learning_rate=0.001
num_epochs=1000
print(input_size,len(allWords))
print(output_size)

  
dataset=ChatDataset()
train_loader=DataLoader(dataset=dataset,batch_size=batch_size,shuffle=True)


device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
model=NeuralNet(input_size,hidden_size,output_size).to(device)

criterian=nn.CrossEntropyLoss()
optimizer=torch.optim.Adam(model.parameters(),lr=learning_rate)

for epoch in range(num_epochs):
  for (words,labels) in train_loader:
    words=words.to(device)
    labels=labels.to(device)
    #forward
    outputs=model(words)
    loss=criterian(outputs,labels)
    #backward and optimizer
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
  
  if(epoch+1)%100 ==0:
    print(f"epoch {epoch+1}/{num_epochs},loss={loss.item():.4f}")

print(f"final loss, {epoch+1}/{num_epochs},loss={loss.item():.4f}")

data={
  "data":model.state_dict(),
  "input_size":input_size,
  "output_size":output_size,
  "hidden_size":hidden_size,
  "tags":tags,
  "allWords":allWords
  
}

torch.save(data,"data.pth")
print(f"File saved")




  
