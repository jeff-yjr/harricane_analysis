# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages

def convert_damage(damage):
  num_damage = []
  unit_damage = []
  new_damage = []
  for cost in damage:
    if cost == 'Damages not recorded':
      num_damage.append(0)
      unit_damage.append(0)
    else:
      num_damage.append(float(cost[:-1]))
      unit_damage.append(cost[-1])

  num = 0
  while num < len(num_damage):
    if num_damage[num] == 0:
      new_damage.append("Damages not recorded")
    else:
      new_damage.append(num_damage[num]*conversion[unit_damage[num]])
    num+=1
  return new_damage

updated_damages=convert_damage(damages)

# 2
# Create a Table
def make_table(name, months, years, max_sustained_winds, areas_affected, Damage, deaths):
  table = {}
  index = 0
  while index < len(name):
    table[name[index]]={
      "Name": names[index],
      "Month": months[index],
      "Year": years[index],
      "Max Sustained Wind": max_sustained_winds[index],
      "Areas Affected": areas_affected[index],
      "Damage": updated_damages[index],
      "Deaths": deaths[index]
    }
    index +=1
  return table

hurricanes_table = make_table(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

# Create and view the hurricanes dictionary

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def by_year(dictionary):
  year_dic = {}

  for key, value in dictionary.items():
    current_year = value["Year"]
    if current_year in year_dic:
      year_dic[current_year].append(value)
    else:
      year_dic[current_year]= []
      year_dic[current_year].append(value)

  return year_dic

hurricane_by_year = by_year(hurricanes_table)

# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in

def count_areas(hurricanes_table):
  area_dic = {}
  for value in hurricanes_table.values():
    current_region = value['Areas Affected']
    for area in current_region:
      if area in area_dic:
        area_dic[area] +=1
      else:
        area_dic[area] = 1

  return area_dic

hurricane_affected_area = count_areas(hurricanes_table)

# 5
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def most_affected_areas(hurricane_affected_table):
  aff_num = 0
  aff_area = ""
  for area, times in hurricane_affected_table.items():
    if times > aff_num:
      aff_num = times
      aff_area = area
  return [aff_area,aff_num]

most_aff_area = most_affected_areas(hurricane_affected_area)

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

def find_deadliest_hurricane(hurricane_table):
  death_toll = 0
  area = ""
  for key, value in hurricane_table.items():
    if value["Deaths"]>death_toll:
      area = key
      death_toll = value["Deaths"]

  return [area, death_toll]


deadliest_hurricane = find_deadliest_hurricane(hurricanes_table)

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

# categorize hurricanes in new dictionary with mortality severity as key

def hurricane_mortality(hurricane_table):
  mort_table = {
    1:[],
    2:[],
    3:[],
    4:[],
    5:[]
  }

  for key, value in hurricane_table.items():
    if value["Deaths"] < 100:
      mort_table[1].append(value)
    elif (value["Deaths"] < 500):
      mort_table[2].append(value)
    elif (value["Deaths"] < 1000):
      mort_table[3].append(value)
    elif (value["Deaths"] < 10000):
      mort_table[4].append(value)
    elif (value["Deaths"] > 10000):
      mort_table[5].append(value)

  return mort_table

hurricane_mort_scale = hurricane_mortality(hurricanes_table)

#for key, value in hurricane_mort_scale.items():
#  for hurricanes in value:
#    print(str(key)+": "+ hurricanes["Name"]+ " "+str(hurricanes["Deaths"]))



# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def find_most_dam_hurricane(hurricane_table):
  most_damage = 0
  hurricane = ""
  for key, value in hurricane_table.items():
    #print(key +": "+str(value["Damage"]))
    if type(value["Damage"]) == float:
      if value["Damage"] > most_damage:
        hurricane = key
        most_damage = value["Damage"]

  return [hurricane, most_damage]

most_dam_hurricane = find_most_dam_hurricane(hurricanes_table)

#print(most_dam_hurricane)
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key

def hurricane_damage_scale(hurricane_table):
  damage_table = {1:[], 2:[], 3:[], 4:[], 5:[], "Unknown":[]}

  for key, value in hurricane_table.items():
    if type(value["Damage"]) == str:
      damage_table["Unknown"].append(value)
    elif value["Damage"] < 100000000.00:
      damage_table[1].append(value)
    elif (value["Damage"] < 1000000000.00):
      damage_table[2].append(value)
    elif (value["Damage"] < 10000000000.00):
      damage_table[3].append(value)
    elif (value["Damage"] < 50000000000.00):
      damage_table[4].append(value)
    elif (value["Damage"] > 50000000000.00):
      damage_table[5].append(value)

  return damage_table


hurricane_damage_table = hurricane_damage_scale(hurricanes_table)

#for key, value in hurricane_damage_table.items():
#  for hurricanes in value:
#    print(str(key)+": "+ hurricanes["Name"]+ " "+str(hurricanes["Damage"]))
