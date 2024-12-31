import pandas # import pandas library for reading file
from collections import Counter # import counter to count occurences of each number

data = pandas.read_csv('keno_100_rounds_10_drawn.csv') # specify file to open

combined = [] # initialize list to store combined data

for value in data['data']:  # for every list stored
    numbers = eval(value)   # convert stored string into a readable string
    combined.extend(numbers)  # extend combined to include numbers

count = Counter(combined) # count frequency of every number in combined

top = count.most_common(3) # get the top 3 numbers in the data

print("The 3 most common numbers are:") # print data header
for i, (num, freq) in enumerate(top, 1): # for the list of most common
    print(f"{i}. {num} ({freq} occurrences)") # print item
