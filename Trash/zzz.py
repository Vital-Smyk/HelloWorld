name_of_file = input("Ввод имени файла: ")
completeName = name_of_file + ".txt"
file1 = open(completeName , "w")
toFile = input("Write what you want into the field")
file1.write(toFile)
file1.close()