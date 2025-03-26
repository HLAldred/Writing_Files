#--------------
#FP2-F02-Writing Files
#Hailey-lynn Aldred
#25 March 2025
#--------------

#----Functions----#
def write_file():
    new_file = open('writing_files.txt', 'w') #opens/creates new file
    print("The file has been opened.")
    new_file.write("These are my drama lines...\n")#new line in the file
    new_file.write("Ahem.\n")#new line in the file
    new_file.write("Has the BC delegate arrived yet?\n")#new line in the file
    new_file.write("Look, it's important I know.\n")#new line in the file
    new_file.write("There's more lines but you'll have to come see the show...")#new line in the file
    print("Closing the file now.")
    new_file.close()#closes the file
    print("The file has been closed.")
    
def app_file():
    new_file = open('writing_files.txt', 'a')#opens the file and ADDS ONTO IT
    print("The file has been opened.")
    new_file.write("\nI'm currently listening to Headlock by Imogen Heap.")
    new_file.write("\nIt's quite good.")
    print("Closing the file now.")
    new_file.close()
    print("The file has been closed.")
    
def name_file():
    #asking questions for in the file
    name = input("What is your name? ")
    song = input("What is your favourite song? ")
    band = input("What is your favourite band/artist? ")
    
    file = name + '.txt' #combines the two and turns it into a .txt file
    save = open(file, 'w') #opens the .txt file that is attached to the file variable
    
    save.write("Name: ")#just some printed stuff
    save.write(name + ', ')#answer plus a comma to separate the other answers
    save.write("Favourite Song: ")
    save.write(song + ', ')#comma to separate
    save.write("Favourite Band/Artist: ")
    save.write(band)
    #creates a new line, and inserts the 'name' variable
    save.write(f"\nThat's pretty cool, {name}. My favourite song is Future is a Foreign Land. My favourite band/artist is Ghost.")
    save.close()#closes the file
    
def main():#all the main code into a singular function
    write_file()
    app_file()
    name_file()
    
#----Main Code----#
main()



