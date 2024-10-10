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
anime-list-full.json was last updated at 2024-10-10 11:35:54.668406

anime-offline-database.json was last updated at 2024-10-09 11:36:11.717399



Recent Updates:

- Added Aharen-san wa Hakarenai (179979) Season 2
- Added Bleach (169755) Season 4
- Added Bye Bye, Earth (181078) Season 2
- Added Ishura (176234) Season 2
- Added Jibaku Shounen Hanako-kun (170892) Season 2
- Added Kaijuu 8-gou (178754) Season 2
- Added Kakkou no Iinazuke (179828) Season 2
- Added Kusuriya no Hitorigoto (176301) Season 2
- Added Medalist (165171) Season 1
- Added Sasaki to Pii-chan (176314) Season 2
- Added Sentai Daishikkaku (178781) Season 2
- Added Shoushimin Series (181182) Season 2
- Added Tate no Yuusha no Nariagari (173780) Season 4
- Added Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san (181641) Season 2
- Added Wind Breaker (178680) Season 2
