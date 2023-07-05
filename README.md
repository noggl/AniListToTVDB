# AniListToTVDB
Scripts to Find the TVDB ID of AniList Titles using anime-lists and AOD
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
anime-list-full.json was last updated at 2023-07-05 11:35:44.393856

anime-offline-database.json was last updated at 2023-07-01 11:34:55.016923



Recent Updates:

- Added Ayaka (155982) Season 1
- Added Bleach (159322) Season 3
- Added Hataraku Maou-sama! (155168) Season 3
- Added Helck (145140) Season 1
- Added Horimiya: Piece (163132) Season 1
- Added Kanojo, Okarishimasu (154745) Season 3
- Added Liar Liar (131863) Season 1
- Added Mushoku Tensei: Isekai Ittara Honki Dasu (146065) Season 3
- Added Nanatsu no Maken ga Shihai suru (142598) Season 1
- Added Rurouni Kenshin: Meiji Kenkaku Romantan (2023) (142877) Season 1
- Added Shinigami Bocchan to Kuro Maid (139435) Season 2
- Added Spy Kyoushitsu (163542) Season 2
- Added Suki na Ko ga Megane wo Wasureta (160188) Season 1
- Added Temple (160447) Season 1
- Added Yumemiru Danshi wa Genjitsushugisha (157397) Season 1
- Added Zom 100: Zombie ni Naru made ni Shitai 100 no Koto (159831) Season 1
