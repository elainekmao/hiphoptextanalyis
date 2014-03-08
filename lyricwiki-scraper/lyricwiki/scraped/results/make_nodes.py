import csv, math, string, sys, json

f = csv.reader(open("tfidf_matrix.csv", 'rb'))
matrix = []
for row in f:
    matrix.append(row)

names = [None, "50 Cent", "Aesop Rock", "A$AP Rocky", "A Tribe Called Quest", "Beastie Boys", "Big Daddy Kane", "Big L", "Big Punisher", "Black Moon", "Black Sheep", "Boogie Down Productions", "Brand Nubian", "Busta Rhymes", "De La Soul", "Diddy", "Digable Planets", "DJ Jazzy Jeff & The Fresh Prince", "DMX", "Eve", "Fugees", "Gang Starr", "Ghostface Killah", "Grandmaster Flash & the Furious Five", "Grandmaster Flash", "G-Unit", "GZA", "Inspectah Deck", "Ja Rule", "Jay-Z", "Jungle Brothers", "Kid Cudi", "Kool G Rap", "Kool Keith", "KRS-One", "Kurtis Blow", "Lauryn Hill", "Lil' Kim", "LL Cool J", "Mary J. Blige", "Mase", "Masta Killa", "MC Lyte", "Method Man", "Mobb Deep", "Mos Def", "Nas", "Naughty By Nature", "Nicki Minaj", "The Notorious B.I.G.", "Ol' Dirty Bastard", "Public Enemy", "Q-Tip", "Queen Latifah", "Raekwon", "Rakim", "Redman", "Run-D.M.C.", "Salt-N-Pepa", "Schoolly D", "Slick Rick", "Talib Kweli", "The Diplomats", "The Roots", "RZA", "The Sugarhill Gang", "U-God", "Will Smith", "Wiz Khalifa", "Wu-Tang Clan", "Wyclef Jean", "Bone Thugs-N-Harmony", "Bow Wow", "Chingy", "Common", "D12", "Eminem", "Kanye West", "Lupe Fiasco", "Nelly", "2 Live Crew", "Arrested Development", "Big K.R.I.T.", "Geto Boys", "Goodie Mob", "Jermaine Dupri", "Juvenile", "Lil Wayne", "Ludacris", "Master P", "Missy Elliott", "Mystikal", "Outkast", "Rick Ross", "Scarface", "Three 6 Mafia", "T.I.", "TRU", "UGK", "Vanilla Ice", "Young Jeezy", "2pac", "Blackalicious", "Casual", "Coolio", "Cypress Hill", "Del Tha Funkee Homosapien", "Digital Underground", "Domo Genesis", "Dr. Dre", "E-40", "Earl Sweatshirt", "Eazy-E", "Hieroglyphics", "Hodgy Beats", "Ice Cube", "Ice-T", "Kendrick Lamar", "Lil B", "Macklemore", "MC Hammer", "Mike G", "N.W.A.", "Odd Future", "Schoolboy Q", "Skee-Lo", "Snoop Dogg", "Souls of Mischief", "Tha Dogg Pound", "The Game", "The Pharcyde", "Tone Loc", "Too Short", "Tyler, the Creator", "Warren G"]

def get_region(i):
    if i in range(1,71):
        return 1
    elif i in range(71,80):
        return 2
    elif i in range(80,101):
        return 3
    elif i in range(101,135):
        return 4

nodes_list = []
for i in range(1,135):
    entry = {'name': names[i], 'group': get_region(i)}
    nodes_list.append(entry)

link_list = []
for i in range(0,134):
    for j in range(i,134):
        if i!= j:
            value = float(matrix[i][j].split()[1][:-1])
            if value >= 0.046924364:
                entry = {'source': i, 'target': j, 'value': value}
                link_list.append(entry)

with open('hiphop_2.json', 'a') as jsonfile:
    jsonfile.write('{')
    jsonfile.write('"nodes": [')
    for i in range(len(nodes_list)):
        json.dump(nodes_list[i], jsonfile)
        jsonfile.write(',')
        jsonfile.write('\n')
    jsonfile.write('],')
    jsonfile.write('"links": [')
    for i in range(len(link_list)):
        json.dump(link_list[i], jsonfile)
        jsonfile.write(',')
        jsonfile.write('\n')
    jsonfile.write(']')
    jsonfile.write('}')

