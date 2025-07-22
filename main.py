import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
conn1 = sqlite3.connect('planets.db')

# Select all
planets = pd.read_sql("""SELECT * FROM planets; """, conn1)
print(planets)

# STEP 1
df_no_moons = pd.read_sql(""" 
SELECT *
From planets
WHERE num_of_moons = 0;
""",conn1)
print(df_no_moons)

# STEP 2
df_name_seven = pd.read_sql(""" 
SELECT name, mass
From planets
WHERE length(name) = 7
""",conn1)
print(df_name_seven)



##### Part 2: Advanced Filtering #####

# STEP 3
df_mass = pd.read_sql(""" 
SELECT name, mass
From planets
WHERE mass <= 1.00
""",conn1)
print(df_mass)


# STEP 4
df_mass_moon = pd.read_sql(""" 
SELECT *
From planets
WHERE num_of_moons >= 1 AND mass < 1.00
""",conn1)
print(df_mass_moon)

# STEP 5
# Replace None with your code
df_blue = pd.read_sql(""" 
SELECT name, color
From planets
WHERE color LIKE "%blue%"
""",conn1)
print(df_blue)



##### Part 3: Ordering and Limiting #####

# STEP 0

# Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('dogs.db')

# Select all
fic_dogs = pd.read_sql("SELECT * FROM dogs;", conn2)
print(fic_dogs)

# STEP 6
df_hungry = pd.read_sql(""" 
SELECT name, age, breed
FROM dogs
WHERE hungry = 1
ORDER BY age ASC
""",conn2)
print(df_hungry)

# STEP 7
df_hungry_ages = pd.read_sql(""" 
SELECT name, age, hungry
FROM dogs
WHERE hungry = 1 AND age BETWEEN 2 AND 7
ORDER BY name ASC
""",conn2)
print(df_hungry_ages)

# STEP 8
df_4_oldest = pd.read_sql(""" 
SELECT name, age, breed
FROM dogs					  
ORDER BY age DESC, breed ASC
Limit 4
""",conn2)
print(df_4_oldest)

##### Part 4: Aggregation #####

# Create a connection
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
br_stats = pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)
print(br_stats)

# STEP 9
# Replace None with your code
df_ruth_years = pd.read_sql(""" 
SELECT COUNT(year)
FROM babe_ruth_stats
""",conn3)
print(df_ruth_years)

# STEP 10
# Replace None with your code
df_hr_total = pd.read_sql(""" 
SELECT SUM(HR)
FROM babe_ruth_stats
""",conn3)
print(df_hr_total)

##### Part 5: Grouping and Aggregation #####

# STEP 11
df_teams_years = pd.read_sql(""" 
SELECT team, COUNT(DISTINCT year) AS number_years
FROM babe_ruth_stats
GROUP BY team							 
""",conn3)
print(df_teams_years)

# STEP 12
df_at_bats = pd.read_sql(""" 
SELECT team, AVG(CAST(at_bats AS INTEGER)) AS average_at_bats
FROM babe_ruth_stats
GROUP BY team
HAVING AVG(CAST(at_bats AS INTEGER)) > 200
""",conn3)
print(df_at_bats)

conn1.close()
conn2.close()
conn3.close()