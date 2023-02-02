# pandas is the core package for data analytics
import pandas

# create the object
#df=pandas.read_csv('C:\\Users\\s66918\\Desktop\\My PYTHON PROGRAMS\\Read and Write Files\\Employees.txt')
#print(df)

# show the version
#pandas.show_versions()
pandas.__version__



############
# DATAFRAMES are like a 2 dimensional array
# DATAFRAME is a sequence of series that share the same index
############
# SERIES is a one dimensional array of indexed data (i.e row or column)
#
############

# oo is the dataframe here
oo=pandas.read_csv('C:\\Users\\s66918\\Desktop\\My PYTHON PROGRAMS\\PANDAS\\Olympics.csv')

# print series for city
#print(oo['City'])

# print series for Athlete. Note [ or dot notation is fine. I prefer dot notation
#print(oo['Athlete'])
#print(oo.Athlete)

# For multiples
#print(oo[['City', 'Athlete']])

# what type is this object
print(type(oo))
print(type(oo.City))


# print all
#print(oo)