import random # import random library for picking random nunbers
import csv # import csv library for writing data to csv

def sim(rounds, winners): # run the simulation with specified rounds and numbers drawn
    data = [] # initialize list to hold data
    for i in range(rounds): # for loop for to simulate data for each round
        data.append(random.sample(range(1, 81), winners)) # append simulated round data to data list
    return data # return final list containing data

def save(data, filename): # function to save data to csv, inputs for filename and data
    with open(filename, mode='w', newline='') as file: # open file with name filename in write mode
        writer = csv.writer(file) # initialize writer
        writer.writerow(['index', 'data']) # write first row of csv, containing structure
        index = 1 # set initial index
        for row in data: # for loop to write every row found in data
            writer.writerow([index, row]) # write the row and its index to csv
            index += 1 # add 1 to the index
        print("data saved")

rounds = int(input("how many rounds: ")) # specify how many rounds to simulate

winners = int(input("how many winners drawn per round: ")) # specify how many numbers to draw, usualy 10 but can vary

filename = f"keno_{rounds}_rounds_{winners}_drawn.csv" # create filename based on input

data = sim(rounds, winners) # run the simulation and save the results
save(data, filename) # save the data