import csv, math, string, sys
from nltk.corpus import stopwords

#Increases field size limit
csv.field_size_limit(1000000000)

def main (document):
    with open(document, 'rb') as csvfile:
        docreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        with open('alllyricsbyartist.csv', 'a') as f:
            docwriter = csv.writer(f, delimiter=',')
            lyrics = ''
            for row in docreader:
                artist = row[1]
                song = row[2]
                clean_song = clean_text(song)
                for word in clean_song:
                    lyrics += word + ' '
            docwriter.writerow([artist, lyrics])
            print "Done with " + document

def clean_text (text):
    lowercase_text = text.lower()
    unhyphenated = string.replace(lowercase_text, "-", " ")
    printable = filter(lambda x: x in string.printable, unhyphenated)
    spaced_commas = string.replace(printable, ",", ", ")
    n_standardize = string.replace(spaced_commas, "niggaz", "niggas")
    unpunctuated_text = string.translate(n_standardize, None, string.punctuation)
    split_text = unpunctuated_text.split()
    rapwords = ['rapgenius.com', 'chorus', 'verse', '2x', '3x', '4x', '5x', '6x', '7x', '8x', 
        '9x', '10x,' 'hook', 'intro', 'outro', 'u', '2', '4', 'em', 'dem', 'ya', 'hes', 'shes', 'im', 'theyre', 'youll', 'ima', 
        'iim', 'simi', 'hunh']
    names = ['unit', '50', 'cent', 'aesop', 'asap', 'aap', 'phife', 'shaheed', 'jarobi', 'q', 'tribe', 
        'quest', 'mca', 'beastie', 'adrock', 'kane', 'scrap', 'scoob', 'mcgruff', 'gruff', 'pun', 
        'punisher', 'buckshot', '5ft', 'smif', 'wessun', 'beatminerz', 'steele', 'lawnge', 'sheep', 
        'dres', 'krs', 'bdp', 'blastmaster', 'larock', 'scott', 'melodie', 'kris', 'nubian', 'jamar', 
        'puba', 'sadat', 'pubas', 'busta', 'pos', 'mase', 'dove', 'plug', 'diddy', 'notorious', 'puff', 
        'planets', 'dps', 'jeff', 'jazzy', 'fp', 'prince', 'jeffs', 'ryders', 'ruff', 'ryde', 'dmx', 
        'eve', 'swizz', 'beatz', 'wyclef', 'pras', 'fugees', 'lauryn', 'gangstarr', 'starr', 'guru', 
        'premier', 'shug', 'ghostface', 'theodore', 'wu', 'tang', 'raekwon', 'grandmaster', 'raheim', 
        'melle', 'chaka', 'khan', 'lloyd', 'banks', 'gza', 'rza', 'rakim', 'rakeem', 'immortal', 
        'technique', 'killah', 'inspectah', 'deck', 'jadakiss', 'jada', 'jadas', 'ja', 'jas', 'rule', 
        'hov', 'jay', 'z', 'vinnie', 'paz', 'jedi', 'vp', 'stoupe', 'jungle', 'jbs', 'afrika', 'cudi', 
        'grimm', 'kool', 'keith', 'kurtis', 'kim', 'kimmie', 'queen', 'bee', 'jm', 'll', 'j', 'mary', 
        'blige', 'mae', 'jamel', 'irief', 'masta', 'lyte', 'lytes', 'method', 'mobb', 'noyd', 'mos', 'def', 
        'talib', 'kweli', 'nas', 'naughty', 'vin', 'treach', 'nature', 'kay', 'gee', 'nicki', 'minaj', 
        'biggie', 'smalls', 'odb', 'ol', 'bastard', 'pe', 'public', 'enemy', 'flav', 'chuck', 'flavor', 'flava', 
        'griff', 'latifah', 'latifahs', 'redman', 'dmc', 'darryl', 'jay', 'cathy', 'salt', 'pepa', 'spinderella', 'pep', 
        'cheryl', 'sandra', 'schoolly', 'schooly', 'slick', 'rick', 'ricky', 'ricks', 'sp', 'poobs', 'dipset', 
        'diplomats', 'santana', 'rell', 'camron', 'juelz', 'cam', 'jim', 'sheek', 'lox', 'stylez', 'luchion', 
        'roots', 'tariq', 'malik', 'sugarhill', 'prince', 'fp', 'wiz', 'khalifa', 'clan', 'clef', 'sean', 
        'bone', 'thug', 'thugs', 'harmony', 'bow', 'wow', 'weezy', 'chingy', 'common', 'com', 'd12', 'eminem', 
        'marshall', 'mathers', 'dilla', 'dill', 'kanye', 'kanyes', 'yeezy', 'lu', 'lupe', 'fiasco', 'nelly', 'twista', 'chainz', 
        'krit', 'chamillionaire', 'childish', 'gambino', 'clipse', 'pusha', 'geto', 'gb', 'goodie', 'gipp', 
        'jd', 'jermaine', 'dupri', 'juvenile', 'wayne', 'luda', 'ludacris', 'missy', 'elliott', 'timbaland', 
        'mystikal', 'outkast', 'andre', 'boi', 'ross', 'scarface', 'mafia', 'magoo', 'ti', 'tru', 'ugk', 
        'vanilla', 'jeezy', '2pac', 'tupac', 'shakur', 'blackalicious', 'casual', 'hieroglyphics', 'del', 
        'coolio', 'cypress', 'dels', 'homosapien', 'domo', 'genesis', 'dre', '40', 'earl', 'earls', 'sweatshirt', 
        'eazy', 'hodgy', 'cube', 'macklemore', 'hammer', 'ren', 'yella', 'nwa', 'odd', 'schoolboy', 'q', 'skee', 
        'snoop', 'dogg', 'doggy', 'dpg', 'mischief', 'souls', 'pharcyde', 'cyde', 'loc', 'hort', 'tyler', 'creator', 'warren', 
        'cole', 'meek', 'mill', 'wale']
    stoplist = stopwords.words('english') + rapwords + names
    important_text = filter(lambda x: x not in stoplist, split_text)
    return important_text

if __name__ == "__main__": main(sys.argv[1])