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
anime-list-full.json was last updated at 2023-08-30 11:34:49.990918

anime-offline-database.json was last updated at 2023-08-30 11:34:51.419192



Recent Updates:

- Added Akage no Anne: Green Gables e no Michi (8950)
- Added Bakumatsu no Spasibo (8092)
- Added Detective Conan: Haibara Ai Monogatari - Kurogane no Mystery Train (158997)
- Added Detective Conan: The Scarlet Alibi (131770)
- Added Gegege no Kitarou: Obake Nighter (8156)
- Added Hug tto! Precure (100661) Season 1
- Added Inu to Neko Docchi mo Katteru to Mainichi Tanoshii (116700) Season 1
- Added Ninja Batman (100248)
- Added Ryouma! The Prince of Tennis Shinsei Movie: Tennis no Ouji-sama (113254)
- Added Seishun Buta Yarou wa Randoseru Girl no Yume wo Minai (161474)
- Added Tennis no Oujisama: Atobe kara no Okurimono - Kimi ni Sasageru Tennis Prince Matsuri (814)
- Added Time Bokan (3915) Season 1
- Added Time Bokan Series: Gyakuten Ippatsuman (8011) Season 1
- Added Time Bokan Series: Yatterman (3008) Season 1
- Added Time Bokan Series: Zenderman (6889) Season 1
- Added X/1999 (155)
