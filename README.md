# Highlight Domain Deletion Script

**Overview**:
This script allows you to delete domains from the Highlight using the provided Highlight access token. 
You need to provide the Highlight Company-ID/Root Domain ID and the path to a CSV file containing the 
domain IDs you wish to delete. 

**Prerequisites**
1. Python 3.x installed on your system.
2. Highlight access token. Generate this token from your Highlight account.

**Usage**
1. Install python dpednencies if not already available using "pip install requests"
2. Run the script 
    python highlight_domain_deletion.py
3. Follow the Prompts:
    a. Enter the Highlight Company-ID/Root Domain ID. This should be the base URL of your Highlight account
       (e.g., https://rpa.casthighlight.com or https://app.casthighlight.com ).
    b. Provide the Highlight Company-ID/Root Domain ID (e.g., 12345).
    c. Enter the path to the CSV file containing the domain IDs. (Example D:\CAST\Delete-Domain-ids.csv)
    d. Input your Highlight access token when prompted
5. Review Output:
    The script will display the REST API requests made for each domain deletion, along with the corresponding 
    response status. If a domain is deleted successfully, it will be indicated in the output.

   ![image](https://github.com/anilpunia/Highlight-Delete-Domains/assets/23251091/e689675c-4448-4f42-82c1-db81ee5503d9)
