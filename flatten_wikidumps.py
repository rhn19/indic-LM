'''
Download the latest wikidumps using-
!wget "http://download.wikimedia.org/mrwiki/latest/mrwiki-latest-pages-articles.xml.bz2"

Change mr to the appropriate language code to download wikidumps for other langauges
'''

'''
Make sure you install wikiextractor-0.1 to avoid migration issues
!pip install wikiextractor==0.1
'''

'''
Run the following command in the terminal with the correct language code and wikidump location
!python -m wikiextractor.WikiExtractor --json -o extracted /content/mrwiki-latest-pages-articles.xml.bz2

Then run this command to extract the text files
!find extracted -name '*bz2' -exec bzip2 -d {} \; > text.xml
'''

#Get all file paths for easy traversal
import glob
file_paths = []
file_paths.extend(glob.glob("/content/extracted/AA/*"))
file_paths.extend(glob.glob("/content/extracted/AB/*"))
file_paths = sorted(file_paths)
# print(file_paths)
# print(len(file_paths))

#add the json contents to a list
import json
result = []
for name in file_paths:
    with open(name, "r") as f:
        for line in f:
            result.append(json.loads(line))

# print(len(result))
# print(result[0])

#save the json output in a single file
with open("mr_wiki.json", "w") as outfile:
     json.dump(result, outfile)