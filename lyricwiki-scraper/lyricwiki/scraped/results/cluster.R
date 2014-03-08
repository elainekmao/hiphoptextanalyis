#east_coast_names <- c("50 Cent", "Aesop Rock", "A$AP Rocky", "A Tribe Called Quest", "Beastie Boys", "Big Daddy Kane", "Big L", "Big Punisher", "Black Moon", "Black Sheep", "Boogie Down Productions", "Brand Nubian", "Busta Rhymes", "De La Soul", "Diddy", "Digable Planets", "DJ Jazzy Jeff & The Fresh Prince", "DMX", "Eve", "Fugees", "Gang Starr", "Ghostface Killah", "Grandmaster Flash & the Furious Five", "Grandmaster Flash", "G-Unit", "GZA", "Inspectah Deck", "Ja Rule", "Jay-Z", "Jungle Brothers", "Kid Cudi", "Kool G Rap", "Kool Keith", "KRS-One", "Kurtis Blow", "Lauryn Hill", "Lil' Kim", "LL Cool J", "Mary J. Blige", "Mase", "Masta Killa", "MC Lyte", "Method Man", "Mobb Deep", "Mos Def", "Nas", "Naughty By Nature", "Nicki Minaj", "The Notorious B.I.G.", "Ol' Dirty Bastard", "Public Enemy", "Q-Tip", "Queen Latifah", "Raekwon", "Rakim", "Redman", "Run-D.M.C.", "Salt-N-Pepa", "Schoolly D", "Slick Rick", "Talib Kweli", "The Diplomats", "The Roots", "RZA", "The Sugarhill Gang", "U-God", "Will Smith", "Wiz Khalifa", "Wu-Tang Clan", "Wyclef Jean")
#midwest_names <- c("Bone Thugs-N-Harmony", "Bow Wow", "Chingy", "Common", "D12", "Eminem", "Kanye West", "Lupe Fiasco", "Nelly")
#south_names <- c("2 Live Crew", "Arrested Development", "Big K.R.I.T.", "Geto Boys", "Goodie Mob", "Jermaine Dupri", "Juvenile", "Lil Wayne", "Ludacris", "Master P", "Missy Elliott", "Mystikal", "Outkast", "Rick Ross", "Scarface", "Three 6 Mafia", "T.I.", "TRU", "UGK", "Vanilla Ice", "Young Jeezy")
#west_coast_names <- c("2pac", "Blackalicious", "Casual", "Coolio", "Cypress Hill", "Del Tha Funkee Homosapien", "Digital Underground", "Domo Genesis", "Dr. Dre", "E-40", "Earl Sweatshirt", "Eazy-E", "Hieroglyphics", "Hodgy Beats", "Ice Cube", "Ice-T", "Kendrick Lamar", "Lil B", "Macklemore", "MC Hammer", "Mike G", "N.W.A.", "Odd Future", "Schoolboy Q", "Skee-Lo", "Snoop Dogg", "Souls of Mischief", "Tha Dogg Pound", "The Game", "The Pharcyde", "Tone Loc", "Too Short", "Tyler, the Creator", "Warren G")

east = read.csv("east_coast_tfidf.csv", header=F, sep=",")
midwest = read.csv("midwest_tfidf.csv", header=F, sep=",")
south = read.csv("south_tfidf.csv", header=F, sep=",")
west = read.csv("west_coast_tfidf.csv", header=F, sep=",")

row.names(east) <- "East"
row.names(midwest) <- "Midwest"
row.names(south) <- "South"
row.names(west) <- "West"

complete <- rbind(east, midwest, south, west)

cosine_distance <- function(a,b) {
    (a %*% b)/(sqrt(a%*%a)*sqrt(b%*%b))
}

newplot <- function() { windows() }

d = dist(complete, cosine_distance)

fit <- cmdscale(d,eig=TRUE, k=4) # k is the number of dim
x <- fit$points[,1]
y <- fit$points[,2]

newplot()
regions = factor(row.names(complete))
plot(x, y, xlab="Coordinate 1", ylab="Coordinate 2", main="United States Hip-Hop", pch=19, col=regions)
legend('topright', legend = levels(regions), col=palette(), cex = 0.8, pch = 1)