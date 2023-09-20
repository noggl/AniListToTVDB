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
anime-list-full.json was last updated at 2023-09-20 11:34:54.661594

anime-offline-database.json was last updated at 2023-09-15 11:34:49.936629



Recent Updates:

- Added Akuma-kun (8194) Season 1
- Added Aqua Kids (108750) Season 1
- Added Bouken Yuuki Pluster World (3637) Season 1
- Added Croket! (5071) Season 1
- Added Dondon Dommel to Ron (2814) Season 1
- Added Dororon Enma-kun (1337) Season 1
- Added Eightman (5052) Season 1
- Added Flanders no Inu, Boku no Patrasche (2624) Season 1
- Added Fortune Quest L (3185) Season 1
- Added Gu-Gu Ganmo (3020) Season 1
- Added Hana no Ko Lunlun (2230) Season 1
- Added Himitsu no Akko-chan (3285) Season 1
- Added Himitsu no Akko-chan (3838) Season 2
- Added Ie Naki Ko (2829) Season 2
- Added Itoshi no Muco (21228) Season 1
- Added Jetter Mars (6087) Season 1
- Added Karakuri Kiden: Hiwou Senki (3935) Season 1
- Added Kasumin (2738) Season 2
- Added Kick no Oni (3870) Season 1
- Added Madou King Granzort (2818) Season 1
- Added Magnerobo Ga-Keen (3932) Season 1
- Added Maken Liner 0011 Henshin Seyo! (11269)
- Added Mirai Shounen Conan (Movie) (7308)
- Added Monster Strike the Movie: Lucifer - Zetsubou no Yoake (116962)
- Added Mori no Densetsu: Dai Ni Gakushou (103323)
- Added Mura Matsuri (6769)
- Added Nine: Original-ban (9242)
- Added Ochame na Futago: Claire Gakuin Monogatari (2570) Season 1
- Added Oishinbo (1093) Season 1
- Added Ookami Shounen Ken (17521) Season 1
- Added Pokemon (21356) Season 9
- Added Pokemon (97634) Season 10
- Added Pokemon: Pikachu to Eievui Friends (16678)
- Added Pokemon: Pikachu to Pokemon Ongakutai (21270)
- Added Pokemon: Pikachu, Kore Nan no Kagi? (21271)
- Added Pokemon: Pikapika Hoshizora Camp (4795)
- Added Popolocrois Monogatari (4191) Season 1
- Added Popolocrois Monogatari (592) Season 2
- Added Rainbow Sentai Robin (9438) Season 1
- Added Sarutobi Ecchan (6311) Season 1
- Added Shiawase Sou no Okojo-san (2934) Season 1
- Added Super Doll Licca-chan (2766) Season 1
- Added Takarajima (2618) Season 1
- Added Tenkuu Senki Shurato (2113) Season 1
- Added The Kabocha Wine (3159) Season 1
- Added Tongari Boushi no Memole (3754) Season 1
- Added Uchuusen Sagittarius (3317) Season 1
- Added Urayasu Tekkin Kazoku (2716) Season 1
- Added Vampiyan Kids (3290) Season 1
- Added Watashi no Ashinaga Ojisan (1375) Season 1
