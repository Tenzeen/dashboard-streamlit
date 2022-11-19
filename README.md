# Dashboard-Streamlit
## Data Used: https://data.cityofnewyork.us/resource/5ucz-vwe8.csv


## Prompt
1. Create a basic streamlit dashboard with data that you have access to (e.g., de-identified data from a group project, or data that you find interesting that is publicly available). The data that you select should have at least one (if not more) of the following fields to be able to complete Step 3 of this assignment:

    - Date/time stamp 

    - Categorical data

    - Continuous data 

    - OPTIONAL: position/locational data 

The dashboard code and data being used should be included within the github repo 

2. The dashboard should include the following components based on the streamlit documentation (https://docs.streamlit.io/library/api-reference) of what is available: 
    - a header 
    - some text 
    - a code-block 
    - 2 dataframes
    - at least 2 charts (e.g., line, area, bar, scatter plot)


3. Please deploy the streamlit application to your cloud of choice and take screen shots of the deployed app with your IP (OR you can deploy it to your new domain name if you want to....) 

4. Once completed, you can shut down the VM after taking screen shots and including them in the github repo

## Steps for setting up streamlit on GCP
1. Create firewall rule that allows port 8501 on TCP
2. Connect to VM instance via SSH
3. Run: sudo apt-get update
4. Run: sudo apt-install python3-pip
5. Run: sudo -H pip3 install --upgrade pip
6. Run: pip3 install streamlit
7. Run: nano ~/.bashrc
8. Add: export PATH="$HOME/.local/bin:$PATH" to the end of the file
9. Restart by running: source ~/.bashrc
