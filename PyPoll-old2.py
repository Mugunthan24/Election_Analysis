import os
import csv

file_to_save = os.path.join("analysis", "election_test.txt")

with open(file_to_save, "w") as txt_file:
    txt_file.write("Mugunthan\nSaranya")