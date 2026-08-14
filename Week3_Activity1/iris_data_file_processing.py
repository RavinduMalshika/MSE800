from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 

#total records
total_records = len(X)
print(f"Total number of records: {total_records}")

# Number of unique flower species
total_num_of_flowers = y['class'].nunique()
print(f"Total number of different flowers: {total_num_of_flowers}")

# Unique species names
names_of_flowers = y['class'].unique()
print(f"Flower species: {list(names_of_flowers)}")
