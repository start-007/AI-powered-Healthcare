import nltk
import numpy as np

from nltk.stem.porter import PorterStemmer
stemmer=PorterStemmer()


nltk.download('punkt')
def tokenize(sentence):
  return nltk.word_tokenize(sentence)


def stem(word):
  return stemmer.stem(word.lower())

def bagOfWords(tokensizedSentence,allWords):
  tokensizedSentence=[stem(w) for w in tokensizedSentence]
  bag=np.zeros(len(allWords),dtype=np.float32)
  for idx,w in enumerate(allWords):
    if w in tokensizedSentence:
      bag[idx]=1
  return bag

if __name__=="__main__":
  a="I am teja. I love you."
  b="Are you loving me?"
  btokens=tokenize(b)
  bstem=bagOfWords(btokens,["are","you","love","I","me","?"])
  print(bstem)


