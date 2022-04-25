# Technical test 

## Context
  Design automation solution  about code review for the security team
## About the solution  

## How to read the project 

## Environment 
### Install Python 
  |   OS          | Link         |
  | :--------------- |:---------------:| 
  |Windows| https://www.python.org/downloads/windows/| 
  |Linux| https://www.python.org/downloads/source/ |
  |Mac OS| https://www.python.org/downloads/macos/ |

### Library to install:
  | Package          | Version         |
  | :--------------- |:---------------:| 
  | Python  |   3..9.7       |  
  | Flask  |   2.1.1         |  
  | Flask-RESTful  | 0.3.9   |   
  | ghapi  | 0.1.20          |    
   
  ```
     pip install flask
     pip install flask_restful 
     pip install ghapi  
  ``` 
 ### Good practice 
 You can create virtual environment : https://docs.python.org/3/library/venv.html   
  
## Configuration 
You will need 3 files configuration:
* config.json : general configuration of the application 
 ```
     {
       "ip":"0.0.0.0",
       "port":8000,
       "debug":1
    }
  ``` 
* configGithub.json : github api configuration 
  ``` 
  {
        "github_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "login": "login",
        "organizations": ["Orga1", "Orga2"]
   }
   ```
* configDatabase.json : database configuration 

_Not implemented_

##  Run the application 
```  
  python main.py 
```

If you want to expose your api, you can use : https://dashboard.ngrok.com/api 
