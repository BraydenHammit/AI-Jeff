from math import sqrt, floor

def run(entry):
    inquiry = entry.get()
    if inquiry == '': inquiry = ' '

    adjectives = ['green','ugly','handsome','pretty','juicy','sentient','purple','fat','skinny','orange','red','demonic','high','low','slippery','rough','vibrant','large','massive','Scottish','disgusting','vile','godlike','good','bad','evil','pricey',
                  'smart','dumb','eligant','stupid','idiotic','intelligent','official','artificial','natural','German','dead','alive','goth','emo','egotistical','unrealistic','tasty','feminine','masculine','girly','manly','special','lonely','killer',
                  'intruiging','zesty','illegal','ethical','unethical','legal','religous','non-religous','colorful','Aetheist','British','French','English','American','cheesy','wet','nasty','sticky','clean','rich','fancy','shiny','unintelligent', 'sour'
                  'confused','slow','fast','sorry','gold','blue','yellow','pink','grey','brown','rainbow','clear','supportive','helpful','honest','dishonest','trustworthy','untrustworthy','loyal','universal','spiteful','helpless','bald']
    nouns = ['cheese','basketball','football','McDonalds','cat','computer','AI','robot','dog','fox','snake','emu','table','emo','eclipse','famine','disease','thing','idea','BitCoin','doohickey','gadget','potato','dollar bill','Barbie doll','bread',
             'penny','t-shirt','dinosaur','turtle','killer','human','fish','feline','Aetheist','rat','pumpkin','quarter','nickel','egg','tariff','chicken','bee','salad']
    the_nouns = ['the cat','the government','the cheeseburger','the law','the future','the present','the past','the president','the moon landing','the King','the Lord','the devil','your mother','the earth','the people','the One Ring','the Chosen One',
                 'the Queen','the judge','the jury','the Bible','the New Testament','the Old Testament','the Constitution','the Bill of Rights','the Declaration of Independence']
    plur_nouns = ['cats','rats','snakes','cheese','foxes','fish','tables','people','citizens','ideas','laws','taxes','potatoes','robots','things','gadgets','Aetheists','humans','families','pumpkins','tariffs','eggs','dogs','computers','chicken','dinosaurs',
                  'bees']
    people = ['Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','the one and only Jeff','Jeff the Killer',     'Obama','Heisenberg','Rick','Morty','Harry Potter',
            'some random guy','McDonalds','Sheldon1436','JosephGotG','satan','God','GreenTurtleFrog','Cpj2020','Verity','Jib','Notch','Mojang','Voldemort','He-Who-Must-Not-Be-Named','You-Know-Who','Kermit the Frog','Tony Stark','Microsoft',
            'Technoblade','Dream','CamMan18','Preston','KTaylor Gaming','Odin','Zeus','Poseidon','Thor','Magnus Chase','Percy Jackson','Desk Chair','Steve Jobs','Steve','Alex','Gandalf','Frodo','Dumbledore','Ron','Hagrid','Hermione']

    words = {
        'self': ['I'],
        'people': people,
        'peopleX': people,
        'verb': ['hate','love','eat','murder','own','ignore','sell','torture','kill','hang'],
        'verbS': ['hates','loves','eats','murders','owns','ignores','admires','cooks','sells','tortures','kills','hangs'],
        'past verb': ['hated','loved','ate','murdered','owned','ignored','sold','tortured','built','ignored','killed','hung'],
        'gverb': ['explode','die','dissapear','disintegrate','leave','apologize'],
        'locations': ['China','the United States of America','Texas','Germany','France','the Netherlands','the Nether','Hell','Heaven','Helheim','Limbo','the United Kingdom','Scotland','Australia','the depths','the shadow realm','Area 51','the End',
                      'the Overworld','the Sift','the Roblox Headquarters','Mother Russia','Georgia','South Park'],
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
        'punct': ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',    '...','!','?'],
        'com': [','],
        'conjunction': ['for','and','yet','so','because','or','or maybe']
    }
    nxt = {
        'start': ['self','people','userS','plur noun are','the noun is'],
        'self': ['verb','am','past verb'],
        'people': ['verbS','is','past verb'],
        'peopleX': ['punct','punct','punct','com'],
        'am': ['AMadjective','a','the noun','from','going to','peopleX'],
        'is': ['AMadjective','a','the noun','from','going to','peopleX'],
        'verb': ['plur noun','a','adjective','the noun'],
        'verbS': ['plur noun','user','the noun'],
        'gverb': ['punct','punct','punct','com'],
        'past verb': ['plur noun','user','the noun','a'],
        'user': ['punct','punct','punct','com'],
        'userS': ['are'],
        'are': ['AMadjective','a','the noun','from','going to','peopleX'],
        'noun': ['punct','punct','punct','com'],
        'the noun': ['punct','punct','punct','com'],
        'the noun is': ['is','past verb'],
        'plur noun are': ['are','past verb'],
        'plur noun': ['punct','punct','punct','com'],
        'adjective': ['plur noun'],
        'from': ['locations'],
        'going to': ['locations','gverb','verb'],
        'locations': ['punct','punct','punct','com'],
        'AMadjective': ['punct','punct','punct','com'],
        'com': ['conjunction'],
        'conjunction': ['self','people','userS','plur noun are','the noun is'],
        'adjectiveQ': ['noun'],
        'punct': ['self','people','userS','plur noun are','the noun is'],
        'a': ['adjectiveQ','noun']
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
        for _ in range(num):
            for key in nxt:
                nxt[key] = nxt[key][1:] + nxt[key][:1]
            for key in words:
                words[key] = words[key][1:] + words[key][:1]

    added = 1
    for let in inquiry:
        added += alphabet(let)
    iterate(added)
    word_id = ['start','start','start']
    answer = ''
    loop = 2
    for each in range(floor(sqrt(len(inquiry))*13)):
        xqc = word_id[loop]
        t = nxt[word_id[loop]]
        failed = True
        iteration = loop // 2
        tt = t[(loop * 13 + iteration * 17 + alphabet(inquiry[(loop + iteration) % len(inquiry)]) * 7) % len(t)]
        char = inquiry[(loop - 2) % len(inquiry)]
        choices = words[tt]
        if inquiry[(loop + iteration) % len(inquiry)].lower() == inquiry[(loop + iteration) % len(inquiry)]:
            word = choices[(alphabet(char) - 1) % len(choices)]
        else:
            word = choices[(alphabet(char) + 1) % len(choices)]
        if xqc == 'a' and ((word[0].lower() in ('i','o','u','a','e')) or (word == 'honest')):
            answer += 'n'
        if tt not in ('punct','com'):
            answer += ' '
        if xqc in ('start','punct'):
            answer += word[0].upper() + word[1:] 
        else:
            answer += word
        word_id.append(tt)
        loop += 1
        iterate(loop-1)

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
        if inquiry[(loop + iteration) % len(inquiry)].lower() == inquiry[(loop + iteration) % len(inquiry)]:
            word = choices[(alphabet(char) - 1) % len(choices)]
        else:
            word = choices[(alphabet(char) + 1) % len(choices)]
        if xqc == 'a' and ((word[0].lower() in ('i','o','u','a','e')) or (word == 'honest')):
            answer += 'n'
        if tt not in ('punct','com'):
            answer += ' '
        if xqc in ('start','punct'):
            answer += word[0].upper() + word[1:]
        else:
            answer += word
        word_id.append(tt)
        loop += 1
        iterate(loop-1)

        if tt == 'punct': finished = True

    return answer