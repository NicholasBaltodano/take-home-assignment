# take-home-assignment
Backend Engineer Take Home Assignment

## PreRequisites 
   Python 3.10+
# Install Instructions
1. Clone repo from github. 
      `https://github.com/NicholasBaltodano/take-home-assignment.git`
2. `cd take-home-assignment`
2. `pip install -r requirements.txt`
3. Optional - You may run into a protobuf error, if you do, please run 
   1. `pip install protobuf<=3.20.1 --force-reinstall`
4. Copies from the Crypto watch SDK
   
   ## API Crendential

   Using a credential file will allow you to authenticate your requests and grant you the API access of your Cryptowatch account.

   Your account Credits will be consumed for the REST and WebSocket API. Specific Credit cost details can be found on the [Pricing page](https://cryptowat.ch/pricing).

   ### Setup your credential file

   1. Generate an Cryptowatch API key from [your account](https://cryptowat.ch/account/api-access)
   2. Create your credential file on your machine by running in order:

      2.1 `mkdir $HOME/.cw`

      2.2 `echo "apikey: 123" > $HOME/.cw/credentials.yml` (where `123` is your 20 digits **public key**)

   3. Verify with `cat $HOME/.cw/credentials.yml` that you see something like below (`123` being your public key):

   ```
   apikey: 123
   ```

   The SDK will read your public key as soon as `import cryptowatch` is ran in your script.

5. Start Server
   1. `python -m uvicorn main:app`

# TODO
1. ~~Gather Data from https://docs.cryptowat.ch/rest-api/ every minute.~~
   
   ~~- Store this data into a database~~
2. ~~Create API to access this data~~
   ~~- Users will select a metric/coin and get data on it~~
   - Users will recieve price data from the last 24 hours & the ranking based on the STD dev. 
3. Refactor!
   1. Need to create seperate the query away from the get_metric function
   2. Add better logging for observabilty
   3. Add a better way to deploy (docker?)
   4. Put application behind NGINX server for production.   
   

# Scalability:
## what would you change if you needed to track many metrics?
   As of right now, the metrics are listed in the config.py. If its a few metrics we can just add them to the list, but if we
   were tracking a lot more, I would have the lists get created dynamically from a central file/database and have the acceptable response list automatically grow with any that we add. 

## What if you needed to sample them more frequently? 
   Right now I have the samping time default set in config.py For a temporary change we can change the file or pass in a specific time. 
   Eventually we can have the application check a configuration for sampling time every so often so it can be changed on the fly
   or have a strategy pattern implementation for the sampling time.

## what if you had many users accessing your dashboard to view metrics?
   I would change the way the API was designed. I would go for a more microservice/API gateway that scales up and down with demand on the application. 
   We could also implement a throttling/rate keeping for API access. 

# Testing:
## how would you extend testing for an application of this kind (beyond what you implemented)?
   We can incorporate testing each endpoint with good and bad data, I would want to test the standard deviation functionality. 
   Other than that I would want to incorporate Stress testing(as Users grow), Load testing, and with the future refactoring regression testing. 
   

# Feature request:
To help the user identify opportunities in real-time, the app will send
an alert whenever a metric exceeds 3x the value of its average in the last 1 hour.
For example, if the volume of GOLD/BTC averaged 100 in the last hour, the app
would send an alert in case a new volume data point exceeds 300. Please write a
short proposal on how you would implement this feature request.


With a new system design found in the Future.png photo, I would have a seperate service that queries the daemon service db for hourly results
of each metric. It will keep history of the the averages, once an average is calculated it will be compared to its previous averages, if it crosses over some specified threshold(3x) then we can send the info to an alerting service that will send to all users tracking that metric. 

Since crypto is volatile we can opt not to make sure the metric is constistently increased before sending notifications, or we can poll the average on a shorter time basis to make sure its consistent. I'm betting users would rather be first then have 100% accuracy.