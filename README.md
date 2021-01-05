# README #
Tiny Audio Cataloguer is a small Python3 tool useful to catalogue and organize audio file based on embedded meta tags such as artist, album and track.


### Dependencies ###

[tinytag](https://pypi.org/project/tinytag/)

`pip3 install tinytag`


### Usage ###

`python3 audio-cataloguer.py -p <path_to_files> [-q]`


### Options ###

* -p: select path to file to be cataloged
* -q: quite mode, do not print step-by-step logs


### Usage Example ###

* Dir tree before running tool

```
tree ~/Desktop/recover_audio                                                                                                                                                                     ✔  15:52:37 
~/Desktop/recover_audio
├── f105153401.mp3
├── f111315311.mp3
├── f120180455.mp3
├── f129107367.mp3
├── f129172327.mp3
├── f134176615.mp3
├── f134209383.m3u
├── f134274919.mp3
├── f134307687.mp3
├── f134373223.jpg
├── f136947255.mp3
├── f136979999.mp3
├── f137012767.mp3
├── f137045535.mp3
├── f137078303.mp3
├── f137111071.mp3
├── f137143839.mp3
├── f137176607.mp3
├── f137209375.mp3
├── f137242143.mp3
├── f137307679.mp3
├── f137340447.m3u
├── f137373215.mp3
├── f137405983.mp3
├── f137438751.jpg
├── f137471519.mp3
├── f137504287.mp3
├── f137537055.mp3
├── f137569823.mp3
├── f137602591.mp3
├── f137635359.mp3
├── f137668127.mp3
├── f137700895.mp3
├── f137733663.mp3
├── f137766431.mp3
├── f137831967.mp3
├── f137864735.mp3
├── f137897503.mp3
├── f137930271.mp3
├── f137963039.mp3
├── f137995807.mp3
├── f138028575.mp3
├── f138061343.mp3
├── f138094111.mp3
└── f138126879.mp3

0 directories, 45 files
```

* Run Tiny Audio Cataloguer

```
python3 audio-cataloguer.py -p ~/Desktop/recover_audio/ -q                                                                                                                                       ✔  15:56:02 
Stating tag scanning...
...Done!
Starting file cataloguing...
...Done!
```

* Dir tree after running tool

```
tree ~/Desktop/recover_audio                                                                                                                                                                     ✔  16:03:25 
~/Desktop/recover_audio
├── Arcade\ Fire
│   ├── Funeral
│   │   ├── 01_f138094111.mp3
│   │   └── 09_f138126879.mp3
│   └── Neon\ Bible
│       ├── 01_f137995807.mp3
│       ├── 02_f137831967.mp3
│       ├── 03_f138028575.mp3
│       ├── 04_f138061343.mp3
│       ├── 05_f137963039.mp3
│       ├── 06_f137700895.mp3
│       ├── 07_f137766431.mp3
│       ├── 08_f137864735.mp3
│       ├── 09_f137733663.mp3
│       ├── 10_f137897503.mp3
│       └── 11_f137930271.mp3
├── The\ Offspring
│   └── Americana
│       ├── 01_f137143839.mp3
│       ├── 01_f137668127.mp3
│       ├── 02_f129172327.mp3
│       ├── 02_f137242143.mp3
│       ├── 03_f137111071.mp3
│       ├── 03_f137635359.mp3
│       ├── 04_f134176615.mp3
│       ├── 04_f137307679.mp3
│       ├── 05_f136979999.mp3
│       ├── 05_f137504287.mp3
│       ├── 06_f137078303.mp3
│       ├── 06_f137602591.mp3
│       ├── 07_f136947255.mp3
│       ├── 07_f137471519.mp3
│       ├── 08_f120180455.mp3
│       ├── 08_f137209375.mp3
│       ├── 09_f134274919.mp3
│       ├── 09_f137373215.mp3
│       ├── 10_f134307687.mp3
│       ├── 10_f137405983.mp3
│       ├── 11_f137045535.mp3
│       ├── 11_f137569823.mp3
│       ├── 12_f137012767.mp3
│       ├── 12_f137537055.mp3
│       ├── 13_f111315311.mp3
│       └── 13_f137176607.mp3
├── f105153401.mp3
├── f129107367.mp3
├── f134209383.m3u
├── f134373223.jpg
├── f137340447.m3u
└── f137438751.jpg

5 directories, 45 files
```