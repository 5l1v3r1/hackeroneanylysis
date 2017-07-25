import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('bounties.csv')

print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Most Reported Programs Overview")
print ("2. Most Amount of Reward Overview")
print ("3. Most Hacked in Month's Overview")
print (30 * '-')

choice = raw_input('Enter your choice [1-3] : ')
choice = int(choice)
if choice == 1:
  program = df.program_name.value_counts().sort_values() 
  program.plot(kind='barh',figsize=(11,11),color='#34ABD8',rot=0)
  plt.show()
elif choice == 2:
  program = df.total_amount.value_counts().sort_values() 
  program.plot(kind='barh',figsize=(20,20),color='#34ABD8',rot=0)  
  plt.show()
else:
  print "Not Found"

