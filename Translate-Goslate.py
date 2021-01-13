import goslate

toTranslate = "How's it going?"

def translateText(inputText):
    gs = goslate.Goslate()
    TText = gs.translate(inputText, 'fr')
    return TText

print(translateText(toTranslate))
