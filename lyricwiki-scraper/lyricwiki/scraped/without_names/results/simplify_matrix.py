import csv, math, string, sys

matrix = csv.reader(open("tfidf_matrix.csv", 'rb'))
simple = csv.writer(open("tfidf_simplified.csv", 'a'))

names = [None, "50 Cent", "Aesop Rock", "A$AP Rocky", "A Tribe Called Quest", "Beastie Boys", "Big Daddy Kane", "Big L", "Big Punisher", "Black Moon", "Black Sheep", "Boogie Down Productions", "Brand Nubian", "Busta Rhymes", "De La Soul", "Diddy", "Digable Planets", "DJ Jazzy Jeff & The Fresh Prince", "DMX", "Eve", "Fugees", "Gang Starr", "Ghostface Killah", "Grandmaster Flash & the Furious Five", "Grandmaster Flash", "G-Unit", "GZA", "Immortal Technique", "Inspectah Deck", "Jadakiss", "Ja Rule", "Jay-Z", "Jedi Mind Tricks", "Jungle Brothers", "Kid Cudi", "Kool G Rap", "Kool Keith", "KRS-One", "Kurtis Blow", "Lauryn Hill", "Lil' Kim", "LL Cool J", "Mary J. Blige", "Mase", "Masta Killa", "MC Lyte", "Meek Mill", "Method Man", "Mobb Deep", "Mos Def", "Nas", "Naughty By Nature", "Nicki Minaj", "The Notorious B.I.G.", "Ol' Dirty Bastard", "Public Enemy", "Q-Tip", "Queen Latifah", "Raekwon", "Rakim", "Redman", "Run-D.M.C.", "Salt-N-Pepa", "Schoolly D", "Slick Rick", "Styles P", "Talib Kweli", "The Diplomats", "The LOX", "The Roots", "RZA", "The Sugarhill Gang", "U-God", "Wale", "Will Smith", "Wiz Khalifa", "Wu-Tang Clan", "Wyclef Jean", "Big Sean", "Bone Thugs-N-Harmony", "Bow Wow", "Chance the Rapper", "Chingy", "Common", "D12", "Eminem", "J Dilla", "Kanye West", "Lupe Fiasco", "Nelly", "Twista", "2 Chainz", "2 Live Crew", "Arrested Development", "Big K.R.I.T.", "Chamillionaire", "Childish Gambino", "Clipse", "Geto Boys", "Goodie Mob", "J. Cole", "Jermaine Dupri", "Juvenile", "Lil Wayne", "Ludacris", "Master P", "Missy Elliott", "Mystikal", "Outkast", "Pusha T", "Rick Ross", "Scarface", "Three 6 Mafia", "Timbaland", "T.I.", "TRU", "UGK", "Vanilla Ice", "Young Jeezy", "2pac", "Blackalicious", "Casual", "Coolio", "Cypress Hill", "Del Tha Funkee Homosapien", "Digital Underground", "Domo Genesis", "Dr. Dre", "E-40", "Earl Sweatshirt", "Eazy-E", "Hieroglyphics", "Hodgy Beats", "Ice Cube", "Ice-T", "Kendrick Lamar", "Lil B", "Macklemore", "MC Hammer", "MC Ren", "Mike G", "N.W.A.", "Odd Future", "Schoolboy Q", "Skee-Lo", "Snoop Dogg", "Souls of Mischief", "Tha Dogg Pound", "The Game", "The Pharcyde", "Tone Loc", "Too Short", "Tyler, the Creator", "Warren G"]

simple.writerow(names)
i = 1
for row in matrix:
    simple_row = [names[i]]
    for item in row:
        simple_row.append(item.split()[1][:-1])
    simple.writerow(simple_row)
    i += 1
