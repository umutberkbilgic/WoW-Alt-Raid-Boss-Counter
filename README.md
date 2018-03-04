# WoW Alt Raid Boss Counter

Enter your alt armory links to alturls_multiple.txt (link + \n). It will gather all the kill counts for each boss specified in alting.py

Run alting.py

![image](https://raw.githubusercontent.com/umutberkbilgic/WoW-Alt-Raid-Boss-Counter/master/img/screenshot.png)

This is particularly useful if you are farming for a spesific item with a given drop rate and you want to see just how many times you tried to get it.

Current issues: 
* Bosses that appear on multiple raids such as Ragnaros and Archimonde mess things up. Numbers for these bosses are higher than they should be.
* Bosses are hardcoded into the source.
* Apostrophe's in the boss names should be escaped as "\\'" since the HTML extract looks like this: "Kael\'thas Sunstrider".

