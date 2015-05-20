"""
    Ludocrist attempt at a POMS test, taking the least effort to do something
    not half that complicated...

    Soyunkope 2015
"""
import random, datetime, sys


tension = zip(["tense", "shaky", "on edge", "panicky", "relaxed", "uneasy", "restless", "nervous", "anxious"],
                           [1, 1, 1, 1,-1, 1, 1, 1, 1])
depression = zip(["unhappy", "sorry for things done", "sad", "blue", "hopeless", "unworthy", "discouraged", "lonely", "miserable", "gloomy", "desperate", "helpless",        "worthless", "terrified", "guilty"],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
anger = zip(["anger", "peeved", "grouchy", "spiteful", "annoyed", "resentful", "bitter", "ready to fight", "rebellious", "deceived", "furious", "bad tempered"],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
vigour = zip(["lively", "active", "energetic", "cheerful", "alert", "fell of pep", "carefree", "vigorous"],
                  [1, 1, 1, 1, 1, 1, 1, 1])
fatigue = zip(["worn out", "listless", "fatigued", "exhausted", "sluggish", "weary", "bushed"],
                   [1, 1, 1, 1, 1, 1, 1])
confusion = zip(["confused", "unable to concentrate", "muddled", "bewildered", "efficient", "forgetful", "uncertain about things"],
                     [1, 1, 1, 1, -1, 1, 1])
ignore = zip(["friendly", "clear-headed", "considerate", "sympathetic", "helpful", "good-natured", "trusting"],
        [1, 1, 1, 1, 1, 1, 1])
tenD = dict(tension)
depD = dict(depression)     
angD = dict(anger)
vigD = dict(vigour)
fatD = dict(fatigue)
conD = dict(confusion)
ignD = dict(ignore)

if __name__ == '__main__':
    random.seed()
    now = datetime.datetime.now()
    fname = str(sys.argv[1])
    affects = [tension, depression, anger, vigour, fatigue, confusion, ignore]
    names = ["tension", "depression", "anger", "vigour", "fatigue", "confusion", "ignore"]
    infor = enumerate(affects)
    quest = []
    for nam in affects:
        quest += [nam[x][0] for x in range(len(nam))]
    random.shuffle(quest)
    res = [] # {i: raw_input(i+': ') for i in quest}
    for q in quest:
        try:
            res += [raw_input(q+': ')]
            while int(res[-1]) not in [1,2,3,4]:
                res[-1] = raw_input(q+': (only values between 1-4) ')
        except ValueError:
            res[-1] = raw_input(q+': (only values between 1-4) ')
    resp=dict(zip(quest,res))
    sols=[tenD, depD, angD, vigD, fatD, conD, ignD]
    report=[]
    for x,mod in enumerate(sols):
        p=0
        for r in mod.keys():
            p = p + int(resp[r])*int(mod[r])
        report += zip([names[x]], [p])
    with open(fname, "a+") as f:
        valA = [now.strftime("%Y-%m-%d_%H:%M:%S")+', '+str(dict(report))[1:-1]]
        valB = [now.strftime("%Y-%m-%d_%H:%M:%S")+', '+str(resp)[1:-1]]
        f.write(str(valA)[2:-2])
        f.write("\n")
        f.write(str(valB)[2:-2])
        f.write("\n")

