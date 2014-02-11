#setting argv to take our script, filename
from sys import argv
script, filename = argv

#opens the given file
opened_file = open(filename, 'r')

#reads given file, line by line
read_file = opened_file.readline()

#create an empty dict. we will feed restaurant:rating pairs to later
restaurants_ratings = {}

#this function returns clean lines from raw, to:
#optimized lines as lists with 2 items ["key", "value"]
def process_line(read_file):
    #strip the whitespace in each line
    stripped_restaurants = read_file.strip()

    #optimizing the items in the line -- splitting by colon
    #will return 1 list w/ 2 items ["name", "rating"]
    optimized_line = stripped_restaurants.split(":")

    #takes 'optimized_line' and feeds it as an entry
    #to the dictionary (restaurant_ratings)
    #as key:value pairs.
    restaurants_ratings[optimized_line[0]] = restaurants_ratings.get(optimized_line[0], optimized_line[1]) 
    #prints dictionary, with new entry
    print restaurants_ratings

# for every line in the file do this function 
while #items in read_file != None:
    #perform the function on that line    
    process_line(read_file)

print restaurants_ratings



#feed content into the empty dict in key value pairs
#Strip the whitespace per line item
#sort the output of the dictionary alphabetically
#print the output

#print "Restaurant '%s' is rated at %r" % (key, value)

#close the file
