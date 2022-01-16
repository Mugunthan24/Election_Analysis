import csv
import os

file_to_load = os.path.join( "resources", "election_results.csv")

with open(file_to_load) as election_data:

    reader_file = csv.reader(election_data)
    for rows in election_data:
        print(rows)



        


