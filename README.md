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
anime-list-full.json was last updated at 2025-04-02 11:36:16.663049

anime-offline-database.json was last updated at 2025-03-25 11:36:07.532445



Recent Updates:

- Added #Compass 2.0: Sentou Setsuri Kaiseki System (158287) Season 1
- Added Anne Shirley (184639) Season 1
- Added Apocalypse Hotel (180675) Season 1
- Added Araiguma Calcal-dan (186522) Season 1
- Added Aru Majo ga Shinu Made (178701) Season 1
- Added Ballpark de Tsukamaete! (184279) Season 1
- Added Boku to Roboko Movie (166249)
- Added Chotto dake Ai ga Omoi Dark Elf ga Isekai kara Oikaketekita (180829) Season 1
- Added Chuuzenji-sensei Mononoke Kougiroku: Sensei ga Nazo wo Hodoite Shimau kara. (182419) Season 1
- Added Classic★Stars (178825) Season 1
- Added Dandadan (185660) Season 2
- Added Docchi ni Suru? (6797)
- Added Dungeon Meshi (178031) Season 2
- Added Enen no Shouboutai (149118) Season 3
- Added Gachiakuta (178025) Season 1
- Added Gorilla no Kami kara Kago sareta Reijou wa Ouritsu Kishidan de Kawaigarareru (182060) Season 1
- Added Grisaia: Phantom Trigger The Animation (99470)
- Added Guilty Gear Strive: Dual Rulers (178046) Season 1
- Added Haite Kudasai, Takamine-san (179965) Season 1
- Added Hana-Doll*: Reinterpretation of Flowering (166371) Season 1
- Added Hibi wa Sugiredo Meshi Umashi (185939) Season 1
- Added Isshun de Chiryou shiteita noni Yakutatazu to Tsuihou sareta Tensai Chiyushi, Yami Healer toshite Tanoshiku Ikiru (175872) Season 1
- Added Jigokuraku (166613) Season 2
- Added Kaitou Queen no Yuuga na Vacances (162682)
- Added Kakushite! Makina-san!! (177509) Season 1
- Added Kanchigai no Atelier Meister: Eiyuu Party no Moto Zatsuyougakari ga, Jitsu wa Sentou Igai ga SSS Rank Datta to Iu Yoku Aru Hanashi (183133) Season 1
- Added Kanpekisugite Kawaige ga Nai to Konyaku Haki sareta Seijo wa Ringoku ni Urareru (183275) Season 1
- Added Katainaka no Ossan, Kensei ni Naru (179955) Season 1
- Added Kidou Senshi Gundam: GQuuuuuuX (185213) Season 1
- Added Kijin Gentoushou (143598) Season 1
- Added Komatsu Sakyou Anime Gekijou (98450) Season 1
- Added Koupen-chan (185646) Season 1
- Added Kowloon Generic Romance (182814) Season 1
- Added Kuroshitsuji (179054) Season 5
- Added Lazarus (167336) Season 1
- Added Maebashi Witches (180825) Season 1
- Added Meitantei Conan Movie 28: Sekigan no Flashback (185212)
- Added Miru: Watashi no Mirai (166373) Season 1
- Added Mono (176246) Season 1
- Added Nazotoki wa Dinner no Ato de (184989) Season 1
- Added Ninja to Koroshiya no Futarigurashi (177120) Season 1
- Added Nmeneko (186313) Season 1
- Added Ore wa Seikan Kokka no Akutoku Ryoushu! (183274) Season 1
- Added Princession Orchestra (178052) Season 1
- Added Rock wa Lady no Tashinami deshite (179694) Season 1
- Added Saikyou no Ousama, Nidome no Jinsei wa Nani wo Suru? (183161) Season 1
- Added Seirei Tsukai (1866)
- Added Shin Samurai-den Yaiba (177476) Season 1
- Added Shirobuta Kizoku desu ga Zense no Kioku ga Haeta node Hiyoko na Otouto Sodatemasu (179541) Season 1
- Added Shiunji-ke no Kodomotachi (174802) Season 1
- Added Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita (143337) Season 2
- Added Summer Pockets (143200) Season 1
- Added Tabekko Doubutsu The Movie (180124)
- Added Tenjouhen: Utsunomiko (5922)
- Added Tensei shitara Slime Datta Ken (182205) Season 5
- Added Teogonia (176702) Season 1
- Added Tsue to Tsurugi no Wistoria (182300) Season 2
- Added Uchuujin MuuMuu (185070) Season 1
- Added Uma Musume: Cinderella Gray (180516) Season 1
- Added Uta no☆Prince-sama♪ Movie: Taboo Night Kisses (172393)
- Added Utsunomiko (5921)
- Added Vigilante: Boku no Hero Academia Illegals (185736) Season 1
- Added Virgin Punk (181449)
- Added Witch Watch (180367) Season 1
- Added Yofukashi no Uta (175914) Season 2
- Added Youjo Senki (135865) Season 2
- Added Your Forma (167142) Season 1
- Added Zatsu Tabi: That's Journey (165445) Season 1
