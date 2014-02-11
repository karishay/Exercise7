from sys import argv
#import the list of restaurants (scores.txt)
script, filename = argv

#open the file
opened_file = open(filename, 'r')

#read the file
read_file = opened_file.readline()

#make a function to run it on every line
def process_line(read_file):
    #put the working code here!
    pass
#split the file into a list
split_restaurants = read_file.split(":")
#print split_restaurants
print split_restaurants

#create an empty dict
#restaurants = {}

#feed content into the empty dict in key value pairs
#Strip the whitespace per line item
#sort the output of the dictionary alphabetically
#print the output

#print "Restaurant '%s' is rated at %r" % (key, value)

#close the file
opened_file.close()