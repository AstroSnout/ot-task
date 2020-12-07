# Python API server  
  
Requirements:  
- Latest Python 3 installed (you can get it [here](https://www.python.org/downloads/))  
  
Installation instructions:  
- Get the source code  
- Install required packages from 'requirements.txt'  
- Rename the file '.env-git' to '.env'  
- Edit the renamed '.env' file and add your API key from etherscan (no quotations required, just paste in the API key)  
- Download the [latest chrome driver](https://chromedriver.chromium.org/downloads) and put it in api-server folder (same folder as 'main.py') as 'chromedriver.exe'
- Run the app through 'start_script.py'  
- The API server should be up and running :)  
  
Potential issues:
- If you get an error thrown during start up (Scraper has no attribute "driver"), try updating your Chrome (not the driver)
