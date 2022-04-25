# Technical test 

## Context
  Design automation solution  about code review for the security team
  The goal is to have different ways to launch actions on github objects (organization, repository, branch, ...) :  
  * Manually using API   
  * With weebhook a component listens webhook and treat each event  
  * You can schedule some action using API and scheduler
  
## About the solution 
  About the solution, I don't have time to finish all the development but I put the focus on design.   
  In this project, I assume that a lot of functions are developped. 
  I use POO to design the application because the code is used to treat event and for the endpoint API. Each object in github can be designed as an object in the code. For each object, you have class API associated for the endpoint. About webhook, the object is instantiated and you can call methods to do some actions when event arrived.  
  I assume that some unknown event can be stored in a database  
  I assume that each action done is stored in database and  if client wants, we can expose endpoint to permit them to do reporting.   
  To improve the solution, I can write developper documentation and api documentation with 

## How to read the project 
  If you want to see how I developped, you can see the class Organization, Config class. 
  I put a lot of descriptions in each files.  

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
