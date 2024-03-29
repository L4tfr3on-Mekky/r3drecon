#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${YELLOW}"
echo "======================================================="
echo "           Welcome to r3drecon Installer             "
echo "======================================================="
echo -e "${NC}"
apt-get install shc
apt-get install jq
apt-get install unzip
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/OWASP/Amass/v3/...@master
go install github.com/ffuf/ffuf@latest
go install -v github.com/lukasikic/subzy@latest
wget https://github.com/findomain/findomain/releases/latest/download/findomain-linux.zip
unzip findomain-linux.zip  
mv findomain $HOME/go/bin
chmod 777 $HOME/go/bin/findomain
go install github.com/tomnomnom/httprobe@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

shc -f r3drecon.sh   
mv r3drecon.sh.x r3drecon
cp r3drecon $HOME/go/bin
chmod 777 $HOME/go/bin/r3drecon
rm -rf r3drecon.sh   

wget https://wordlists-cdn.assetnote.io/data/automated/httparchive_subdomains_2020_11_18.txt -O  subdomains.txt
mv subdomains.txt /usr/share/wordlists/
chmod 777 /usr/share/wordlists/subdomains.txt
