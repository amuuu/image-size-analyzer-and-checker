import sys
from process import *
from os import walk

#######################

IMG_PATH = "imgs/"

#######################

files = []
for (dirpath, dirnames, filenames) in walk(IMG_PATH):
    files.extend(filenames)
    break

modify_dictionary = {}
for item in files:
    size = get_size(IMG_PATH+item)
    
    print(str(size[1]) + "x" + str(size[0]) + " :::: " + item)
    
    modify_str, modify_tuple = check_size(size)
    
    if modify_tuple != None:
        modify_dictionary[item] = modify_tuple
    
    print(modify_str)
    print()


should_rescale = input("####\n\nWould you like the program to rescale images automatically? (y/n)\n")
if (should_rescale == 'y'):
    os.mkdir(IMG_PATH + "modified_photos")
    
    for key in modify_dictionary:
        print("Rescaling " + key + "...")

        if modify_dictionary[key][0] == 0: #y
            target_y = "y="+str(modify_dictionary[key][1])
            target_x = ""
        else:
            target_x = "x="+str(modify_dictionary[key][1])
            target_y = ""

        img = process(IMG_PATH + key, process_type="rescale", target_x=target_x, target_y=target_y)
        save(img, IMG_PATH + "modified_photos/" + key)
        
        print("Saved new " + key + ".")


else:
    print("Auto-rescale canceled. See you later bro/sis")
