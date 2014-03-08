import csv, math, string, sys

matrix = csv.reader(open("tfidf_matrix.csv", 'rb'))
simple = csv.writer(open("tfidf_simplified.csv", 'a'))

names = [None, "50 Cent", "Aesop Rock", "A$AP Rocky", "A Tribe Called Quest", "Beastie Boys", "Big Daddy Kane", "Big L", "Big Punisher", "Black Moon", "Black Sheep", "Boogie Down Productions", "Brand Nubian", "Busta Rhymes", "De La Soul", "Diddy", "Digable Planets", "DJ Jazzy Jeff & The Fresh Prince", "DMX", "Eve", "Fugees", "Gang Starr", "Ghostface Killah", "Grandmaster Flash & the Furious Five", "Grandmaster Flash", "G-Unit", "GZA", "Inspectah Deck", "Ja Rule", "Jay-Z", "Jungle Brothers", "Kid Cudi", "Kool G Rap", "Kool Keith", "KRS-One", "Kurtis Blow", "Lauryn Hill", "Lil' Kim", "LL Cool J", "Mary J. Blige", "Mase", "Masta Killa", "MC Lyte", "Method Man", "Mobb Deep", "Mos Def", "Nas", "Naughty By Nature", "Nicki Minaj", "The Notorious B.I.G.", "Ol' Dirty Bastard", "Public Enemy", "Q-Tip", "Queen Latifah", "Raekwon", "Rakim", "Redman", "Run-D.M.C.", "Salt-N-Pepa", "Schoolly D", "Slick Rick", "Talib Kweli", "The Diplomats", "The Roots", "RZA", "The Sugarhill Gang", "U-God", "Will Smith", "Wiz Khalifa", "Wu-Tang Clan", "Wyclef Jean", "Bone Thugs-N-Harmony", "Bow Wow", "Chingy", "Common", "D12", "Eminem", "Kanye West", "Lupe Fiasco", "Nelly", "2 Live Crew", "Arrested Development", "Big K.R.I.T.", "Geto Boys", "Goodie Mob", "Jermaine Dupri", "Juvenile", "Lil Wayne", "Ludacris", "Master P", "Missy Elliott", "Mystikal", "Outkast", "Rick Ross", "Scarface", "Three 6 Mafia", "T.I.", "TRU", "UGK", "Vanilla Ice", "Young Jeezy", "2pac", "Blackalicious", "Casual", "Coolio", "Cypress Hill", "Del Tha Funkee Homosapien", "Digital Underground", "Domo Genesis", "Dr. Dre", "E-40", "Earl Sweatshirt", "Eazy-E", "Hieroglyphics", "Hodgy Beats", "Ice Cube", "Ice-T", "Kendrick Lamar", "Lil B", "Macklemore", "MC Hammer", "Mike G", "N.W.A.", "Odd Future", "Schoolboy Q", "Skee-Lo", "Snoop Dogg", "Souls of Mischief", "Tha Dogg Pound", "The Game", "The Pharcyde", "Tone Loc", "Too Short", "Tyler, the Creator", "Warren G"]

simple.writerow(names)
i = 1
for row in matrix:
    simple_row = [names[i]]
    for item in row:
        simple_row.append(item.split()[1][:-1])
    simple.writerow(simple_row)
    i += 1
