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
anime-list-full.json was last updated at 2024-11-27 11:35:59.027086

anime-offline-database.json was last updated at 2024-11-23 11:35:46.174135



Recent Updates:

- Added Amrita no Kyouen (114606)
- Added Ashita Sekai ga Owaru toshitemo (104562)
- Added Blue Giant (140499)
- Added Blue Thermal (138379)
- Added Captain Bal (107857)
- Added Chuck Shimezou (107858)
- Added Garden of Remembrance (151017)
- Added Goodbye, Don Glees! (136302)
- Added Gridman Universe (142684)
- Added Haikyuu!! Movie: Gomisuteba no Kessen (153658)
- Added Hokkyoku Hyakkaten no Concierge-san (164226)
- Added Kitarou Tanjou: Gegege no Nazo (130622)
- Added Marudase Kintarou (118936)
- Added One Punch Man (153800) Season 3
- Added The iDOLM@STER Shiny Colors (175533) Season 2
- Added Yaneura no Rudger (142494)
- Added Yes ka No ka Hanbun ka (112930)
- Added Youkaiden Nekome Kozou (104327) Season 1
