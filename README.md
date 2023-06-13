# AniListToTVDB
Scripts to Find the TVDB ID of AniList Titles using XEM and AOD

## About
This came about because I couldn't find a way to relate AniList IDs to TVDB IDs for my project [AniPlanrr](https://github.com/noggl/AniPlanrr). The matching could only be done by name, and that was not reliable enough. This script uses the [XEM](https://thexem.info/) and [AOD](https://github.com/manami-project/anime-offline-database) to first link AniDB IDs to TVDB IDs (using XEM), and then replace the AniDB IDs with AniList IDs (using AOD).

There is an API for XEM, but it did not seem to be possible to get TVDB IDs when providing an AniDB ID, or an AniDB ID when providing a TVDB ID, so I had to scrape the website. This is not ideal, but it works. If the [API is updated to allow this](https://github.com/thezoggy/xem/issues/5), I will update the script to use it.

AOD is an offline database, so the script just downloads the .json file from the master branch and reads it.

## Requirements
- Python 3
- [Requests](https://pypi.org/project/requests/)
- [wget](https://pypi.org/project/wget/)
- [os](https://docs.python.org/3/library/os.html)
- [json](https://docs.python.org/3/library/json.html)
- [csv](https://docs.python.org/3/library/csv.html)
To install the requirements, run `pip install -r requirements.txt`

## Usage

**YOU SHOULD NOT NEED TO RUN THESE SCRIPTS!! I WILL PROVIDE THE `mappings.csv` FILE IN THE REPO. RUNNING THE SCRIPTS WILL HIT THE XEM WEBSITE, AND I DON'T WANT TO OVERLOAD IT. IF YOU THINK SOMETHING IS OUT OF DATE, PLEASE OPEN AN ISSUE.**

There are 2 parts to this process, getting the data from XEM and then relating it to AniList IDs using AOD. To do the first part, run `python3 scrape.py`. This will create a file called `XEM.json` which contains the data from XEM.

To relate the data to AniList IDs, run `python3 createCSV.py`. This will create a file called `mappings.csv` which contains the data from XEM, but with AniList IDs instead of AniDB IDs. This will take a while, as it has to download the AOD file and read it. The `mappings.csv` can then be used in a program like [AniPlanrr](https://github.com/noggl/AniPlanrr).
