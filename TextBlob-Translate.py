from textblob import TextBlob

toTranslate = "How's it going?"

def translateText(inputText):  
    TText = TextBlob(inputText)    
    TText = TText.translate(to='fr')
    return TText

try: 
    print(translateText(toTranslate))
except:
    print("Couldn't translate:",toTranslate)
