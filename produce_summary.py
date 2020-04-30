def delivered_melons(day_number, file_name): # create the function
    print("Day", day_number) 
    the_file = open(file_name) # open the file

    for line in the_file: # iterate over the file
        line = line.rstrip() # remove white space on the right
        words = line.split('|') # split each line into a list

        melon = words[0] # assign variables to the list
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
        count, melon, amount)) # print desired information

delivered_melons(1, "um-deliveries-20140519.txt") # call the function
delivered_melons(2, "um-deliveries-20140520.txt")
delivered_melons(3, "um-deliveries-20140521.txt")
