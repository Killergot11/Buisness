import requests

# Replace 'YOUR_UNSPLASH_API_KEY' with your actual Unsplash API key
UNSPLASH_API_KEY = 'g3YuBNbagtTPjCDvEvToXRSrwOvhIbt79KujQpuLW7Y'

# Unsplash API base URL
UNSPLASH_API_BASE_URL = 'https://api.unsplash.com/'

# Function to fetch an image URL from Unsplash based on a query
def fetch_image_url(query):
    headers = {'Authorization': f'Client-ID {UNSPLASH_API_KEY}'}
    params = {'query': query}
    response = requests.get(f'{UNSPLASH_API_BASE_URL}search/photos', headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['total'] > 0:
            return data['results'][0]['urls']['regular']
        else:
            return None
    else:
        return None

# Main loop to interact with the chatbot
print("Image Chatbot: Ask for an image (e.g., cat, dog, flower) or type 'exit' to end.")
while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print("Image Chatbot: Goodbye!")
        break

    image_url = fetch_image_url(user_input)
    if image_url:
        print("Image Chatbot:", image_url)
    else:
        print("Image Chatbot: Sorry, I couldn't find an image for that query.")