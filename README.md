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
anime-list-full.json was last updated at 2024-09-11 11:35:41.097277

anime-offline-database.json was last updated at 2024-09-11 11:35:42.816574



Recent Updates:

- Added Ai to Ken no Camelot: Mangaka Marina Time Slip Jiken (5931)
- Added Altered Carbon: Resleeved (115715)
- Added Aya to Majo (119321)
- Added Bakemonogatari (15689) Season 3
- Added Bakemonogatari (20593) Season 5
- Added Bakemonogatari (20918) Season 6
- Added Bakemonogatari (21745) Season 8
- Added Baki (2018) (97888) Season 1
- Added Bakugan Battle Brawlers (10330) Season 3
- Added BanG Dream! Garupa☆Pico (101632) Season 1
- Added BanG Dream! Garupa☆Pico (113906) Season 2
- Added BanG Dream! Garupa☆Pico (135171) Season 3
- Added BanG Dream! Morfonication (146501) Season 1
- Added BeyWarriors: Cyborg (102934) Season 1
- Added Blossom (13253)
- Added Bright: Samurai Soul (135432)
- Added Bubble (142455)
- Added Crusher Joe OVA (2696)
- Added Daishizen no Majuu: Bagi (2312)
- Added Dororo (11471)
- Added Elmer no Bouken: My Father`s Dragon (6593)
- Added Exper Zenon (10463)
- Added Fate/Grand Order × Himuro no Tenchi: 7-nin no Saikyou Ijin-hen (100729) Season 1
- Added Hare Tokidoki Buta (107618) Season 1
- Added Hitori no Shita: The Outcast (98574) Season 2
- Added Hora, Mimi ga Mieteru yo! Season 2 (107984) Season 1
- Added I: Wish You Were Here (1156) Season 1
- Added Ikki Tousen (105391) Season 5
- Added Jikken-hin Kazoku: Creatures Family Days (98477) Season 1
- Added JoJo no Kimyou na Bouken (2012) (131942) Season 6
- Added Kara no Kyoukai: Mirai Fukuin - Extra Chorus (20697)
- Added Kennosuke-sama (18603)
- Added Kud Wafter (104749)
- Added Kumo no You ni Kaze no You ni (1032)
- Added Kyoufu no Bio Ningen Saishuu Kyoushi (2780)
- Added Lily C.A.T. (3258)
- Added Magia Record: Mahou Shoujo Madoka★Magica Gaiden (136080) Season 3
- Added Nils no Fushigi na Tabi (Movie) (7664)
- Added Otona no Bouguya-san (104308) Season 1
- Added Otona no Bouguya-san (124136) Season 2
- Added PSYCHO-PASS 3 FIRST INSPECTOR (113917)
- Added Re:Zero kara Hajimeru Isekai Seikatsu (2018) (100049)
- Added Robot Girls Z (19799) Season 1
- Added Ryuu no Haisha (87539) Season 1
- Added SOUND & FURY (111932)
- Added Sango Shou Densetsu: Aoi Umi no Elfie (5014)
- Added Science Saru x MBS Original Short Anime Daisakusen! (174666) Season 1
- Added Seimei no Kagaku: Micro Patrol (3624) Season 1
- Added Self Portrait (8647)
- Added Semiwa Magic Cube (118199) Season 1
- Added Semiwa Magic Cube (118200) Season 2
- Added Shingeki no Kyojin (146984) Season 7
- Added Shiranpuri (Movie) (13175)
- Added Shuranosuke Zanmaken: Shikamamon no Otoko (1451)
- Added Sono Bisque Doll wa Koi wo Suru (154768) Season 2
- Added Strike Witches: Operation Victory Arrow (20650)
- Added Tekken (537)
- Added Tenjou Tenge: The Past Chapter (760)
- Added Thermae Romae (12321) Season 1
- Added Uchuu Senkan Yamato: Aratanaru Tabidachi (3071)
- Added Upotte!! (12317) Season 1
- Added ZENONZARD THE ANIMATION (112033) Season 1
