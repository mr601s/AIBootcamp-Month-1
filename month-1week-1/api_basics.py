"""
API Basics - Your first HTTP Request
Day 13: Learning to fetch data from the internet
"""

import requests
import json

def test_simple_api():
    """Make your first API request"""

    print('='*60)
    print('YOUR FIRST API REQUEST')
    print('='*60)

    # Free API - no authenticaion needed

    url = 'https://dog.ceo/api/breeds/image/random'

    print(f'\nFetching data from: {url}')
    print('Waiting for response...\n')

    # The Magic Line - Make HTTP request 
    response = requests.get(url)

    # Check if successful
    if response.status_code == 200:
        print('✅ Success! Response received.\n')

        # Parse JSON response
        data = response.json()

        print('\nResponse Data:')
        print(json.dumps(data, indent=2))

        print(f'\nRandom Dog Image URL: {data["message"]}')
    else:
        print(f'❌ Error: Received status code {response.status_code}')

def test_random_user():
    """API request with parameters"""

    print('\n' + '='*60)
    print('API WITH PARAMETERS')
    print('='*60)

    url = 'https://randomuser.me/api/'

    # Parameters customize what we get 

    params = {
        'results': 1,
        'nat': 'us'
    }

    print('\nfetching random user data...')
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        user = data['results'][0]

        name = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']

        print('\nRandom User Data:')
        print(f'Name: {name}')
        print(f'Email: {email}')

if __name__ == '__main__': 
    test_simple_api()
    
    input("\nPress ENTER for next example...")
    test_random_user()
    
    print("\n🎉 You just made HTTP requests to real APIs!")
    print("This is how modern apps get data from the internet!")