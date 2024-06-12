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
anime-list-full.json was last updated at 2024-06-12 11:35:19.898781

anime-offline-database.json was last updated at 2024-06-11 11:35:22.500746



Recent Updates:

- Added 1000-nen Joou: Queen Millennia (1549)
- Added Ace wo Nerae! (1979) (313)
- Added Aikatsu! Movie (20640)
- Added Akihabara Dennou-gumi: 2011-nen no Natsuyasumi (2289)
- Added Alexander Senki Movie (5157)
- Added Alps no Shoujo Heidi: Alm no Yama-hen (9548)
- Added Alps no Shoujo Heidi: Alm no Yama-hen (9549)
- Added Ao Oni The Animation (Movie) (21898)
- Added Boku no Hero Academia: UA Heroes Battle (169402)
- Added Crayon Shin-chan Movie 23: Ora no Hikkoshi Monogatari - Saboten Daisuugeki (98744)
- Added Cure Miracle to Mofurun no Mahou Lesson (98785)
- Added Death Billiards (14353)
- Added Doraemon Movie 34: Shin Nobita no Daimakyou - Peko to 5-nin no Tankentai (19645)
- Added Dragon Quest: Dai no Daibouken (7435)
- Added Dragon Quest: Dai no Daibouken (7436)
- Added Dragon Quest: Dai no Daibouken (7364)
- Added Dragon Quest: Dai no Daibouken (7491)
- Added FLCL Alternative (21748)
- Added FLCL Alternative (21746)
- Added Fate/Zero Cafe (19165)
- Added Fate/kaleid liner Prisma☆Illya: Prisma☆Phantasm (100269)
- Added Gegege no Kitarou: Youkai Tokkyuu! Maboroshi no Kisha (8157)
- Added Gensoumaden Saiyuuki Movie: Requiem - Erabarezaru Mono e no Chinkonka (484)
- Added Gintama: Yorinuki Gintama-san on Theater 2D (20760)
- Added Glass no Chikyuu wo Sukue Unico Special (105255)
- Added Higashi no Eden: Air Communication (6927)
- Added Inazuma Eleven Go vs. Danball Senki W Movie (15785)
- Added Kaiketsu Zorori: Mamoru ze! Kyouryuu no Tamago (19587)
- Added Kindaichi Shounen no Jikenbo Movie 1: Operazakan - Aratanaru Satsujin (2077)
- Added Kindaichi Shounen no Jikenbo Movie 1: Operazakan - Aratanaru Satsujin (9154)
- Added Kirakira☆Precure A La Mode Movie: Paritto! Omoide no Mille-Feuille! (98891)
- Added Koro-sensei Q! (21864)
- Added Kouya no Kotobuki Hikoutai Kanzenban (115082)
- Added Kyojin no Hoshi (Movie) (17439)
- Added Lupin III: Pilot Film (5225)
- Added Lupin III: Pilot Film (97619)
- Added Lupin III: Pilot Film (107313)
- Added MiniPato (2733)
- Added Mouretsu Pirates: Abyss of Hyperspace (14817)
- Added Orange: Mirai (97669)
- Added Persona 4 the Animation: The Factor of Hope (14267)
- Added Pia Carrot e Youkoso!!: Sayaka no Koi Monogatari (216)
- Added Precure Super Stars! Movie (101101)
- Added Precure Super Stars! Movie (101908)
- Added Pretty Rhythm Movie: All Star Selection - Prism Show☆Best Ten (20581)
- Added Quanzhi Gaoshou: Dianfeng Rongyao (108981)
- Added Ribbon no Kishi (1999) (14249)
- Added Saenai Heroine no Sodatekata Fine (100675)
- Added Saint Seiya: Shinku no Shounen Densetsu (101499)
- Added Sekaiichi Hatsukoi Movie: Yokozawa Takafumi no Baai (20371)
- Added Sidonia no Kishi Movie (21154)
- Added Sore Ike! Anpanman: Utatte Teasobi! Anpanman to Mori no Takara (10685)
- Added Sore Ike! Anpanman: Utatte Teasobi! Anpanman to Mori no Takara (119784)
- Added Star Driver the Movie (12857)
- Added Star☆Twinkle Precure: Hoshi no Uta ni Omoi wo Komete (109737)
- Added Street Fighter Zero The Animation (979)
- Added Super Doll Licca-chan: Licca-chan Zettai Zetsumei! Doll Knights no Kiseki (10199)
- Added Toriko Movie: Bishokushin no Special Menu (17699)
- Added Tropical-Rouge! Precure Petit Tobikome! Collaboration ♡ Dance Party! (131045)
- Added Uchuu Kyoudai: Itten no Hikari (17573)
- Added Yuuki Yuuna wa Yuushabu Shozoku (97856)
- Added eX-Driver: Nina & Rei Danger Zone (1733)
- Added gdgd Fairies Movie: tte Iu Eiga wa Dou kana...? (20887)
