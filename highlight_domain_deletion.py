import csv
import requests

def delete_domain(base_url, company_id, domain_id, token):
    url = f"{base_url}/WS2/portfolioManagement/domains/{company_id}/domains/{domain_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"  # Adding bearer token
    }
    try:
        #print("Inside try block")  # Add this line
        print("REST API:", url)  # Add this line
        response = requests.delete(url, headers=headers)
        #print("Response Status Code:", response.status_code)
        #print("Response Content:", response.content)
        response.raise_for_status()  # Raise an HTTPError for bad response status codes

        if response.status_code == 204:
            print(f"Domain with ID {domain_id} deleted successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to delete domain with ID {domain_id}. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    base_url = input("Enter the Highlight Company-ID/Root Domain ID r(Example https://rpa.casthighlight.com):  ")
    company_id = input("Enter the Highlight Company-ID/Root Domain ID(Example 12345): ")
    csv_file = input("Enter the path of the CSV file containing domain IDs: ")
    token = input("Enter your Highlight access token: (Generate and use Highlight access token) ")  # Replace with your bearer token
    domain_ids = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present

# Check if the reader is empty or contains only one row
        rows = list(reader)
        if len(rows) == 0:
            print("CSV file is empty.")
            return
        elif len(rows) == 1:
            # If only one row, directly extract the domain ID
            domain_id = rows[0][0]
            domain_ids.append(domain_id)
        else:
            # If multiple rows, iterate over them and extract domain IDs
            for row in rows:
                domain_id = row[0]  # Assuming domain IDs are in the first column
                domain_ids.append(domain_id)
    
    domain_ids.sort()  # Sort the domain IDs in ascending order
    
    for domain_id in domain_ids:
        delete_domain(base_url,company_id,domain_id, token)

if __name__ == "__main__":
    main()
