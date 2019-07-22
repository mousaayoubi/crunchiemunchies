import codecademylib
import numpy as np

#Import cereal file
calorie_stats = np.genfromtxt('cereal.csv', delimiter = ',')
print(calorie_stats)

#Average of data
average_calories = np.mean(calorie_stats)
print(average_calories)

#Sort data
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

#Median of data
median_calories = np.median(calorie_stats)
print(median_calories)

#nth percentile
nth_percentile = np.percentile(calorie_stats, 4)
print(nth_percentile)
nth_percentile = 4

#Percentage of cereals over 60 calories
more_calories = np.mean(calorie_stats>60)
print(more_calories)

#Std of data
calorie_std = np.std(calorie_stats)
print(calorie_std)

#Marketing message
marketing = 'CrunchieMunchies only has 60 calories per serving while 96% of its competitors have higher calories than that. It must be one of the healthiest cereals out there.'
print(marketing)