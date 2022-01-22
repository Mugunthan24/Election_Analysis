# Election_Analysis
Election audit in Colorado

## Overview of Election Audit
The election audit was done to assist Tom, a Colarado Board of Elections employee with tabulating the election results for a US electional prescinct in Colarado. The information the audit was supposed to gather was the total votes, total votes for each candidate, total percentage of votes for each candidate, voter turnout for each county, percentage of votes from each county, the county with the highest turnout, and the winner of the election based on popular vote. If the audit is done successfully with Python, then it is likely to be implemented for future elections of various levels such Federal and Municicipal elections.

## Election-Audit Results
![image_name](https://github.com/Mugunthan24/Election_Analysis/blob/main/Resources/Election%20Analysis.PNG)

### County Breakdown
- A total of 369,711 votes were cast in this congressional election
- Below is a breakdown of the number of votes and percentage of total votes for each county:
    - Jefferson: Contributed to 10.5% of the total votes (38,855 votes)
    - Denver: Contributed to 82.8% of the total votes (306,055 votes)
    - Arapahoe: Contributed to 6.7% of the total votes (24,801 votes)
- Denver received the highest number of votes

### Candidate Breakdown
- Below is a breakdown of the number of votes and percentage of total votes for each candidate:
    - Charles Casper Stockham: Contributed to 23% of the total votes (85,213 votes)
    - Diana DeGette: Contributed to 73.8% of the total votes (272,892 votes)
    - Raymon Anthony Doane: Contributed to 3.1% of the total votes (11,606 votes)
- Below is a breakdown of the candidate who won the election:
    - Candidate Name: Diana DeGette
    - Number of Votes: 272,892
    - Percentage of Total Votes: 73.8%

## Election-Audit Summary
Traditionally, the outcome of elections have been determined by hand or using tools like Microsoft Excel. With the power of Python, it becomes possible to automate gathering key information more efficiently as we have seen for the US electional prescinct in Colarado. However, the code can be adapted to be run for other elections such as at the Federal and Municipal level. The subsequent paragraphs will discuss how this can be done.

### Federal Election
The winner for the US Electional prescinct election is determined by popular vote, however the presidential election is determined by who wins more seats in the electoral college. Each State has varying number of electoral seats based on its population, and if a party wins a majority of the seats in a state, then they get all the seats.

The code can be adapted by creating a dictionary titled "Electoral_College," with state being the key and the number of seats in each state being the value. Then a for loop can be implemented that will go through the data for each state and calculate the total votes, and the percentage of votes for each party. Which ever party has the highest percentage of votes will then get all the seats from that state which can be extracted using the dictionary. We would then move on to the next state and so on and add the number of seats for each state to the winners current amount until all 50 states have been iterated through. The party with the most seats in the end would win the presidential election.

### Municipal Election
The code can be adapted for a municipal election by removing the county information from the code and just tabulating who won the election based on popular vote. The current code calculates numerous variables not needed for a local election.
