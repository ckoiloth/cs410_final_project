# Usage Instructions

To use the system after you have cloned the repository please follow these steps : 

## Setup Open AI

1. Go to [https://openai.com/](https://openai.com/) and login and click on API 
2. Click on API Keys : 
3. 

![Untitled](Usage%20Instructions%2019b70886fa804197a552aa8273ad2f1e/Untitled.png)

1. Click on Create Secret Key and Copy the key 
2. Then go to [keys.py](http://keys.py) in the project repo and paste your secret key in the openAIKey variable as a String

![Untitled](Usage%20Instructions%2019b70886fa804197a552aa8273ad2f1e/Untitled%201.png)

## Start the Service

1. `pip install -r requirements.txt` to get all the required dependencies 
2. Then you need to open two terminals : 
    1. In one of them please start the python server via : 
    
    ```json
    flask run 
    ```
    
    b. On the second one you need start the Streamlit front end via : 
    
    ```json
    streamlit run streamlist_main.py --server.enableCORS=false
    ```
    
    This should bring up these prompts : 
    
    ![Untitled](Usage%20Instructions%2019b70886fa804197a552aa8273ad2f1e/Untitled%202.png)
    
    ![Untitled](Usage%20Instructions%2019b70886fa804197a552aa8273ad2f1e/Untitled%203.png)
    
    and a webpage should open up : 
    
    ![Untitled](Usage%20Instructions%2019b70886fa804197a552aa8273ad2f1e/Untitled%204.png)
    
    You can go ahead and upload documents and ask questions as much as you want now!