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
anime-list-full.json was last updated at 2023-09-13 11:35:06.789644

anime-offline-database.json was last updated at 2023-09-12 11:34:56.346196



Recent Updates:

- Added Animal Yokochou (280) Season 1
- Added Hagane Orchestra (97608) Season 1
- Added Kagami no Kojou (145739)
- Added Kamiarizuki no Kodomo (118390)
- Added Kino no Tabi: The Beautiful World - Nanika wo Suru Tame ni - Life Goes On. (1379)
- Added Kobutori (1929) (5875)
- Added Laidbackers (104721)
- Added Manga Revue Haru (107670)
- Added Okusama wa Mahou Shoujo (614) Season 1
- Added Onegai My Melody (4114) Season 2
- Added Patalliro Saiyuuki! (1035) Season 1
- Added Pokemon: Meloetta no Kirakira Recital (13799)
- Added Sengoku Choujuu Giga: Kou (116053) Season 2
- Added Tezuka Osamu no Kyuuyaku Seisho Monogatari: In the Beginning (2282) Season 1
