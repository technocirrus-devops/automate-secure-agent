#!/bin/bash
# Pointing to sh does not work in ubuntu, bash works fine.

python3 automate.py $USERNAME $PASSWORD

username=`cat username.txt`
token=`cat install-token.txt`
path="./"

echo "Username : $username"
echo "Install Token : $token"

# Find newly downloaded file.
installer_name=$(find -name agent64_install_ng_ext*.bin)    # ./filename

# Using substring to remove './' from filename.
installer=${installer_name:2}   # filename

chmod u+x $installer

echo "Installing secure agent in silent mode..."
$installer_name -i silent -DUSER_INSTALL_DIR=/home/ec2-user/

echo "Installation complete"

sleep 600
cd /home/ec2-user/apps/agentcore

./infaagent startup
echo "Secure Agent Startup complete"

sleep 60

./consoleAgentManager.sh configureToken $username $token

if ./consoleAgentManager.sh isConfigured
then
    echo "Secure Agent Configuration Successful"
else
    echo "Secure Agent Not Configured."
fi
