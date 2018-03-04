import urllib.request

bosses = ["Kael\\'thas Sunstrider",
          "Yogg-Saron",
          "Malygos",
          "Alysrazor",
          "Ragnaros",
          "Al\\'Akir",
          "Garrosh Hellscream",
          "Horridon",
          "Ji-Kun",
          "Felhounds of Sargeras",
          "Gul\\'dan",
          "Archimonde",
          "Mistress Sassz\\'ine",
          "The Lich King",
          "Onyxia",
          "Elegon"]

str_diff    = "<div class=\"font-bliz-light-xSmall-beige\">"

no_of_bosses = len(bosses)

def find_before_index(main_str, search_str, index):

    # find the first index of search_str in main_str before index and save it to result

    incr = len(search_str)
    left_index = index - 1

    out_of_bounds = False
    
    while (True):
        current_str = main_str[left_index : index]
        
        found_index = current_str.find(search_str)

        if (found_index == -1):
            left_index -= incr

            if (index - left_index > len(main_str)):
                if (out_of_bounds == False):
                    out_of_bounds = True
                else:
                    found_index = -1
                    break
        else:
            break
    
    return left_index + found_index + 1

str_start = " x</span><span class=\"gutter-tiny inline\"></span><span class=\"font-bliz-light-xSmall-lightGreen\">"

# str_start + bossname + str_end = str to search for in the html string

file = open("alturls_multiple.txt", "r") # open the txt file containing urls
alt_links = file.read() # read the file and make it available to the program

urls = alt_links.split("\n") # create url array
no_of_alts = len(urls); # how many urls are there
print ("Number of alts is " + str(no_of_alts))

for i in range(0, no_of_alts):
    print ("Loaded armory URL: " + urls[i] + "/pve") # make sure the urls are correct

boss_kill_counter = [0] * no_of_bosses

for i in range(0, no_of_alts): # for every alt ...
    url = urls[i] + "/pve"
    html = urllib.request.urlopen(url)
    html_str = str(html.read())
    
    print ("\n\n ------------------- Alt name: " +(urls[i])[55:])

    for j in range(0, no_of_bosses): # get boss defeat counts.

        index = 1
        did_it_already = 0
        
        print ("\n" + bosses[j].replace("\\", ""))
        
        while(True):
            count = 0
            
            search_str = "" + str_start + bosses[j]
            index = html_str.find(search_str, index + 1)

            difficulty_index_start = find_before_index(html_str, str_diff, index)
            difficulty_index_end   = difficulty_index_start + (html_str[difficulty_index_start : ]).find("</div><div")

            if (did_it_already == 1):
                did_it_already = 2
            elif (did_it_already == 2):
                did_it_already = 0
            
            if  (index != -1):
                if (html_str[index-3] == '>'):
                    # 2 digit count
                    count = int(html_str[index-2 : index])
                elif (html_str[index-2] == '>'):
                    # 1 digit count
                    count = int(html_str[index-1 : index])
                else:
                    # 3 digit count
                    count = int(html_str[index-3 : index])

                if (did_it_already == 0):                    
                    
                    print ("    " + html_str[ len(str_diff) - 1 + difficulty_index_start : difficulty_index_end ] + ": " + str(count))

                    boss_kill_counter[j] += count

                    did_it_already = 1
                
            else:
                break

print ("\n\n\nTotal number of kills accross all character: ") 
for i in range(0, no_of_bosses):
    print (bosses[i].replace("\\", "") + ": " + str(boss_kill_counter[i]))

end = input("\n\n\nEnter to continue...")
    
