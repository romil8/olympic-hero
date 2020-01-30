# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data= pd.read_csv(path)
data.rename({'Total':'Total_Medals'},axis=1,inplace=True)
data.head(10)


# --------------
#Code starts here
data['Better_Event']= np.where(data['Total_Summer'] > data['Total_Winter'],'Summer',np.where(data['Total_Summer'] == data['Total_Winter'],'Both','Winter'))
better_event = data['Better_Event'].value_counts().idxmax()

print('Better event with respect to all the performing countries : ')
print(better_event)



# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

#drop last row
top_countries.drop(len(data) - 1, axis = 0, inplace = True)

#function to get top 10 values for a particular column
def top_ten(df, col_name) :
  country_list = []
  country_list = df.nlargest(10,col_name)
  return country_list

#Get top 10 values for a particular column
top_10_summer = top_ten(top_countries,['Total_Summer'])['Country_Name'].tolist()
top_10_winter = top_ten(top_countries,['Total_Winter'])['Country_Name'].tolist()
top_10 = top_ten(top_countries,['Total_Medals'])['Country_Name'].tolist()

#Get top performing countries 
common = list(set(top_10_summer).intersection(set(top_10_winter)).intersection(set(top_10)))
print(common)



# --------------
#Code starts here
summer_df= data[data['Country_Name'].isin(top_10_summer)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])

#Changing the graph title
plt.title('Top 10 Summer')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')


#For Winter

#Creating the dataframe for Winter event
winter_df=data[data['Country_Name'].isin(top_10_winter)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])

#Changing the graph title
plt.title('Top 10 Winter')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')



#For both the events

#Creating the dataframe for both the events
top_df=data[data['Country_Name'].isin(top_10)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(top_df['Country_Name'], top_df['Total_Medals'])

#Changing the graph title
plt.title('Top 10')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')





# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax()]['Country_Name']
print("Top Summer Country:", summer_country_gold, " has a ratio of %.2f" %summer_max_ratio )


#For Winter
winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax()]['Country_Name']
print("Top Winter Country:", winter_country_gold, " has a ratio of %.2f" %winter_max_ratio )


#For Both the events
top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax()]['Country_Name']
print("Top Country:", top_country_gold, " has a ratio of %.2f" %top_max_ratio )




# --------------
#Code starts here
data_1 = data.drop(data.tail(1).index)

# COmpute weighted value where each gold medal counts for 3 points, silver medals for 2 points, and bronze medals for 1 point
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1

# Maximum points earned by any country
most_points = data_1['Total_Points'].max()

# Country name which have earned the maximum points
best_country = data_1.loc[data_1['Total_Points'].idxmax()]['Country_Name']
print("{} has earned the most points with a total count of {}".format(best_country,most_points))


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best.reset_index(drop = True, inplace = True)

#Subset 'best' even further by only including the columns : ['Gold_Total','Silver_Total','Bronze_Total']
best = best[['Gold_Total','Silver_Total','Bronze_Total']]

# A stacked bar plot 
best.plot.bar(stacked = True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)


