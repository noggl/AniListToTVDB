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
anime-list-full.json was last updated at 2023-10-04 11:35:10.474597

anime-offline-database.json was last updated at 2023-09-28 11:34:50.846335



Recent Updates:

- Added Alice to Therese no Maboroshi Koujou (136149)
- Added Arknights: Reimei Zensou (158895) Season 2
- Added Atarashii Joushi wa Do Tennen (165070) Season 1
- Added Beyblade X (165159) Season 1
- Added Bikkurimen (163364) Season 1
- Added Biohazard: Death Island (161441)
- Added Bokura no Ameiro Protocol (166896) Season 1
- Added Boukensha ni Naritai to Miyako ni Deteitta Musume ga S-Rank ni Natteta (156184) Season 1
- Added Boushoku no Berserk (156039) Season 1
- Added Bullbuster (157399) Season 1
- Added Buta no Liver wa Kanetsu Shiro (142599) Season 1
- Added Captain Tsubasa (2018) (163024) Season 2
- Added City Hunter Movie: Tenshi no Namida (147189)
- Added Crayon Shin-chan Movie 31: Chounouryoku Daikessen - Tobe Tobe Temakizushi (158595)
- Added Dead Mount Death Play (162803) Season 2
- Added Dog Signal (160514) Season 1
- Added Dr. Stone (162670) Season 4
- Added FLCL: Grunge (146472) Season 1
- Added FLCL: Grunge (146473) Season 2
- Added Hibike! Euphonium: Ensemble Contest-hen (150429)
- Added Hikikomari Kyuuketsuki no Monmon (159808) Season 1
- Added Hoshikuzu Telepath (155419) Season 1
- Added Houkago Shounen Hanako-kun (159074) Season 1
- Added Hypnosis Mic: Division Rap Battle - Rhyme Anima (163140) Season 2
- Added Kamonohashi Ron no Kindan Suiri (158926) Season 1
- Added Kawagoe Boys Sing (162209) Season 1
- Added Kibou no Chikara: Otona Precure '23 (162720) Season 1
- Added Kikansha no Mahou wa Tokubetsu desu (163142) Season 1
- Added Kimitachi wa Dou Ikiru ka (109979)
- Added Kinpatsu no Jeanie (6012) Season 1
- Added Kizuna no Allele (166523) Season 2
- Added MF Ghost (143327) Season 1
- Added Mahou no Angel Sweet Mint (2040) Season 1
- Added Mahou no Mako-chan (4113) Season 1
- Added Mahoutsukai no Yome (166452) Season 3
- Added Matsuinu (169227) Season 1
- Added Megumi no Daigo: Kyuukoku no Orange (158791) Season 1
- Added Migi to Dali (142666) Season 1
- Added Nanatsu no Taizai: Mokushiroku no Yonkishi (148862) Season 1
- Added Noel no Fushigi na Bouken (9303)
- Added Ojou to Banken-kun (155527) Season 1
- Added Osomatsu-san: Tamashii no Takoyaki Party to Densetsu no Otomarikai (135178)
- Added Overtake! (160515) Season 1
- Added Paradox Live the Animation (150077) Season 1
- Added Precure All Stars Movie F (159429)
- Added Rail Romanesque (127163) Season 2
- Added Saihate no Paladin (143085) Season 2
- Added Sand Land (158896)
- Added Sasaki to Miyano Movie: Sotsugyou-hen (146743)
- Added Seijo no Maryoku wa Bannou desu (146206) Season 2
- Added Seiken Gakuin no Makentsukai (140501) Season 1
- Added Shangri-La Frontier: Kusoge Hunter, Kamige ni Idoman to su (151970) Season 1
- Added Spy x Family (158927) Season 3
- Added The iDOLM@STER Million Live! (120755) Season 1
- Added The iDOLM@STER Shiny Colors (162889) Season 1
- Added Tokyo Revengers (163329) Season 3
- Added Uma Musume: Pretty Derby (156632) Season 3
- Added Under Ninja (138788) Season 1
- Added Watashi no Oshi wa Akuyaku Reijou. (158704) Season 1
- Added Yuzuki-san Chi no Yonkyoudai. (164312) Season 1
