"""
    run cmd : python automate.py <username> <password>
    P.S. username - Informatica Secure Agent Username
         password - Informatica Secure Agent Password
"""

import requests
import json
import wget
import sys

# Set platform for which secure agent software is to be downloaded.
# ( win64 / linux64 )
platform = "linux64"

# Generate login URL
login_url = "https://dm-em.informaticacloud.com/ma/api/v2/user/login"

# Required Login headers
login_headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Required login data to be sent to server.
login_data = {
    "@type": "login",
    "username": sys.argv[1],
    "password": sys.argv[2],
}

# Make POST request and save response.
login_response = requests.post(
    login_url, data=json.dumps(login_data), headers=login_headers
)

print(f"Successfully logged in with : {login_data['username']}")

# Extract required information.
icSessionId = login_response.json()["icSessionId"]
serverURL = login_response.json()["serverUrl"]

print(f"Generating secure agent download information...")

# Generate Installer URL.
installer_info_url = f"{serverURL}/api/v2/agent/installerInfo/{platform}"

# Required installer headers.
installer_info_headers = {"icSessionid": f"{icSessionId}"}

# Make GET request to server with header and save response.
installer_info_response = requests.get(
    installer_info_url, headers=installer_info_headers
)

# Extract required information from response.
print(f"Generating download URL for secure agent...")
downloadUrl = installer_info_response.json()["downloadUrl"]
install_token = installer_info_response.json()["installToken"]

# Download secure agent software.
print(f"Downloading secure agent for {platform}")
wget.download(downloadUrl)

print(f"\nSecure agent download successfull...")

# Write the username and install token to a file.
with open("username.txt", "w") as file_username:
    file_username.write(login_data["username"])

print(f"Username stored in 'username.txt'")

with open("install-token.txt", "w") as file_token:
    file_token.write(install_token)

print(f"Install token stored in 'install-token.txt'")
