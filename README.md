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
anime-list-full.json was last updated at 2023-07-19 11:34:42.623728

anime-offline-database.json was last updated at 2023-07-13 11:35:16.848251



Recent Updates:

- Added Accel World: Infinite∞Burst (21404)
- Added Ai no Utagoe wo Kikasete (123899)
- Added Ame wo Tsugeru Hyouryuu Danchi (139643)
- Added Bakuten!! Movie (136064)
- Added BanG Dream! It's MyGO!!!!! (163571) Season 1
- Added Bem Movie: Become Human (119258)
- Added BeyWarriors: Cyborg (102934) Season 1
- Added Boku ga Aishita Subete no Kimi e (139310)
- Added Bungou Stray Dogs (163263) Season 5
- Added Chouon Senshi Borgman (3035) Season 1
- Added Cider no You ni Kotoba ga Wakiagaru (107625)
- Added Dark Gathering (152802) Season 1
- Added Delicious Party♡Precure Movie: Yume Miru Oko-sama Lunch! (144687)
- Added Detective Conan Movie 25: Halloween no Hanayome (142219)
- Added Doraemon Movie 41: Nobita no Little Star Wars (126783)
- Added Dragon Ball Z Movie 10: Kiken na Futari! Super Senshi wa Nemurenai (903)
- Added Eiga Daisuki Pompo-san (99900)
- Added Entotsu Machi no Poupelle (98776)
- Added Fate/kaleid liner Prisma☆Illya Movie: Licht - Namae no Nai Shoujo (118743)
- Added Goblin Slayer: Goblin's Crown (108623)
- Added Healin' Good♡Precure Movie: Yume no Machi de Kyun! Tto GoGo! Dai Henshin!! (121026)
- Added Hula Fulla Dance (125841)
- Added Inu-Ou (109928)
- Added Isekai Quartet Movie: Another World (117074)
- Added Kidou Senshi Gundam: Cucuruz Doan no Shima (139273)
- Added Kidou Senshi Gundam: Twilight Axis - Akaki Zanei (104557)
- Added Kimi wa Kanata (116226)
- Added Kimi wo Aishita Hitori no Boku e (139311)
- Added Koukaku Kidoutai: SAC_2045 - Jizoku Kanou Sensou (138899)
- Added Luo Xiao Hei Zhan Ji (Movie) (112023)
- Added Manaria Friends (21322) Season 1
- Added Meitantei Conan: Hannin no Hanzawa-san (140005) Season 1
- Added Nakitai Watashi wa Neko wo Kaburu (114963)
- Added Nanatsu no Bitoku (100644) Season 1
- Added Natsu e no Tunnel, Sayonara no Deguchi (142769)
- Added Omoi, Omoware, Furi, Furare (109125)
- Added Pokemon Movie 01: Mewtwo no Gyakushuu (528)
- Added Pokemon Movie 03: Kesshoutou no Teiou Entei (1118)
- Added Pokemon Movie 04: Celebi Toki wo Koeta Deai (1119)
- Added Pokemon Movie 09: Pokemon Ranger to Umi no Ouji Manaphy (2201)
- Added Pokemon Movie 10: Dialga vs. Palkia vs. Darkrai (2847)
- Added Pokemon Movie 15: Kyurem vs. Seikenshi (12671)
- Added Pokemon Movie 17: Hakai no Mayu to Diancie (20644)
- Added Pokemon Movie 18: Ring no Choumajin Hoopa (21266)
- Added Pokemon Movie 23: Koko (114564)
- Added Precure Miracle Leap Movie: Minna to no Fushigi na Ichinichi (112612)
- Added Rail Romanesque (114263) Season 1
- Added Shika no Ou: Yuna to Yakusoku no Tabi (102891)
- Added Summer Ghost (130050)
- Added Umibe no Étranger (112788)
- Added Watashi ni Tenshi ga Maiorita! Precious Friends (126425)
