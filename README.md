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
anime-list-full.json was last updated at 2025-01-01 11:35:51.306151

anime-offline-database.json was last updated at 2024-12-25 11:36:02.805395



Recent Updates:

- Added A-Rank Party wo Ridatsu shita Ore wa, Moto Oshiego-tachi to Meikyuu Shinbu wo Mezasu. (180812) Season 1
- Added Akuyaku Reijou Tensei Ojisan (172453) Season 1
- Added Ameku Takao no Suiri Karte (176642) Season 1
- Added Around 40 Otoko no Isekai Tsuuhan (180292) Season 1
- Added Babanbabanban Vampire (175422) Season 1
- Added BanG Dream! Ave Mujica (169295) Season 1
- Added Bokura no Nanokakan Sensou (101610)
- Added Botsuraku Yotei no Kizoku dakedo, Hima Datta kara Mahou wo Kiwametemita (176063) Season 1
- Added Cardfight!! Vanguard (182920) Season 11
- Added Class no Daikirai na Joshi to Kekkon suru Koto ni Natta. (178462) Season 1
- Added Doraemon Movie 44: Nobita no E Sekai Monogatari (182333)
- Added Douse, Koishite Shimaunda. (175409) Season 1
- Added Farmagia (178312) Season 1
- Added Fate/strange Fake (166617) Season 1
- Added Fuguushoku "Kanteishi" ga Jitsu wa Saikyou Datta (178548) Season 1
- Added Grisaia: Phantom Trigger (145740) Season 1
- Added Guild no Uketsukejou desu ga, Zangyou wa Iya nanode Boss wo Solo Toubatsu Shiyou to Omoimasu (167143) Season 1
- Added Hana wa Saku, Shura no Gotoku (178022) Season 1
- Added Hazure Skill "Kinomi Master": Skill no Mi (Tabetara Shinu) wo Mugen ni Taberareru You ni Natta Ken ni Tsuite (178100) Season 1
- Added Honey Lemon Soda (175443) Season 1
- Added Inazuma Eleven: Aratanaru Eiyuu-tachi no Joshou (180806)
- Added Inazuma Eleven: Soushuuhen Densetsu no Kickoff (180804)
- Added Izure Saikyou no Renkinjutsushi? (177506) Season 1
- Added Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo (172258) Season 2
- Added Kimi to Idol Precure♪ (185073) Season 1
- Added Kinnikuman: Kanpeki Chоujin Shiso-hen (181886) Season 2
- Added Kisaki Kyouiku kara Nigetai Watashi (170650) Season 1
- Added Kono Kaisha ni Suki na Hito ga Imasu (179696) Season 1
- Added Kuroiwa Medaka ni Watashi no Kawaii ga Tsuujinai (177552) Season 1
- Added Magic Maker: Isekai Mahou no Tsukurikata (179297) Season 1
- Added Mahoutsukai Precure! (162722) Season 2
- Added Mahoutsukai no Yakusoku (170916) Season 1
- Added Make a Girl (154064)
- Added Mashin Souzouden Wataru (173333) Season 1
- Added Momentary Lily (177159) Season 1
- Added NEET Kunoichi to Nazeka Dousei Hajimemashita (174654) Season 1
- Added Nihon e Youkoso Elf-san. (172439) Season 1
- Added Okinawa de Suki ni Natta Ko ga Hougen Sugite Tsurasugiru (166699) Season 1
- Added Ore dake Level Up na Ken (176496) Season 2
- Added Oshiri Tantei Movie 6: Star and Moon (185643)
- Added Project Sekai Movie: Kowareta Sekai to Utaenai Miku (179878)
- Added S-Rank Monster no "Behemoth" dakedo, Neko to Machigawarete Elf Musume no Pet toshite Kurashitemasu (176158) Season 1
- Added Sakamoto Days (177709) Season 1
- Added Salaryman ga Isekai ni Ittara Shitennou ni Natta Hanashi (179689) Season 1
- Added Senpai wa Otokonoko Movie: Ame Nochi Hare (182158)
- Added Sentai Red Isekai de Boukensha ni Naru (180052) Season 1
- Added Sorairo Utility (TV) (174596) Season 1
- Added Sousei no Aquarion: Myth of Emotions (162921) Season 1
- Added Tasokare Hotel (178495) Season 1
- Added UniteUp! (167742) Season 2
- Added Unnamed Memory (178550) Season 2
- Added Versailles no Bara (Movie) (154392)
- Added Watashi no Shiawase na Kekkon (169441) Season 2
- Added Zenshuu. (176273) Season 1
- Added Übel Blatt (175198) Season 1
