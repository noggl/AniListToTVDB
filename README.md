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
anime-list-full.json was last updated at 2025-07-16 11:39:43.314686

anime-offline-database.json was last updated at 2025-06-21 11:37:42.518331



Recent Updates:

- Added 9: Ruler's Crown (177761) Season 1
- Added Ame to Kimi to (180425) Season 1
- Added Aoi Kioku: Manmou Kaitaku to Shounen-tachi (17117)
- Added Arknights: Reimei Zensou (177175) Season 3
- Added Busamen Gachi Fighter (184575) Season 1
- Added Busu ni Hanataba wo. (156395) Season 1
- Added Clevatess: Majuu no Ou to Akago to Shikabane no Yuusha (178869) Season 1
- Added Dekin no Mogura (184574) Season 1
- Added Fermat no Ryouri (186003) Season 1
- Added Food Court de, Mata Ashita. (185519) Season 1
- Added Futari Solo Camp (185965) Season 1
- Added Game Center Shoujo to Ibunka Kouryuu (180794) Season 1
- Added Isekai Mokushiroku Mynoghra: Hametsu no Bunmei de Hajimeru Sekai Seifuku (178433) Season 1
- Added Jidou Hanbaiki ni Umarekawatta Ore wa Meikyuu wo Samayou (169440) Season 2
- Added Karaoke Iko! (183127) Season 1
- Added Kizetsu Yuusha to Ansatsu Hime (186561) Season 1
- Added Mattaku Saikin no Tantei to Kitara (180460) Season 1
- Added Muchuu sa, Kimi ni. (183128) Season 1
- Added Nyaight of the Living Cat (175124) Season 1
- Added Osomatsu-san (177880) Season 4
- Added Puniru wa Kawaii Slime (185755) Season 2
- Added Ruri no Houseki (180929) Season 1
- Added Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu (178090) Season 2
- Added Tougen Anki (177474) Season 1
- Added Tsuihousha Shokudou e Youkoso! (185544) Season 1
- Added Turkey! (159483) Season 1
- Added Utagoe wa Mille-Feuille (166215) Season 1
- Added Watashi ga Koibito ni Nareru Wake Nai jan, Muri Muri! (※Muri ja Nakatta!?) (184591) Season 1
- Added Zutaboro Reijou wa Ane no Moto Konyakusha ni Dekiai sareru (179879) Season 1
