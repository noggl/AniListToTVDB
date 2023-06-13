# Creates CSV from XEM.json
# CSV is in format Title;AniList ID;TVDB ID/TMDB ID;Season #
# XEM.json is in format {title: [{AniList ID: TVDB ID}}, with the AniList IDs in order of season number

import json
import csv
import os
import wget

def setupAOD():
    if not os.path.exists("anime-offline-database.json"):
        wget.download("https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database.json", "anime-offline-database.json")
    with open("anime-offline-database.json", "r") as f:
        AOD = json.load(f).get("data")
    return AOD

def getAniListID(AOD,AniDB_IDs):
    # Download the AOD JSON from github
    # https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database.json
        AniList_IDs=[]
        for AniDB_ID in AniDB_IDs:
            matched=False
            anidb_url="https://anidb.net/anime/" + AniDB_ID
            for show in AOD:
                if anidb_url in show["sources"]:
                    for source in show["sources"]:
                        if "anilist.co" in source:
                            anilist_url = source
                            AniList_ID = anilist_url.split("/")[-1]
                            matched=True
                            print("Matched " + AniList_ID + " to " + AniDB_ID)
                            AniList_IDs.append(AniList_ID)
                            # Break out of the loop
                            break
            # If the show wasn't found in AOD, write to manual.txt
            if not matched:
                print("Couldn't find " + AniDB_ID + " in AOD")
                with open("manual.txt", "a") as f:
                    #if file isn't empty, add a newline
                    if f.tell() != 0:
                        f.write("\n")
                    f.write("NOT FOUND IN AOD - AniDB ID: " + AniDB_ID)
        return AniList_IDs

def main():
    AOD=setupAOD()
    with open("XEM.json", "r") as f:
            mappings = json.load(f)
            with open("mappings.csv", "w") as f:
                #Sort mappings by title
                mappings = dict(sorted(mappings.items()))
                for title in mappings:
                        keys=getAniListID(AOD,list(mappings[title].keys()))
                        for i in range(len(keys)):
                            key=keys[i]
                            value=list(mappings[title].values())[0]
                            season=i+1
                            csv.writer(f, delimiter=";").writerow([title, key, value, season])

if __name__ == "__main__":
    main()