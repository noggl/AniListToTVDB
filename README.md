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
anime-list-full.json was last updated at 2026-01-17 11:37:26.301373

anime-offline-database.json was last updated at 2025-06-21 11:37:42.518331



Recent Updates:

- Added All You Need Is Kill (187892)
- Added Ashita no Joe (Movie) (2920)
- Added Baton (6189)
- Added Boku no Kokoro no Yabai Yatsu Movie (182317)
- Added Chou Deneiban SD Gundam Sangokuden Brave Battle Warriors (8132)
- Added Doraemon Movie 01: Nobita no Kyouryuu (2645)
- Added Genius Party (3508)
- Added Girls & Panzer: Motto Love Love Sakusen desu! (188034)
- Added Hanarokushou ga Akeru Hi ni (177132)
- Added Kinnikuman II Sei: Second Generations (12279)
- Added Kono Hon wo Nusumu Mono wa (193923)
- Added Kouchuu Ouja Mushiking: Greatest Champion e no Michi (17469)
- Added Kouchuu Ouja Mushiking: Greatest Champion e no Michi (2173)
- Added Kusunoki no Bannin (189956)
- Added Kyojin no Hoshi: Chizome no Kesshousen (17443)
- Added Kyojin no Hoshi: Chizome no Kesshousen (17445)
- Added Kyojin no Hoshi: Chizome no Kesshousen (17447)
- Added Magical★Taruruuto-kun Movie (105193)
- Added Magical★Taruruuto-kun Movie (105195)
- Added Mahou Shoujo Lalabel: Umi ga Yobu Natsuyasumi (7807)
- Added Musha Knight Commando: SD Gundam Scramble (9087)
- Added Musha Knight Commando: SD Gundam Scramble (9098)
- Added Penguin no Mondai Movie (6063)
- Added SHORT PEACE (17677)
- Added Saishuu Gakushou Hibike! Euphonium (188035)
- Added Seishun Buta Yarou wa Yumemiru Shoujo no Yume wo Minai (104157)
- Added Tensei shitara Slime Datta Ken Movie 2: Soukai no Namida-hen (182206)
- Added Virgin Punk (181449)
- Added Wakusei Robo Danguard Ace tai Konchuu Robot Gundan (5515)
- Added Xevious (12799)
- Added Xiongmao Monogatari TaoTao (102460)
