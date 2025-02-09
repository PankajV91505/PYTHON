import requests

def fectch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        message = user_data["content"]
        return message
    else:
        raise "No data found"

def main():
    try:
        message = fectch_random_user_freeapi()
        print(f"Message: {message}")
    except Exception as e:
        print(str(e))
        
    
    
if __name__ == "__main__":
    main()