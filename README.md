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
anime-list-full.json was last updated at 2024-10-02 11:36:04.588806

anime-offline-database.json was last updated at 2024-10-01 11:36:12.110149



Recent Updates:

- Added Ani ni Tsukeru Kusuri wa Nai! (120046) Season 4
- Added Beyblade Burst (108853) Season 4
- Added Boku no Hero Academia: UA Heroes Battle (169402)
- Added Byulbyul Iyagi 2 (9447)
- Added City Hunter: Hyakuman Dollar no Inbou (1476)
- Added Doraemon: The Day When I Was Born (2652)
- Added Fate/kaleid liner Prisma☆Illya: Prisma☆Phantasm (100269)
- Added Fragtime (108487)
- Added Gyo (10417)
- Added Hibike! Euphonium: Ensemble Contest-hen (150429)
- Added Kick-Heart (16149)
- Added Kizumonogatari: Koyomi Vamp (181970)
- Added Little Witch Academia: Mahoujikake no Parade (19489)
- Added Nanatsu no Taizai (21385) Season 2
- Added Osomatsu-san: Tamashii no Takoyaki Party to Densetsu no Otomarikai (135178)
- Added Pastel Life (101596) Season 1
- Added Pokemon: Pikachu to Eevee Friends (16678)
- Added Pokemon: Pikachu, Kore Nan no Kagi? (21271)
- Added Psychic Academy (337) Season 1
- Added Ribbon no Kishi (1999) (14249)
- Added Seitokai no Ichizon (5909) Season 1
- Added Super Shiro (107993) Season 1
- Added Teki wa Kaizoku: Neko-tachi no Kyouen (2679) Season 1
- Added To Be Hero (97616) Season 1
- Added Waza no Tabibito (10904)
- Added eX-Driver: Nina & Rei Danger Zone (1733)
