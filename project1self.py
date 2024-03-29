# -*- coding: utf-8 -*-
"""PROJECT1SELF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oQD9pJNE6UZjQvvYROpCJpZ5CDTIT9fq
"""

# Project :
# Let us build a complete project using NumPy (without any help).

# Path: project_data = 'KAG_Conversion_Data.csv'
# Features:
# ad_id: unique ID for each ad

# xyzcampaignid: an ID associated with each ad campaign of XYZ company

# fbcampaignid: an ID associated with how Facebook tracks each campaign

# age: age of the person to whom the ad is shown

# gender: gender of the person to whom the add is shown

# interest: a code specifying the category to which the person’s 
# interest belongs (interests are as mentioned in the person’s Facebook public profile)

# Impressions: the number of times the ad was shown

# Clicks: number of clicks on for that ad

# Spent: Amount paid by company xyz to Facebook, to show that ad

# Total conversion: Total number of people who enquired about the product after seeing the ad

# Approved conversion: Total number of people who bought the product after seeing the ad


# Instructions:
# A) Load the data. Data is already given to you in variable path

# B)How many unique ad campaigns (xyzcampaignid) does this data contain ? 
# And for how many times was each campaign run ?

# C) What are the age groups that were targeted through these ad campaigns?

# D)What was the average, minimum and maximum amount spent on the ads?

# E) What is the id of the ad having the maximum number of clicks ?

# F) How many people bought the product after seeing the ad with most clicks? 
# Is that the maximum number of purchases in this dataset?

# G) So the ad with the most clicks didn't fetch the maximum number of purchases. 
# Find the details of the product having maximum number of purchases

# A) Load the data. Data is already given to you in variable path
import numpy as np
data_file = "KAG_Conversion_Data.csv"

data = np.genfromtxt(data_file, delimiter=",", skip_header=1, dtype= int)
data = np.genfromtxt(data_file, delimiter=",", skip_header=1, dtype= str)
# data = data.astype()
print("\nData: \n\n", data)

xyz = data[:,1]
print(xyz)

# B) How many unique ad campaigns (xyzcampaignid) does this data contain ? 
# And for how many times was each campaign run ?

np.unique(xyz, return_counts=True)   
# use return_counts to get all values 
# where unique

# C) What are the age groups that were targeted through these ad campaigns?

AgeTarget = data[:,3]
print(AgeTarget)
np.unique(AgeTarget, return_counts= True) #, return_index=True)

data = np.genfromtxt(data_file, delimiter=",", skip_header=1, dtype= float)

print(data)

# D) What was the average, minimum and maximum amount spent on the ads?


data = np.genfromtxt(data_file, delimiter=",", skip_header=1, dtype= float)
Avg = np.mean(data[:,8])
MINIMUM  = np.min(data[:,8])
MAXIMUM = np.max(data[:,8])
print(Avg)
print(MAXIMUM)
print(MINIMUM)

# Max_Clicks = np.max(data[:7])
# print(Max_Clicks)

spent = np.mean(data[:,8].astype('float64'))
print(spent)

# E) What is the id of the ad having the maximum number of clicks ?
np.max(data[:,7])

# F) How many people bought the product after seeing the ad with most clicks? 
# Is that the maximum number of purchases in this dataset?

np.where(data[:,7] == 421)
maxof = np.where(data == np.max(data[:,7]))
print(maxof)

data[maxof[0], 0]

# F) How many people bought the product after seeing the ad with most clicks? 
# Is that the maximum number of purchases in this dataset? ALTERNATIVE WAY
ID_max = data[data[:,7] == 421].astype(int)
print(ID_max[0,0])
print(ID_max[:,:])

# z = np.where(data == np.max(data[:,7]))
# data[z[0],0]

# G) How many people bought the product after seeing the ad with most clicks? 
# Is that the maximum number of purchases in this dataset?
#  ALTERNATIVE WAY
data[860,10]

# Is that the maximum number of purchases in this dataset?
np.max(data[:,10])

# So the ad with the most clicks didn't fetch the maximum number of purchases. 
# Find the details of the product having maximum number of purchases

np.unique(data[data[:,10]== 13]).astype(int)

max_Number_of_Purchases = data[data[:,10]==21].astype(int)
print(max_Number_of_Purchases)

max_Number_of_Purchases

print("The Ad id for the product having maximum number of purchases: ", max_Number_of_Purchases[0][0])

data_string = np.genfromtxt(data_file, delimiter=",", skip_header=1, dtype= str)
max_Number_of_purchases_str = data_string[528,:]
print(max_Number_of_purchases_str)
# max_Number_of_Purchases_string = data_string[data_string[:,10]==21]
# print(max_Number_of_Purchases_string[528, :])

np.where(data[:,0]==1121104)

max_purchases_index = np.where(data == np.max(data[:,10]))
data[max_purchases_index[0][0]]

print("The Ad id for the product having maximum number of purchases: ", max_Number_of_Purchases[0][0])
print("The ")

dictionary = {"ad_id":max_Number_of_Purchases[0][0], 
              "xyz_campaign_id":max_Number_of_Purchases[0][1],
              "fb_campaign_id":max_Number_of_Purchases[0][2],
              "age":max_Number_of_purchases_str[3],
              "gender":max_Number_of_purchases_str[4],
              "interest":max_Number_of_Purchases[0][5], 
              "Impressions":max_Number_of_Purchases[0][6],
              "Clicks":max_Number_of_Purchases[0][7],
              "Spent":max_Number_of_Purchases[0][8],
              "Total_Conversion":max_Number_of_Purchases[0][9],
              "Approved_Conversion":max_Number_of_Purchases[0][10]}

print(dictionary)

