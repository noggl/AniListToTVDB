# AniListToTVDB
Scripts to Find the TVDB ID of AniList Titles using anime-lists and AOD

<a href="https://www.buymeacoffee.com/noggl" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 25px !important;width: 110px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
### **Looking for the mapping.csv file? [Click here!](https://raw.githubusercontent.com/noggl/AniListToTVDB/main/mapping.csv)**
------------------------
## About
This came about because I couldn't find a way to relate AniList IDs to TVDB or TMDB IDs for my project [AniPlanrr](https://github.com/noggl/AniPlanrr). The matching could only be done by name, and that was not reliable enough. This script uses [Fribb's anime-lists](https://github.com/Fribb/anime-lists) and [manami-project's AOD](https://github.com/manami-project/anime-offline-database) to create a CSV file that can be used to relate AniList IDs to TVDB or TMDB IDs.

Both of these resources are .json files housed in the project's github repo, so this project downloads those files and parses them to create the CSV file.

## Requirements
- Python 3
- git

## Usage

Run the script with `python3 createCSV.py`. This will clone/update the github repos and create the `mappings.csv` to be used in a program like [AniPlanrr](https://github.com/noggl/AniPlanrr).

There are 2 available flags, `-f` and `-g`, which will force the creation of the CSV file or commit to github respectively. The first is useful for testing, the second is used in the github action that keeps this repo up to date.

## Status
anime-list-full.json was last updated at 2023-09-27 11:35:08.543749

anime-offline-database.json was last updated at 2023-09-27 11:35:10.410883



Recent Updates:

- Added AWOL (12951) Season 1
- Added Chou Kuse ni Narisou (2771) Season 1
- Added Don Chuck Monogatari (2575) Season 1
- Added Idol Tenshi Youkoso Youko (4928) Season 1
- Added Saa Ikou! Tamagotchi (6798) Season 1
- Added Saiko Robot Kombock (3772) Season 1
- Added Suzume no Tojimari (142770)
- Added Time Bokan 2000: Kaitou Kiramekiman (5475) Season 1
