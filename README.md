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
anime-list-full.json was last updated at 2023-12-27 11:34:56.809128

anime-offline-database.json was last updated at 2023-12-27 11:34:59.604459



Recent Updates:

- Added 30-sai made Doutei dato Mahoutsukai ni Nareru Rashii (167087) Season 1
- Added Ao no Exorcist (158931) Season 3
- Added Bloody Escape: Jigoku no Tousou Geki (144770)
- Added Boku no Kokoro no Yabai Yatsu (166216) Season 2
- Added Bucchigiri?! (165254) Season 1
- Added Chiyu Mahou no Machigatta Tsukaikata (137908) Season 1
- Added Doraemon Movie 43: Nobita no Chikyuu Symphony (166976)
- Added Dungeon Meshi (153518) Season 1
- Added Gekkan Mousou Kagaku (169418) Season 1
- Added Harimaware! Koinu (169291) Season 1
- Added Hikari no Ou (162842) Season 2
- Added Himesama "Goumon" no Jikan desu (166522) Season 1
- Added Ishura (161476) Season 1
- Added Jaku-Chara Tomozaki-kun (143866) Season 2
- Added Kekkon Yubiwa Monogatari (160389) Season 1
- Added Kidou Senshi Gundam SEED Freedom (134761)
- Added Kingdom (155227) Season 5
- Added Kyuujitsu no Warumono-san (162002) Season 1
- Added Loop 7-kaime no Akuyaku Reijou wa, Moto Tekikoku de Jiyuu Kimama na Hanayome Seikatsu wo Mankitsu suru (168374) Season 1
- Added Mashle (166610) Season 2
- Added Mato Seihei no Slave (141821) Season 1
- Added Meiji Gekken: 1874 (171144) Season 1
- Added Meitou "Isekai no Yu" Kaitakuki: Around 40 Onsen Mania no Tensei Saki wa, Nonbiri Onsen Tengoku deshita (171019) Season 1
- Added Nozomanu Fushi no Boukensha (147642) Season 1
- Added Oomuro-ke (167984)
- Added Oroka na Tenshi wa Akuma to Odoru (164244) Season 1
- Added Pon no Michi (165314) Season 1
- Added Saijaku Tamer wa Gomi Hiroi no Tabi wo Hajimemashita. (156891) Season 1
- Added Saikyou Tank no Meikyuu Kouryaku: Tairyoku 9999 no Rare Skill-mochi Tank, Yuusha Party wo Tsuihou sareru (169935) Season 1
- Added Sasaki to Pii-chan (152682) Season 1
- Added Sengoku Youko (168194) Season 1
- Added Shaman King (2021) (147850) Season 2
- Added Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita (156131) Season 2
- Added Snack Basue (166093) Season 1
- Added Spy x Family Movie: Code: White (158928)
- Added Tsuki ga Michibiku Isekai Douchuu (139518) Season 2
- Added Urusei Yatsura (2022) (155645) Season 2
- Added Wonderful Precure! (171030) Season 1
- Added Yubisaki to Renren (166794) Season 1
- Added Yuuki Bakuhatsu Bang Bravern (165598) Season 1
