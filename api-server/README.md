# Python API server  
  
Requirements:  
- Latest Python 3 installed (you can get it [here](https://www.python.org/downloads/))  
- Latest Google Chrome browser installed on the system
  
Installation instructions:  
- Get the source code  
- Install required packages from 'requirements.txt' ('pip install -r requirements.txt')  
- Create a new file in 'api-server' root folder named '.env'
- Edit the created '.env' file and add your etherscan API key as ETHERSCAN_API_KEY=whatevermyapikeyis123  
- Download the [latest chrome driver](https://chromedriver.chromium.org/downloads) and put it in api-server folder (same folder as 'main.py') as 'chromedriver.exe'
- Run the app through 'start_script.py'  
- The API server should be up and running :)  
  
Potential issues:
- If you get an error thrown during start up (Scraper has no attribute "driver"), try updating your Chrome browser (not the driver)
