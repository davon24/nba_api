import requests

def get_posts(api_key=None):
    # Define the API endpoint
    url = "https://api.balldontlie.io/v1/players/?cursor=3100"
    call_header = {}
    if api_key:
        call_header['Authorization'] = api_key
    try:
        # Send a GET request to retrieve data
        response = requests.get(url,headers=call_header)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the JSON response
        posts = response.json()
       
        return posts 
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(call_header)
    except Exception as err:
        print(f"Other error occurred: {err}")

