import datetime
import json
import csv
import os
import subprocess
import sys

def getCommitDate(URL):
    # Parse url for file name, user, and repo
    githubFile=URL.split("/")[-1]
    githubRepo=URL.split("/")[-3]
    githubUser=URL.split("/")[-4]
    requestURL="https://api.github.com/repos/" + githubUser + "/" + githubRepo + "/commits?path=" + githubFile
    # Get last updated date from github
    result = subprocess.check_output("curl -s " + requestURL, shell=True)
    # convert result to dictionary
    result = json.loads(result)
    date=result[0]["commit"]["author"]["date"]
    # Convert date to datetime object
    lastUpdated=datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    return lastUpdated

def updateLog(strings):
    # Delete all lines after "Updates:"
    with open("updated.txt", "r") as f:
        lines=f.readlines()
    with open("updated.txt", "w") as f:
        for line in lines:
            if line.startswith("Recent Updates:"):
                break
            else:
                #if line isn't empty or just a newline
                if line.strip():
                    f.write(line)
    # Write strings to file
    with open("updated.txt", "a") as f:
        print("\nUpdates:")
        f.write("\nRecent Updates:\n")
        for string in strings:
            print(string)
            f.write(string + "\n")

def updateREADME():
    # Replace the Status section of the README with the contents of updated.txt
    with open("README.md", "r") as f:
        lines=f.readlines()
    with open("README.md", "w") as f:
        for line in lines:
            if line.startswith("## Status"):
                break
            else:
                f.write(line)
        f.write("## Status\n")
        with open("updated.txt", "r") as f2:
            for line in f2:
                #if line starts with Added
                if line.startswith("Added"):
                    f.write("- " + line)
                else:
                    f.write(line+ "\n")
    
def getLocalDate(filename):
    found=False
    if not os.path.exists("updated.txt"):
        return False
    with open("updated.txt", "r") as f:
        # Get date from updated.txt. Find line that starts with "anime-list-full.json was last updated"
        for line in f:
            if line.startswith(filename + " was last updated"):
                # Get "%Y-%m-%dT%H:%M:%SZ" from line
                lastUpdated=datetime.datetime.strptime(line.split(" was last updated at ")[1].strip(), "%Y-%m-%d %H:%M:%S.%f")
                found=True
                break
    if not found:
        return False
    else:
        return lastUpdated

def refreshFile(url):
    changes=False
    filename=url.split("/")[-1]
    if not os.path.exists(filename):
        print(filename + " not found. Downloading...")
        changes=True
        # Download the file
        downloadFile(url)
    else:
        localDate=getLocalDate(filename)
        # Get date from github
        githubDate=getCommitDate(url)
        # Compare dates
        if localDate == False or localDate < githubDate:
            print(filename + " is out of date. Downloading...")
            changes=True
            # Download the file
            downloadFile(url)
        else:
            print("No changes to " + filename)
    return changes

def downloadFile(url):
    #parse url for file name
    fileName=url.split("/")[-1]
    os.system("curl -s "+ url + " -o " + fileName)
    # Write current date to updated.txt
    if os.path.exists("updated.txt"):
        # If filename is already in the doc, update it, otherwise append it
        found=False
        with open("updated.txt", "r") as f:
            for line in f:
                if line.startswith(fileName):
                    found=True
                    break
        if found:
            with open("updated.txt", "r") as f:
                lines=f.readlines()
            with open("updated.txt", "w") as f:
                for line in lines:
                    if line.startswith(fileName):
                        #Write Datetime to file
                        f.write(fileName + " was last updated at " + str(datetime.datetime.now()) + "\n")
                    else:
                        f.write(line)
        else:
            with open("updated.txt", "a") as f:
                f.write(fileName + " was last updated at " + str(datetime.datetime.now()) + "\n")
    else:
        # Create the file
        with open("updated.txt", "w") as f:
            f.write(fileName + " was last updated at " + str(datetime.datetime.now()) + "\n")


def updateDB():
    changes=False
    # Update anime-list-full.json
    url="https://raw.githubusercontent.com/Fribb/anime-lists/master/anime-list-full.json"
    if refreshFile(url):
        changes=True
        # Update anime-offline-database.json"
    url="https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database.json"
    if refreshFile(url):
        changes=True
    return changes

def loadAOD():
    with open("anime-offline-database.json", "r") as f:
        aod = json.load(f).get("data")
    print(str(len(aod)) + " entries in AOD")
    return aod

def loadAnimeList():
    with open("anime-list-full.json", "r") as f:
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
        sys.stdout.write("\Putting seasons in order: " + str(i) + "/" + str(len(mappings)))
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
    if updateDB() or len(sys.argv) > 1:
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
        updates=[]
        for show in seasonedMappings:
            with open("mapping.csv", "a") as f:
                csv.writer(f, delimiter=";").writerow([show["title"], show["anilist_id"], show["id"], show["animeSeason"]])
                # If show is not in oldMapping
                if not any(d[1] == str(show["anilist_id"]) for d in oldMapping):
                    if show["type"] == "TV":
                        updates.append("Added " + show["title"] + " (" + str(show["anilist_id"]) + ") Season " + str(show["animeSeason"]))
                    elif show["type"] == "MOVIE":
                        updates.append("Added " + show["title"] + " (" + str(show["anilist_id"]) + ")")
        # If there are updates
        if len(updates) > 0:
            # Send updates to updateLog
            updateLog(updates)
            updateREADME()
    else:
        print("No changes, exiting")


if __name__ == "__main__":
    main()