import json, sys, string, urllib, urllib, re

def search(query):
    q = {'titles': query}
    url = 'http://en.wikipedia.org/w/api.php?format=json&action=query&' + urllib.urlencode(q) + '&prop=revisions&rvprop=content&rvsection=0'
    content = json.loads(urllib.urlopen(url).read())
    for page in content["query"]["pages"]:
        info = content["query"]["pages"][page]["revisions"][0]["*"]
        print info
        matchObj = re.search("birth_name * = (.*) .*", info)
        if matchObj:
            print "yes"
            print matchObj.group(1)
        else:
            print "hello"
    #image_url = 'https://upload.wikimedia.org/wikipedia/commons/1/1e/' + 

if __name__ == "__main__": 
    search(sys.argv[1])