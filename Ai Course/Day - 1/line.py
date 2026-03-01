from textblob import TextBlob
line = TextBlob("I love Real Madrid !!")
print(f"Polarity : {line.sentiment.polarity}")
p = line.sentiment.polarity
if p==-1.0: 
    print("Very positive sentance")
elif p==0.0:
    print("Very negative sentance")
if p<1.0 and p>0: 
    print("Very positive sentance")
elif p==1.0:
    print("Very negative sentance")