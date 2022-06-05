
import random
import json
import torch
from nltkFuncs import tokenize,bagOfWords,stem
from model import NeuralNet

with open("intents.json","r") as f:
  intents=json.load(f)

device=torch.device("cuda" if torch.cuda.is_available() else "cpu")

FILE="data.pth"

data=torch.load(FILE)
input_size=data["input_size"]
hidden_size=data["hidden_size"]
output_size=data["output_size"]
tags=data["tags"]
allWords=data["allWords"]
model_state=data["data"]
model=NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

botName="Me"
print(f"{botName} Hello YOU type \'quit\' to exit ")
def response(sentence):
  sentence=tokenize(sentence)
  bag=bagOfWords(sentence,allWords)
  bag=bag.reshape(1,bag.shape[0])
  bag=torch.from_numpy(bag)
  output=model(bag)
  _,predicted=torch.max(output,dim=1)
  tag=tags[predicted.item()]
  prob=torch.softmax(output,dim=1)
  prob_predicted=prob[0][predicted.item()]
  flag=1
  if(prob_predicted.item()>0.75):
    for intent in intents["intents"]:
      if(tag==intent["tag"]):
        return random.choice(intent['responses'])
        flag=0
  else:
    return "I dont understand"


if __name__=="__main__":
  print(response("who are you?"))
  
   
