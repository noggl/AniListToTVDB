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
anime-list-full.json was last updated at 2024-04-03 11:34:50.106650

anime-offline-database.json was last updated at 2024-04-03 11:34:51.796229



Recent Updates:

- Added Astro Note (171040) Season 1
- Added Bartender: Kami no Glass (155890) Season 1
- Added Blue Archive the Animation (160589) Season 1
- Added Blue Lock: Episode Nagi (163147)
- Added Bocchi the Rock! Movie (165253)
- Added Boku no Hero Academia (163139) Season 7
- Added Boukyaku Battery (TV) (167927) Season 1
- Added Cream Lemon: Lemon Angel (3205) Season 1
- Added Dead Dead Demons Dededede Destruction (146609)
- Added Dekisokonai to Yobareta Motoeiyuu wa Jikka kara Tsuihou sareta node Sukikatte ni Ikiru Koto ni Shita (166372) Season 1
- Added Doraemon: Kaette Kita Doraemon (Movie) (2651)
- Added Girls Band Cry (164212) Season 1
- Added Hananoi-kun to Koi no Yamai (165855) Season 1
- Added Henjin no Salad Bowl (166828) Season 1
- Added Highspeed Etoile (152302) Season 1
- Added Himitsu no AiPri (171080) Season 1
- Added Jiisan Baasan Wakagaeru (168138) Season 1
- Added Kaii to Otome to Kamikakushi (160090) Season 1
- Added Karasu wa Aruji wo Erabanai (170503) Season 1
- Added Kenka Dokugaku (174653) Season 1
- Added Kimetsu no Yaiba (166240) Season 5
- Added Kuramerukagari (171608)
- Added Kurayukaba (169778)
- Added Kuroshitsuji (166715) Season 4
- Added Lv2 kara Cheat datta Motoyuusha Kouho no Mattari Isekai Life (170130) Season 1
- Added Maou no Ore ga Dorei Elf wo Yome ni Shitanda ga, Dou Medereba Ii? (156023) Season 1
- Added Meitantei Conan Movie 27: 100-man Dollar no Michishirube (169754)
- Added Moeru! Oniisan (6067) Season 1
- Added Mushoku Tensei: Isekai Ittara Honki Dasu (166873) Season 4
- Added Nijiyon Animation (172242) Season 2
- Added One Room, Hiatari Futsuu, Tenshi-tsuki. (169927) Season 1
- Added Ooi! Tonbo (164440) Season 1
- Added Ookami to Koushinryou: Merchant Meets the Wise Wolf (145728) Season 1
- Added Re:Monster (169417) Season 1
- Added Rinkai! (163141) Season 1
- Added Sasayaku You ni Koi wo Utau (160181) Season 1
- Added Seiyuu Radio no Uraomote (159039) Season 1
- Added Sentai Daishikkaku (158417) Season 1
- Added Shinigami Bocchan to Kuro Maid (169584) Season 3
- Added Shinkalion: Change the World (172395) Season 1
- Added Shuumatsu Train Doko e Iku? (155657) Season 1
- Added Suki demo Kirai na Amanojaku (148080)
- Added Tadaima, Okaeri (169698) Season 1
- Added Tensei Kizoku, Kantei Skill de Nariagaru (164702) Season 1
- Added Tensei shitara Slime Datta Ken (156822) Season 4
- Added The Fable (166910) Season 1
- Added The New Gate (170890) Season 1
- Added Tonari no Youkai-san (146867) Season 1
- Added Touken Ranbu Kai: Kyoden Moyuru Honnouji (150085) Season 1
- Added Trapezium (171291)
- Added Uma Musume: Pretty Derby - Shin Jidai no Tobira (172420)
- Added Unnamed Memory (158709) Season 1
- Added Vampire Dormitory (170604) Season 1
- Added Yozakura-san Chi no Daisakusen (158898) Season 1
- Added Yuru Camp△ (155908) Season 4
- Added i☆Ris the Movie: Full Energy!! (156727)
