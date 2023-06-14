# Scrapes thexem.info for all mappings and saves them to XEM.json

import json
import requests

def pr(text):
    #print function
    #prints text to console and to log.txt
    print(text)
    with open("log.txt", "a") as f:
        f.write(text + "\n")

def get_shows():
    #Gets shows by urls at https://thexem.info/xem/shows
    #Returns a list of shows
    shows = []
    url = "https://thexem.info/xem/shows"
    r = requests.get(url)
    if r.status_code == 200:
        html = r.text
        html = html.split("\n")
        for line in html:
            if "href" in line and "xem/show/" in line:
                line = line.split('"')
                shows.append(line[1])
    return shows

def get_show(show):
    #Get the mappings by url at https://thexem.info/
    # AniDB Ids are the keys and TVDB Ids are the values
    # Returns a dictionary of mappings
    mappings = {}
    url = "https://thexem.info" + show
    r = requests.get(url)
    if r.status_code == 200:
        html = r.text
        html = html.split("\n")
    else:
        pr("Error: " + str(r.status_code) + " " + url)
        return None
    title=get_title(html)
    AniDB_IDs=get_AniDB_ID(html)
    #remove duplicates from AniDB_IDs but keep order
    AniDB_IDs=list(dict.fromkeys(AniDB_IDs))
    TVDB_IDs=get_TVDB_ID(html)
    #remove duplicates from TVDB_IDs but keep order
    TVDB_IDs=list(dict.fromkeys(TVDB_IDs))
    # Make sure there are the same number of AniDB and TVDB IDs
    if len(AniDB_IDs) == len(TVDB_IDs):
        pr("Mappings found for " + title)
        for i in range(len(AniDB_IDs)):
            mappings[AniDB_IDs[i]] = TVDB_IDs[i]
    else:
        #If there there is only 1 TVDB ID, use it for all AniDB IDs
        if len(TVDB_IDs) == 1 and len(AniDB_IDs) > 0:
            pr("Mappings found for " + title + " using only 1 TVDB ID")
            for AniDB_ID in AniDB_IDs:
                mappings[AniDB_ID] = TVDB_IDs[0]
        else:
            pr("Error: Can't auto match AniDB IDs to TVDB IDs for " + title)
            # Append the data to a file for manual matching if there are AniDB IDs
            if len(AniDB_IDs) > 0:
                with open("manual.txt", "a") as f:
                    f.write(title + "\n" + "AniDB IDs:\n")
                    for AniDB_ID in AniDB_IDs:
                        f.write(AniDB_ID + "\n")
                    f.write("TVDB IDs:\n")
                    for TVDB_ID in TVDB_IDs:
                        f.write(TVDB_ID + "\n")
                    f.write("\n\n")
            return None
    #print(str({title: mappings}))
    return {title: mappings}

def get_AniDB_ID(html):
    #Gets the AniDB Ids from the html
    #Returns a list of AniDB Ids
    # AniDB IDs are the text of the links to the AniDB pages
    AniDB_IDs = []
    for line in html:
        #pr("Reading Line" + line + "\n")
        if "href" in line and "anidb.net/perl-bin/" in line:
            line = line.split('"')
            # Get part after aid=
            AniDB_IDs.append(line[1].split("aid=")[-1])
    return AniDB_IDs

def get_TVDB_ID(html):
    #Gets the TVDB Ids from the html
    #Returns a list of TVDB Ids
    # TVDB IDs are the part after id= in the links to the TVDB pages
    TVDB_IDs = []
    for line in html:
        if "href" in line and "thetvdb.com/?tab=series" in line:
            line = line.split('"')
            TVDB_IDs.append(line[1].split("id=")[-1])
    return TVDB_IDs

def get_title(html):
    #IF HTML File exists, get the title from it
    #Returns the title of the show from the <title> tag
    title = ""
    for line in html:
        if "<title>" in line:
            title = line.split("<title>")[1].split("</title>")[0]
            # Get the part before | Mapping
            title = title.split(" | Mapping")[0]
    return title.strip()

#run the main function
def main():
    shows = get_shows()
    mappings = {}
    # Remove duplicates in shows
    shows = list(set(shows))
    #get mapping of shows
    for show in shows:
        mapping=get_show(show)
        # If show didn't return a mapping, skip it
        if mapping != None:
            mappings.update(mapping)
    #Alphabetize the keys
    mappings = dict(sorted(mappings.items()))
    #write mappings to json file
    with open("XEM.json", "w") as f:
        json.dump(mappings, f)

def test():
    #test function
    #gets the mappings for a single show
    show = "/xem/show/4162"
    mappings = get_show(show)
    pr(mappings)

if __name__ == "__main__":
    #confirm that the user needs to scrape thexem.info, and that they can't use the existing XEM.json
    print("")
    pr("!!!!!!!!!!!!!PLEASE DO NOT SCRAPE XEM!!!!!!!!!!!!!")
    pr("You should be able to just use the mapping.csv file in the github repo!")
    pr("Are you sure you want to proceed? (y/n)")
    if input().lower() == "y":
        pr("Scraping thexem.info")
        main()