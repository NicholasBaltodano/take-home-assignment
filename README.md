# take-home-assignment
Backend Engineer Take Home Assignment


# TODO
1. ~~Gather Data from https://docs.cryptowat.ch/rest-api/ every minute.~~
   
   ~~- Store this data into a database~~
2. ~~Create API to access this data~~
   ~~- Users will select a metric/coin and get data on it~~
   - Users will recieve price data from the last 24 hours & the ranking based on the STD dev. 
   

# Scalability:
## what would you change if you needed to track many metrics?
## What if you needed to sample them more frequently? 
## what if you had many users accessing your dashboard to view metrics?

# Testing:
## how would you extend testing for an application of this kind (beyond what you implemented)?

# Feature request:
To help the user identify opportunities in real-time, the app will send
an alert whenever a metric exceeds 3x the value of its average in the last 1 hour.
For example, if the volume of GOLD/BTC averaged 100 in the last hour, the app
would send an alert in case a new volume data point exceeds 300. Please write a
short proposal on how you would implement this feature request.