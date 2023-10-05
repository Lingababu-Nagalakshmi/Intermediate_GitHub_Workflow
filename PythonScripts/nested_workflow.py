import requests

def check_api(api_url):
    try:
        response = requests.get(api_url)

        # Check the status code
        if response.status_code == 200:
            # If the status code is 200, the request was successful
            print("API is working.")
        else:
            # If the status code is not 200, there may be an issue
            print(f"API returned a status code of {response.status_code}.")
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Network error: {e}")
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace this URL with the API you want to check
    api_url = "https://jsonplaceholder.typicode.com/posts/1"

    check_api(api_url)
