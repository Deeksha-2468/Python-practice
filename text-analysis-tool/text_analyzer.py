#Text Analysis Tool
import re
from collections import Counter 
import json
def analyze_text(paragraph):
  #Counts the sentences
  sentences=re.split(r'[.!?]+',paragraph)
  num_sentences=len([s for s in sentences if s.strip()])
  #Extract words
  words=re.findall(r'\b[a-zA-Z]+\b',paragraph.lower())
  #Frequency of words
  word_freq=Counter(words)
  #Longest word in the paragraph 
  longest_word:max(words,key=len) if words else""
  longest_length:len(longest_word)
  total_words:len(words)
  unique_words:len(word_freq)
  return {
        'num_sentences':num_sentences,
        'total_words':total_words,
        'unique_words':unique_words,
        'longest_word':longest_word,
        'longest_length':longest_length,
        'top_words':dict(word_freq.most_common(10))
  }
#Usage of an example
para="The small cat loves to nap in the warm sun. It sleeps all day, then wakes up to play. A happy cat is a wonderful thing, and this small pet is very happy."
result=analyze_text(para)
print(json.dumps(result,indent=4))
