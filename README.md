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
anime-list-full.json was last updated at 2024-06-26 11:35:23.612734

anime-offline-database.json was last updated at 2024-06-26 11:35:25.223161



Recent Updates:

- Added "Oshi no Ko" (166531) Season 2
- Added 2.5-jigen no Ririsa (158559) Season 1
- Added Atri: My Dear Moments (154963) Season 1
- Added Bakeneko Anzu-chan (158641)
- Added Boku no Hero Academia the Movie 4: You're Next (168013)
- Added Boku no Tsuma wa Kanjou ga Nai (175450) Season 1
- Added Bye Bye, Earth (157371) Season 1
- Added Crayon Shin-chan Movie 32: Ora-tachi no Kyouyuu Nikki (171145)
- Added Delico's Nursery (167991) Season 1
- Added Dungeon no Naka no Hito (168345) Season 1
- Added Elf-san wa Yaserarenai. (173388) Season 1
- Added Fairy Tail: 100-nen Quest (139095) Season 1
- Added Giji Harem (163623) Season 1
- Added Gintama on Theater 2D: Baragaki-hen (169000)
- Added Grendizer U (154195) Season 1
- Added Harimaware! Koinu (176283) Season 2
- Added Hazurewaku no "Joutai Ijou Skill" de Saikyou ni Natta Ore ga Subete wo Juurin suru made (173694) Season 1
- Added Isekai Suicide Squad (166710) Season 1
- Added Isekai Yururi Kikou: Kosodateshinagara Boukensha Shimasu (171031) Season 1
- Added Katsute Mahou Shoujo to Aku wa Tekitai shiteita. (170938) Season 1
- Added Kimi no Iro (158166)
- Added Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen (139825) Season 2
- Added Kinnikuman: Kanpeki Chоujin Shiso-hen (162796) Season 1
- Added Koi wa Futago de Warikirenai (167144) Season 1
- Added Look Back (174788)
- Added Madougushi Dahliya wa Utsumukanai (168623) Season 1
- Added Make Heroine ga Oosugiru! (171457) Season 1
- Added Maougun Saikyou no Majutsushi wa Ningen datta (173584) Season 1
- Added Mayonaka Punch (174044) Season 1
- Added Megami no Café Terrace (166477) Season 2
- Added Mob kara Hajimaru Tansaku Eiyuutan (172416) Season 1
- Added Mononoke Movie: Karakasa (151117)
- Added Na Nare Hana Nare (170891) Season 1
- Added Naze Boku no Sekai wo Daremo Oboeteinai no ka? (167419) Season 1
- Added NieR:Automata Ver1.1a (167420) Season 2
- Added Nige Jouzu no Wakagimi (162896) Season 1
- Added Ore wa Subete wo "Parry" suru: Gyaku Kanchigai no Sekai Saikyou wa Boukensha ni Naritai (170695) Season 1
- Added Patalliro! Stardust Keikaku (12663)
- Added Raiyantsuuri no Uta (9959)
- Added Ramen Akaneko (170998) Season 1
- Added Senpai wa Otokonoko (163133) Season 1
- Added Shikanoko Nokonoko Koshitantan (175977) Season 1
- Added Shinmai Ossan Boukensha, Saikyou Party ni Shinu hodo Kitaerarete Muteki ni Naru. (163292) Season 1
- Added Shoushimin Series (173295) Season 1
- Added Shy (171748) Season 2
- Added SutoPuri Movie: Hajimari no Monogatari - Strawberry School Festival!!! (176319)
- Added Tasogare Out Focus (166700) Season 1
- Added Tasuuketsu (174070) Season 1
- Added Tensui no Sakuna-hime (175868) Season 1
- Added Tsue to Tsurugi no Wistoria (174576) Season 1
- Added VTuber Nandaga Haishin Kiri Wasuretara Densetsu ni Natteta (160488) Season 1
- Added Wonderful Precure! Movie (169403)
- Added Zegapain: STA (168998)
