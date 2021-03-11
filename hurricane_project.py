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

#2 Damage Tester
def damages_updated(damagy):
  damage_list = []
  for damage in damagy:
    if damage == 'Damages not recorded':
      damage_list.append(damage)
    elif damage[-1] == "M":
      damage_list.append(float(damage[0:-1])*1000000)
    else:
      damage_list.append(float(damage[0:-1])*1000000000)
  return damage_list

damaging_hurricane = (damages_updated(damages))
# print(damaging_hurricane)

# 3
# Create and view the hurricanes dictionary
def hurricane_dic_maker(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricane_dic = {}
  for i in range(len(names)):
    hurricane_dic[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': damages[i], 'Deaths': deaths[i]}
  return hurricane_dic

my_hurrican_dic = hurricane_dic_maker(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

# print(my_hurrican_dic)

# 4
# Organizing by Year

def hurricane_dir_to_year(yeary, namey, diccy):
  hurricane_year_dic = {}
  for i in range(len(diccy)):
    if yeary[i] in hurricane_year_dic:
      hurricane_year_dic[yeary[i]].append([diccy[names[i]]])
    else:
      hurricane_year_dic[yeary[i]] = [diccy[names[i]]]
  return hurricane_year_dic
  

big_one =(hurricane_dir_to_year(years, names, my_hurrican_dic))

# print(big_one[1932])

# 5
# Counting Damaged Areas
def area_impact_count(dico):
  impacted_areas_dic = {}
  for i in my_hurrican_dic.values():
    for j in i['Areas Affected']:
      if j not in impacted_areas_dic:
        impacted_areas_dic[j] = 1
      else:
        impacted_areas_dic[j] += 1
  return impacted_areas_dic

impacted_areas = (area_impact_count(my_hurrican_dic))

# print(impacted_areas)

# 6
# Calculating Maximum Hurricane Count
def worst_impacted_spot(dicto):
  fudgy = list(dicto.values())
  fidgy = list(dicto.keys())
  position = (fudgy.index(max(fudgy)))
  return f'The worst area hit by a hurricane was {fidgy[position]}, which was hit a grand total of {fudgy[position]} times.'

# print(worst_impacted_spot(impacted_areas))

# 7
# Calculating the Deadliest Hurricane

def biggest_killer(dikky):
  killer_dic = {}
  for i in dikky:
    joe = dikky[i]["Deaths"]
    killer_dic[i] = dikky[i]["Deaths"]

    fudgy = list(killer_dic.values())
    fidgy = list(killer_dic.keys())
    position = (fudgy.index(max(fudgy)))

  return f'The hurricane that caused the greatest number of deaths was Hurricane {fidgy[position]}, which killed a total of {fudgy[position]} people.'

# print(biggest_killer(my_hurrican_dic))

# 8
# Rating Hurricanes by Mortality

mortality_scale = {0: "",
                   1: "",
                   2: "",
                   3: "",
                   4: ""}


def mortality_ranking(dikky):
  mortal_dic = {}
  neo_mortal_dic = {}
  for i in dikky:
    joe = dikky[i]["Deaths"]
    mortal_dic[i] = joe
  # print(mortal_dic)

  for j, k in mortal_dic.items():
    if k == 0:
      val = 0
    elif k <= 100:
      val = 1
    elif k <= 500:
      val = 2
    elif k <= 1000:
      val = 3
    elif k <= 10000:
      val = 4
    else:
      val = 5
  
    if val in neo_mortal_dic:
      neo_mortal_dic[val].append(j)
    else:
      neo_mortal_dic[val] = [j]

  return neo_mortal_dic

big_killers = mortality_ranking(my_hurrican_dic)
# print(big_killers[1])

# 9
# find highest damage inducing hurricane and its total cost

def greatest_damage(dikky):
  damagy_dic = {}
  #First, create a bespoke dictionary for cyclone and damage caused
  for i in dikky:
    joe = dikky[i]["Damage"]
    damagy_dic[i] = dikky[i]["Damage"]

  #Then, clean it to get it as values
  neo_damage_dic = {}
  for cyclone, damage in damagy_dic.items():
    if damage == 'Damages not recorded':
      neo_damage_dic[cyclone] = 0
    elif damage[-1] == "M":
      neo_damage_dic[cyclone] = float(damage[0:-1])*1000000
    else:
      neo_damage_dic[cyclone] = float(damage[0:-1])*1000000000

  #Now you can find the max value
  fudgy = list(neo_damage_dic.values())
  fidgy = list(neo_damage_dic.keys())
  position = (fudgy.index(max(fudgy)))
  return f'The hurricane that caused the greatest damage was Hurricane {fidgy[position]}, which caused damage equal to ${fudgy[position]}.'

# print(greatest_damage(my_hurrican_dic))

# 10
# Rating Hurricanes by Damage

def ranking_damage(dikky):
  damagy_dic = {}
  #First, create a bespoke dictionary for cyclone and damage caused
  for i in dikky:
    joe = dikky[i]["Damage"]
    damagy_dic[i] = dikky[i]["Damage"]

  #Then, clean it to get it as values
  neo_damage_dic = {}
  for cyclone, damage in damagy_dic.items():
    if damage == 'Damages not recorded':
      neo_damage_dic[cyclone] = 0
    elif damage[-1] == "M":
      neo_damage_dic[cyclone] = float(damage[0:-1])*1000000
    else:
      neo_damage_dic[cyclone] = float(damage[0:-1])*1000000000

# print(ranking_damage(my_hurrican_dic))
  final_damage_dic = {}
  for j, k in neo_damage_dic.items():
    if k == 0:
      val = 0
    elif k <= 100000000:
      val = 1
    elif k <= 1000000000:
      val = 2
    elif k <= 10000000000:
      val = 3
    elif k <= 50000000000:
      val = 4
    else:
      val = 5
    
    if val in final_damage_dic:
      final_damage_dic[val].append(j)
    else:
      final_damage_dic[val] = [j]
    
  return(final_damage_dic)

print(ranking_damage(my_hurrican_dic))
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}