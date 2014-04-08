import csv, math, numpy, string, sys, collections, random
from gensim import corpora, models, similarities

clusters = collections.defaultdict(list) #identify vectors by ids
names_dict = collections.defaultdict(str)
names_dict_copy = collections.defaultdict(str)

index = similarities.SparseMatrixSimilarity.load('tfidf.index')
corpus = corpora.MmCorpus.load('tfidf_model.tfidf')
sim = list(enumerate(index))
print "Index loaded."

def main():
    names = ["50 Cent", "Aesop Rock", "A$AP Rocky", "A Tribe Called Quest", "Beastie Boys", "Big Daddy Kane", "Big L", "Big Punisher", "Black Moon", "Black Sheep", "Boogie Down Productions", "Brand Nubian", "Busta Rhymes", "De La Soul", "Diddy", "Digable Planets", "DJ Jazzy Jeff & The Fresh Prince", "DMX", "Eve", "Fugees", "Gang Starr", "Ghostface Killah", "Grandmaster Flash & the Furious Five", "Grandmaster Flash", "G-Unit", "GZA", "Immortal Technique", "Inspectah Deck", "Jadakiss", "Ja Rule", "Jay-Z", "Jedi Mind Tricks", "Jungle Brothers", "Kid Cudi", "Kool G Rap", "Kool Keith", "KRS-One", "Kurtis Blow", "Lauryn Hill", "Lil' Kim", "LL Cool J", "Mary J. Blige", "Mase", "Masta Killa", "MC Lyte", "Meek Mill", "Method Man", "Mobb Deep", "Mos Def", "Nas", "Naughty By Nature", "Nicki Minaj", "The Notorious B.I.G.", "Ol' Dirty Bastard", "Public Enemy", "Q-Tip", "Queen Latifah", "Raekwon", "Rakim", "Redman", "Run-D.M.C.", "Salt-N-Pepa", "Schoolly D", "Slick Rick", "Styles P", "Talib Kweli", "The Diplomats", "The LOX", "The Roots", "RZA", "The Sugarhill Gang", "U-God", "Wale", "Will Smith", "Wiz Khalifa", "Wu-Tang Clan", "Wyclef Jean", "Big Sean", "Bone Thugs-N-Harmony", "Bow Wow", "Chance the Rapper", "Chingy", "Common", "D12", "Eminem", "J Dilla", "Kanye West", "Lupe Fiasco", "Nelly", "Twista", "2 Chainz", "2 Live Crew", "Arrested Development", "Big K.R.I.T.", "Chamillionaire", "Childish Gambino", "Clipse", "Geto Boys", "Goodie Mob", "J. Cole", "Jermaine Dupri", "Juvenile", "Lil Wayne", "Ludacris", "Master P", "Missy Elliott", "Mystikal", "Outkast", "Pusha T", "Rick Ross", "Scarface", "Three 6 Mafia", "Timbaland", "T.I.", "TRU", "UGK", "Vanilla Ice", "Young Jeezy", "2pac", "Blackalicious", "Casual", "Coolio", "Cypress Hill", "Del Tha Funkee Homosapien", "Digital Underground", "Domo Genesis", "Dr. Dre", "E-40", "Earl Sweatshirt", "Eazy-E", "Hieroglyphics", "Hodgy Beats", "Ice Cube", "Ice-T", "Kendrick Lamar", "Lil B", "Macklemore", "MC Hammer", "MC Ren", "Mike G", "N.W.A.", "Odd Future", "Schoolboy Q", "Skee-Lo", "Snoop Dogg", "Souls of Mischief", "Tha Dogg Pound", "The Game", "The Pharcyde", "Tone Loc", "Too Short", "Tyler, the Creator", "Warren G"]
    for i in range(0,153):
        names_dict[i] = names[i]
        names_dict_copy[i] = names[i]
    print "Names dictionary populated."
    for i in range(0,153):
        current_vector = random.sample(names_dict.keys(), 1)[0]
        print current_vector
        print "Processing vector " + str(current_vector)
        if clusters:
            distance_dict = {}
            for cluster in clusters: 
                distance_dict[cluster] = cluster_similarity(current_vector,cluster)
            most_similar = max(distance_dict.iterkeys(), key=lambda k: distance_dict[k])
            highest_similarity = distance_dict[most_similar]
            if highest_similarity > 0.0555156831182: #mean
                update_cluster(current_vector,most_similar)
            else:
                new_cluster(current_vector)
        else:
            clusters[1] = [current_vector]
            print "Cluster 1 created."
        del names_dict[current_vector]
    for cluster in clusters:
        cluster_artists = []
        for name in clusters[cluster]:
            cluster_artists.append(names_dict_copy[name])
        print cluster_artists
    return clusters

def vector_similarity(i,j): #by IDs
    return sim[i-1][1][j-1]

def cluster_similarity(i,cluster_id):
    cluster = clusters[cluster_id]
    total = 0
    for j in cluster:
        total += vector_similarity(i,j)
    return total/len(cluster)

def update_cluster(vector,cluster_id):
    clusters[cluster_id] += [vector]
    print "Cluster " + str(cluster_id) + " updated with new vector."

def new_cluster(vector):
    last_cluster = clusters.keys()[-1]
    clusters[last_cluster + 1] += [vector]
    print "Cluster " + str(last_cluster +1) + " created."

if __name__ == "__main__": main()

