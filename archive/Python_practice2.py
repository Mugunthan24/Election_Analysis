from re import X


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, value in counties_dict.items():
    print(f"{county} county has {value:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for item in voting_data:
    print(f"{item['county']} has {item['registered_voters']:,} registered_voters.")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.") 

for county in counties_dict.keys():
    print(counties_dict.items())
    print(counties_dict.values())

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)