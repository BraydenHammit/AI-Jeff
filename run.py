from math import sqrt, floor

def run(entry,ans):
    inquiry = entry.get()
    if inquiry == '': inquiry = ' '

    adjectives = ['green','ugly','handsome','pretty','juicy','sentient','purple','fat','skinny','orange','red','demonic','high','low','slippery','rough','vibrant','large','massive','Scottish','disgusting','vile','godlike','good','bad','evil','pricey',
                  'smart','dumb','eligant','stupid','idiotic','intelligent','official','artificial','natural','German','dead','alive','goth','emo','egotistical','unrealistic','tasty','feminine','masculine','girly','manly','special','lonely','killer',
                  'intruiging','zesty','illegal','ethical','unethical','legal','religous','non-religous','colorful','Aetheist','British','French','English','American','cheesy','wet','nasty','sticky','clean','rich','fancy','shiny','unintelligent',
                  'confused']
    nouns = ['cheese','basketball','football','McDonalds','cat','computer','AI','robot','dog','fox','snake','emu','table','emo','eclipse','famine','disease','thing','idea','BitCoin','doohickey','gadget','potato','dollar bill','Barbie doll','bread',
             'penny','t-shirt','dinosaurs','turtle','killer','human','fish','feline','Aetheist','rat']
    the_nouns = ['the cat','the government','the cheeseburger','the law','the future','the present','the past','the president','the moon landing','the King','the Lord','the devil','your mother']
    plur_nouns = ['cats','rats','snakes','foxes','fish','tables','people','citizens','ideas','laws','taxes','potatoes','robots','things','gadgets','Aetheists','humans','families']

    words = {
        'self': ['I'],
        'people': ['Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff',     'Obama','Heisenberg','Rick','Morty','Harry Potter','some random guy','McDonalds','Sheldon1436','JosephGotG','satan','God','GTF','Cpj2020',
                   'Voldemort','He-Who-Must-Not-Be-Named','You-Know-Who','Kermit the Frog','Tony Stark','Microsoft','Jeff the Killer','Technoblade','KTaylor Gaming'],
        'verb': ['hate','love','eat','murder','own','ignore','sell','torture'],
        'verbS': ['hates','loves','eats','murders','owns','ignores','admires','cooks','sells','tortures'],
        'past verb': ['hated','loved','ate','murdered','owned','ignored','sold','tortured','built','ignored'],
        'locations': ['China','the United States of America','Texas','Germany','France','the Netherlands','the Nether','Hell','Heaven','Helheim','Limbo','the United Kingdom','Scotland','Australia','the depths','the shadow realm','Area 51','the End','the Overworld',
                      'the Sift','the Roblox Headquarters','Mother Russia','Georgia'],
        'going to': ['going to'],
        'am': ['am'],
        'are': ['are'],
        'is': ['is'],
        'userS': ['you'],
        'from': ['from'],
        'a': ['a'],
        'user': ['you'],
        'noun': nouns,
        'the noun': the_nouns,
        'the noun is': the_nouns,
        'plur noun': plur_nouns,
        'plur noun are': plur_nouns,
        'adjective': adjectives,
        'adjectiveQ': adjectives,
        'AMadjective': adjectives,
        'punct': ['.','.','.','.','.','.','.','.','.','.','.','.',    '...','!','?'],
        'com': [','],
        'conjunction': ['for','and','yet','so','because','or','or maybe']
    }
    nxt = {
        'start': ['self','people','userS','plur noun are','the noun is'],
        'self': ['verb','am','past verb'],
        'people': ['verbS','is','past verb'],
        'am': ['AMadjective','a','the noun','from','going to'],
        'is': ['AMadjective','a','the noun','from','going to'],
        'verb': ['plur noun','noun','adjective','the noun'],
        'verbS': ['plur noun','user','the noun'],
        'past verb': ['plur noun','user','the noun','a'],
        'user': ['punct','punct','punct','com'],
        'userS': ['are'],
        'are': ['AMadjective','a','the noun','from','going to'],
        'noun': ['punct','punct','punct','com'],
        'the noun': ['punct','punct','punct','com'],
        'the noun is': ['is','past verb'],
        'plur noun are': ['are','past verb','verb'],
        'plur noun': ['punct','punct','punct','com'],
        'adjective': ['plur noun'],
        'from': ['locations'],
        'going to': ['locations'],
        'locations': ['punct','punct','punct','com'],
        'AMadjective': ['punct','punct','punct','com'],
        'com': ['conjunction'],
        'conjunction': ['self','people','userS','plur noun are','the noun is'],
        'adjectiveQ': ['noun'],
        'punct': ['self','people','userS','plur noun are','the noun is'],
        'a': ['adjectiveQ']
    }

    def alphabet(value):
        alph = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8,
            'i': 9,
            'j': 10,
            'k': 11,
            'l': 12,
            'm': 13,
            'n': 14,
            'o': 15,
            'p': 16,
            'q': 17,
            'r': 18,
            's': 19,
            't': 20,
            'u': 21,
            'v': 22,
            'w': 23,
            'x': 24,
            'y': 25,
            'z': 26
        }
        try:
            val = alph[value.lower()]
            return val
        except:
            try:
                val = int(value)
                return val
            except:
                return 1

    def iterate(num):
        for each in range(num):
            for key in nxt:
                nxt[key] = nxt[key][1:] + nxt[key][:1]
            for key in words:
                words[key] = words[key][1:] + words[key][:1]


    word_id = ['start','start','start']
    answer = ''
    loop = 2
    for each in range(floor(sqrt(len(inquiry))*17)):
        xqc = word_id[loop]
        t = nxt[word_id[loop]]
        failed = True
        iteration = loop // 2
        tt = t[(loop * 13 + iteration * 17 + alphabet(inquiry[(loop + iteration) % len(inquiry)]) * 7) % len(t)]
        char = inquiry[(loop - 2) % len(inquiry)]
        choices = words[tt]
        word = choices[(alphabet(char) - 1) % len(choices)]
        if xqc == 'a' and word[0].lower() in ('i','o','u','a','e'):
            answer += 'n'
        if tt not in ('punct','com'):
            answer += ' '
        if xqc in ('start','punct'):
            answer += word[0].upper() + word[1:] 
        else:
            answer += word
        word_id.append(tt)
        loop += 1
        iterate((round(loop % 5 // len(inquiry)))+1)

    if word_id[loop] == 'punct': finished = True
    else: finished = False
    while finished == False:
        xqc = word_id[loop]
        t = nxt[word_id[loop]]
        failed = True
        iteration = loop // 2
        tt = t[(loop * 13 + iteration * 17 + alphabet(inquiry[(loop + iteration) % len(inquiry)]) * 5) % len(t)]
        char = inquiry[(loop - 2) % len(inquiry)]
        choices = words[tt]
        word = choices[(alphabet(char) - 1) % len(choices)]
        if xqc == 'a' and word[0].lower() in ('i','o','u','a','e'):
            answer += 'n'
        if tt not in ('punct','com'):
            answer += ' '
        if xqc in ('start','punct'):
            answer += word[0].upper() + word[1:]
        else:
            answer += word
        word_id.append(tt)
        loop += 1
        iterate((round(loop % 5 // len(inquiry)))+1)

        if tt == 'punct': finished = True

    return answer