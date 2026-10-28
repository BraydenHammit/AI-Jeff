from math import sqrt, floor
from alph import alphabet

def run(entry):
    inquiry = entry.get()
    if inquiry == '': inquiry = ' '

    adjectives = ['green','ugly','handsome','pretty','juicy','sentient','purple','fat','skinny','orange','red','demonic','high','low','slippery','rough','vibrant','large','massive','Scottish','disgusting','vile','godlike','good','bad','evil','pricey',
                  'smart','dumb','eligant','stupid','idiotic','intelligent','official','artificial','natural','German','dead','alive','goth','emo','egotistical','unrealistic','tasty','feminine','masculine','girly','manly','special','lonely','killer',
                  'intruiging','zesty','illegal','ethical','unethical','legal','religous','non-religous','colorful','Aetheist','British','French','English','American','Dutch','Czech','cheesy','wet','nasty','sticky','clean','rich','fancy','shiny','unintelligent',
                  'confused','slow','fast','sorry','gold','blue','yellow','pink','grey','brown','rainbow','clear','supportive','helpful','honest','dishonest','trustworthy','untrustworthy','loyal','universal','spiteful','helpless','bald','sour','bitter',
                  'humane','inhumane','toxic','poisonous','strange']
    nouns = ['cheese','basketball','football','McDonalds','cat','computer','AI','robot','dog','fox','snake','emu','table','emo','eclipse','famine','disease','thing','idea','BitCoin','doohickey','gadget','potato','dollar bill','Barbie doll','bread',
             'penny','t-shirt','dinosaur','turtle','killer','human','fish','feline','Aetheist','rat','pumpkin','quarter','nickel','egg','tariff','chicken','bee','salad','desk','mouse','chair','moose','cactus','plant','tree','banana','chair','bum',
             'man','woman','boy','girl','child','fungus','infection','virus','bacteria','amoeba','mushroom','ghost','skeleton','mummy','zombie','candy','pickle','apple']
    the_nouns = ['the cat','the government','the cheeseburger','the law','the future','the present','the past','the president','the moon landing','the King','the Lord','the devil','your mother','the Earth','the people','the One Ring','the Chosen One',
                 'the Queen','the judge','the jury','the Bible','the New Testament','the Old Testament','the Constitution','the Bill of Rights','the Declaration of Independence','the CIA','the FBI','the FDA','the Secret Service','everything']
    plur_nouns = ['cats','rats','snakes','cheese','foxes','fish','tables','people','citizens','ideas','laws','taxes','potatoes','robots','things','gadgets','Aetheists','humans','families','pumpkins','tariffs','eggs','dogs','computers','chicken','dinosaurs',
                  'bees','mice','geese','desks','chairs','bananas','plants','trees','cacti','mooses','bums','men','women','boys','girls','children','fungi','infections','viruses','bacteria','amoebae','mushrooms','ghosts','skeletons','mummies','zombies',
                  'candies','pickles','apples','human rights']
    people = ['Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','Jeff','the one and only Jeff','Jeff the Killer',     'Obama','Heisenberg','Rick','Morty','Harry Potter','Elon Musk',
            'some random guy','McDonalds','Sheldon1436','satan','God','GreenTurtleFrog','Cpj2020','Verity','Jib','Notch','Mojang','Voldemort','He-Who-Must-Not-Be-Named','You-Know-Who','Kermit the Frog','Tony Stark','Microsoft','Tom Holland','Spiderman',
            'Technoblade','Dream','CamMan18','Preston','KTaylor Gaming','Odin','Zeus','Poseidon','Thor','Magnus Chase','Percy Jackson','Desk Chair','Steve Jobs','Steve','Alex','Gandalf','Frodo','Dumbledore','Ron','Hagrid','Hermione','Iron Man','Zendaya',
            'the Hulk','Bruce Banner','some dude','Dr. Seuss','Dr. Strange','Darth Vader','Luke Skywalker','Obi-Wan Kenobi']

    words = {
        'self': ['I'],
        "selfm": ["I'm","I'm not"],
        'people': people,
        'peopleX': people,
        'verb': ['hate','love','eat','murder','own','ignore','sell','torture','kill','hang','hunt','seek out','rename'],
        'verbS': ['hates','loves','eats','murders','owns','ignores','admires','cooks','sells','tortures','kills','hangs','hunts','seeks','renames'],
        'past verb': ['hated','loved','ate','murdered','owned','ignored','sold','tortured','built','ignored','killed','hung','hunted','sought','renamed'],
        'gverb': ['explode','die','dissapear','disintegrate','leave','apologize'],
        'verbing': ['killing','murdering','hanging','removing','executing','hunting','torturing','eating','ignoring'],
        'locations': ['China','the United States of America','Texas','Germany','France','the Netherlands','the Nether','Hell','Heaven','Helheim','Limbo','the United Kingdom','Scotland','Australia','the depths','the shadow realm','Area 51','the End',
                      'the Overworld','the Sift','the Roblox Headquarters','Mother Russia','Georgia','South Park','Czechia'],
        'going to': ['going to'],
        'am': ['am','am not'],
        'are': ['are','are not'],
        'is': ['is','is not',"isn't"],
        'be': ['be'],
        'userS': ['you'],
        'from': ['from'],
        'a': ['a'],
        'user': ['you'],
        'answer': ['yes','no','maybe','probably','probably not'],
        'noun': nouns,
        'the noun': the_nouns,
        'the noun is': the_nouns,
        'plur noun': plur_nouns,
        'plur noun are': plur_nouns,
        'adjective': adjectives,
        'adjectiveQ': adjectives,
        'AMadjective': adjectives,
        'punct': ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',    '...','!','?'],
        'com': [','],
        'conjunction': ['for','and','yet','so','because','or','or maybe']
    }
    nxt = {
        'start': ['self','selfm','people','userS','plur noun are','the noun is','answer'],
        'self': ['verb','am','past verb'],
        'people': ['verbS','is','past verb'],
        'peopleX': ['punct','punct','punct','com'],
        'am': ['AMadjective','a','the noun','from','going to','peopleX','verbing'],
        'selfm': ['AMadjective','a','the noun','from','going to','peopleX','verbing'],
        'is': ['AMadjective','a','the noun','from','going to','peopleX','verbing'],
        'verb': ['plur noun','a','adjective','the noun'],
        'verbing': ['plur noun','a','adjective','the noun'],
        'verbS': ['plur noun','user','the noun'],
        'gverb': ['punct','punct','punct','com'],
        'past verb': ['plur noun','user','the noun','a'],
        'user': ['punct','punct','punct','com'],
        'userS': ['are'],
        'are': ['AMadjective','a','the noun','from','going to','peopleX','verbing'],
        'noun': ['punct','punct','punct','com'],
        'the noun': ['punct','punct','punct','com'],
        'the noun is': ['is','past verb'],
        'plur noun are': ['are','past verb'],
        'plur noun': ['punct','punct','punct','com'],
        'adjective': ['plur noun'],
        'from': ['locations'],
        'going to': ['locations','gverb','verb','be'],
        'locations': ['punct','punct','punct','com'],
        'AMadjective': ['punct','punct','punct','com'],
        'be': ['AMadjective','a'],
        'com': ['conjunction'],
        'conjunction': ['self','selfm','people','userS','plur noun are','the noun is'],
        'adjectiveQ': ['noun'],
        'punct': ['self','selfm','people','userS','plur noun are','the noun is','answer'],
        'a': ['adjectiveQ','noun'],
        'answer': ['punct','punct','punct','com']
    }

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

    extloop = 0
    if word_id[loop] == 'punct': finished = True
    else: finished = False
    while finished == False:
        xqc = word_id[loop]
        t = nxt[word_id[loop]]
        if ('com' in t) and extloop > 99:
            t = ['punct']
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
        extloop += 1
        iterate(loop-1)

        if tt == 'punct': finished = True

    return answer