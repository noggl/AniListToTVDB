# Creates CSV from XEM.json
# CSV is in format Title;AniList ID;TVDB ID/TMDB ID;Season #
# XEM.json is in format {title: [{AniList ID: TVDB ID}}, with the AniList IDs in order of season number

import json
import csv
import os
import subprocess
import sys

def updateRepos():
    changes=False
    # Update anime-lists repo
    if not os.path.exists("anime-lists"):
        # Clone anime-lists repo
        os.system("git clone https://github.com/Fribb/anime-lists.git")
    else:
        # Check for and pull latest changes
        result = subprocess.check_output("cd anime-lists && git pull", shell=True)
        # Check if already up to date
        if 'Already up to date' not in str(result):
            print("Changes in anime-lists")
            changes=True
        else:
            print("No changes in anime-lists")
        
    # Update AOD Repo
    if not os.path.exists("anime-offline-database"):
        # Clone AOD repo
        os.system("git clone https://github.com/manami-project/anime-offline-database.git")
    else:
        # Pull latest changes
        result = subprocess.check_output("cd anime-offline-database && git pull", shell=True)
        # Check if val includes "Already up to date"
        if 'Already up to date' not in str(result):
            print("Changes in AOD")
            changes=True
        else:
            print("No changes in AOD")
    return changes

def loadAOD():
    with open("anime-offline-database/anime-offline-database.json", "r") as f:
        aod = json.load(f).get("data")
    print(str(len(aod)) + " entries in AOD")
    return aod

def loadAnimeList():
    with open("anime-lists/anime-list-full.json", "r") as f:
        anime_list = json.load(f)
    print(str(len(anime_list)) + " entries in anime-list")
    return anime_list

def createMapping():
    aod=loadAOD()
    anime_list=loadAnimeList()
    # Initialize mappings list
    mappings=[]
    for show in anime_list:
            #Display progress
            sys.stdout.write("\rLinking anime-list and AOD: " + str(len(mappings)) + "/" + str(len(anime_list)))
            showKeys=list(show.keys())
            if "anilist_id" in showKeys:
                # Look for show in AOD
                found=False
                anilist_url="https://anilist.co/anime/" + str(show["anilist_id"])
                for aodShow in aod:
                    if anilist_url in aodShow["sources"]:
                        aod_show=aodShow
                        found=True
                        break
                if found:
                    #Add Title and season from AOD to show
                    show["title"]=aod_show["title"]
                    # Combine animeSeason's year and season keys into string for sorting
                    if aod_show["animeSeason"]["season"]:
                        # Replace season name with number
                        if aod_show["animeSeason"]["season"] == "SPRING":
                            aod_show["animeSeason"]["season"]=2
                        elif aod_show["animeSeason"]["season"] == "SUMMER":
                            aod_show["animeSeason"]["season"]=3
                        elif aod_show["animeSeason"]["season"] == "FALL":
                            aod_show["animeSeason"]["season"]=4
                        elif aod_show["animeSeason"]["season"] == "WINTER":
                            aod_show["animeSeason"]["season"]=1
                        show["animeSeason"]=str(aod_show["animeSeason"]["year"]) + "-" + str(aod_show["animeSeason"]["season"])
                    else:
                        show["animeSeason"]=str(aod_show["animeSeason"]["year"])
                    # If the show is a TV show, use TVDB ID, else use TMDB ID
                    if show["type"] == "TV" and "thetvdb_id" in showKeys:
                        show["id"]=show["thetvdb_id"]
                    elif show["type"] == "MOVIE" and "themoviedb_id" in showKeys:
                        show["id"]=show["themoviedb_id"]
                    # Write to CSV
                    showKeys=list(show.keys())
                    if "id" in showKeys:
                        # If show is tv or a movie
                        if show["type"] == "TV" or show["type"] == "MOVIE":
                            mappings.append(show)
    print("\nLinked " + str(len(mappings)) + " shows and movies between anime-list and AOD")
    return mappings

def orderSeasons(mappings):
    seasonedMappings=[]
    for i in range(len(mappings)):
        # Display progress
        sys.stdout.write("\rOrdering seasons: " + str(i) + "/" + str(len(mappings)))
        #if mappings[i] is not already in seasonedMappings
        if not any(d["id"] == mappings[i]["id"] for d in seasonedMappings):
            seasons=[]
            seasons.append(mappings[i])
            for j in range(len(mappings)):
                if i != j:
                    if mappings[i]["id"] == mappings[j]["id"]:
                        seasons.append(mappings[j])
            if len(seasons) > 1:
                # sort seasons based on year and season
                seasons.sort(key=lambda x: x["animeSeason"])
                # replace seasons with numbers
                title=seasons[0]["title"]
                for k in range(len(seasons)):
                    seasons[k]["animeSeason"]=k+1
                    seasons[k]["title"]=title
            else:
                seasons[0]["animeSeason"]=1
            #print("Found " + str(len(seasons)) + " seasons for " + seasons[0]["title"] + " (" + str(seasons[0]["anilist_id"]) +")")
            if len(seasons) > 1 and seasons[0]["type"] == "MOVIE":
                print("\nWARNING: That's a bit weird, " + seasons[0]["title"] + " (" + str(seasons[0]["anilist_id"]) + ") is a movie and has " + str(len(seasons)) + " seasons")
            for season in seasons:
                seasonedMappings.append(season)
    # Sort mappings by title
    seasonedMappings.sort(key=lambda x: x["title"])
    # Get movies list
    movies=[]
    shows=set()
    for show in seasonedMappings:
        if show["type"] == "MOVIE":
            movies.append(show)
        else:
            shows.add(show["title"])
    print("\n\nFound " + str(len(seasonedMappings) - len(movies)) + " seasons across " + str(len(shows)) + " shows, and " + str(len(movies)) + " movies")
    # Write to CSV
    # Clear CSV
    return seasonedMappings

def main():
    # if there have been changes or if argument is given
    if updateRepos() or len(sys.argv) > 1:
        print("\nBuilding mapping!")
        mappings=createMapping()
        seasonedMappings=orderSeasons(mappings)
        # Load old mapping
        oldMapping=[]
        with open("mapping.csv", "r") as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
                oldMapping.append(row)
        open("mapping.csv", "w").close()
        print("\nChanges:")
        for show in seasonedMappings:
            with open("mapping.csv", "a") as f:
                csv.writer(f, delimiter=";").writerow([show["title"], show["anilist_id"], show["id"], show["animeSeason"]])
                # If show is not in oldMapping
                if not any(d[1] == str(show["anilist_id"]) for d in oldMapping):
                    if show["type"] == "TV":
                        print("Added " + show["title"] + " (" + str(show["anilist_id"]) + ") Season " + str(show["animeSeason"]))
                    elif show["type"] == "MOVIE":
                        print("Added " + show["title"] + " (" + str(show["anilist_id"]) + ")")
        return 0
    else:
        print("No changes, exiting")
        return 0


if __name__ == "__main__":
    main()