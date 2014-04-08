import csv, math, string, sys, json, collections

f = csv.reader(open("tfidf_matrix.csv", 'rb'))
matrix = []
for row in f:
    matrix.append(row)

names = [None, "50 Cent", "Aesop Rock", "A$AP Rocky", "A Tribe Called Quest", "Beastie Boys", "Big Daddy Kane", "Big L", "Big Punisher", "Black Moon", "Black Sheep", "Boogie Down Productions", "Brand Nubian", "Busta Rhymes", "De La Soul", "Diddy", "Digable Planets", "DJ Jazzy Jeff & The Fresh Prince", "DMX", "Eve", "Fugees", "Gang Starr", "Ghostface Killah", "Grandmaster Flash & the Furious Five", "Grandmaster Flash", "G-Unit", "GZA", "Immortal Technique", "Inspectah Deck", "Jadakiss", "Ja Rule", "Jay-Z", "Jedi Mind Tricks", "Jungle Brothers", "Kid Cudi", "Kool G Rap", "Kool Keith", "KRS-One", "Kurtis Blow", "Lauryn Hill", "Lil' Kim", "LL Cool J", "Mary J. Blige", "Mase", "Masta Killa", "MC Lyte", "Meek Mill", "Method Man", "Mobb Deep", "Mos Def", "Nas", "Naughty By Nature", "Nicki Minaj", "The Notorious B.I.G.", "Ol' Dirty Bastard", "Public Enemy", "Q-Tip", "Queen Latifah", "Raekwon", "Rakim", "Redman", "Run-D.M.C.", "Salt-N-Pepa", "Schoolly D", "Slick Rick", "Styles P", "Talib Kweli", "The Diplomats", "The LOX", "The Roots", "RZA", "The Sugarhill Gang", "U-God", "Wale", "Will Smith", "Wiz Khalifa", "Wu-Tang Clan", "Wyclef Jean", "Big Sean", "Bone Thugs-N-Harmony", "Bow Wow", "Chance the Rapper", "Chingy", "Common", "D12", "Eminem", "J Dilla", "Kanye West", "Lupe Fiasco", "Nelly", "Twista", "2 Chainz", "2 Live Crew", "Arrested Development", "Big K.R.I.T.", "Chamillionaire", "Childish Gambino", "Clipse", "Geto Boys", "Goodie Mob", "J. Cole", "Jermaine Dupri", "Juvenile", "Lil Wayne", "Ludacris", "Master P", "Missy Elliott", "Mystikal", "Outkast", "Pusha T", "Rick Ross", "Scarface", "Three 6 Mafia", "Timbaland", "T.I.", "TRU", "UGK", "Vanilla Ice", "Young Jeezy", "2pac", "Blackalicious", "Casual", "Coolio", "Cypress Hill", "Del Tha Funkee Homosapien", "Digital Underground", "Domo Genesis", "Dr. Dre", "E-40", "Earl Sweatshirt", "Eazy-E", "Hieroglyphics", "Hodgy Beats", "Ice Cube", "Ice-T", "Kendrick Lamar", "Lil B", "Macklemore", "MC Hammer", "MC Ren", "Mike G", "N.W.A.", "Odd Future", "Schoolboy Q", "Skee-Lo", "Snoop Dogg", "Souls of Mischief", "Tha Dogg Pound", "The Game", "The Pharcyde", "Tone Loc", "Too Short", "Tyler, the Creator", "Warren G"]

words_dict = {}
top_10 = csv.reader(open("../clean_top_10.csv", "rb"))
for line in top_10:
    words_dict [line[0]] = line[1:]

def get_region(i):
    if i in range(1,78):
        return 1
    elif i in range(78,91):
        return 2
    elif i in range(91,119):
        return 3
    elif i in range(119,154):
        return 4

link_dict = collections.defaultdict(list)
link_list = []
for i in range(0,153):
    for j in range(i,153):
        if i!= j:
            value = float(matrix[i][j].split()[1][:-1])
            if value > 0.0555156831182:        #CAN CHANGE THIS VALUE TO MODIFY EDGES INCLUDED
                entry = {'source': i, 'target': j, 'weight': value}
                link_list.append(entry)
                link_dict[i].append(j)
                link_dict[j].append(i)

nodes_list = []
for i in range(1,154):
    entry = {'index': i-1, 'links': link_dict[i-1], 'name': names[i], 'group': get_region(i), 'words': words_dict[names[i]]}
    nodes_list.append(entry)

with open('hiphop.json', 'a') as jsonfile:
    jsonfile.write('{\n')
    jsonfile.write('"nodes": [\n')
    for i in range(len(nodes_list)):
        json.dump(nodes_list[i], jsonfile)
        if i != len(nodes_list) - 1:
            jsonfile.write(',')
        jsonfile.write('\n')
    jsonfile.write('],\n')
    jsonfile.write('"links": [')
    for i in range(len(link_list)):
        json.dump(link_list[i], jsonfile)
        if i != len(link_list) - 1:
            jsonfile.write(',')
        jsonfile.write('\n')
    jsonfile.write(']\n')
    jsonfile.write('}')

