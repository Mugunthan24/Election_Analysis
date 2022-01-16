counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])


counties = ["Arapahoe","Denver","Jefferson"] 
if "Arapahoe" in counties: 
    print("True") 
else: 
    print("False")


counties = ["Arapahoe","Denver","Jefferson"] 
if "El Paso" not in counties: 
    print("True") 
else: 
    print("False")


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
 
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of count")


x = 0
while x <= 5:
    print(x)
    x = x + 1

for county in range(3):
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in range(5):
    print(num)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)


for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for key, value in counties_dict.items():
    print(key, value)

for county in counties_dict:
    print(f"{county} has {counties_dict[county]} registered voters")  

for county, voters in counties_dict.items():
    #print(county, voters)
    print(f"{county} has {voters} registered voters.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:  
     print(county_dict.values())

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, num_Voters in counties_dict.items():
    print(f"{county} has {num_Voters:.2f}  registered voters.")



counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
