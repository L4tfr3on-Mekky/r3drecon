<h1 align="center">
  <br>
  <a href="https://www.linkedin.com/in/abdelrahem-mekky-0917871a6/"><img src="images/logo.JPG" alt="r3drecon"></a>
</h1>
<h4 align="center">Streamline your recon and vulnerability detection process with r3drecon,
A recon and initial vulnerability detection tool built using shell script and open source tools.</h4>
<br>

<p align="center">
  <a href="#how-it-works-">How it works</a> •
  <a href="#install-r3drecon">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#modes">MODES</a> •
  <a href="#for-developers">For Developers</a> •
  <a href="#credits">Credits</a> 
</p>




 
Introducing r3drecon, a powerful recon and initial vulnerability detection tool for Bug Bounty Hunters. Built using a variety of open-source tools and a shell script, r3drecon allows you to quickly and efficiently run a scan on the target domain and identify potential vulnerabilities.

r3drecon begins by performing recon on the target system, collecting information such as subdomains, and running services with nuclei. It then uses this information to scan for known vulnerabilities and potential attack vectors, alerting you to any high-risk issues that may need to be addressed.

In addition, r3drecon also includes features for identifying misconfigurations and insecure default settings with nuclei templates, helping you ensure that your systems are properly configured and secure.

r3drecon is an essential tool for conducting thorough and effective recon and vulnerability assessments.
Let's Find Bugs with r3drecon


  

  
## How it Works ?
This tool mainly performs 3 tasks
1. Effective Subdomain Enumeration from Various Tools
2. Get URLs with open HTTP and HTTPS service.
3. Run a Nuclei and other scans on previous output
So basically, this is an autmation script for your initial recon in bugbounty
  
## Install r3drecon
   r3drecon requires different tools to run successfully. Run the following command to install the latest version with all requirments-

 ```sh
git clone https://github.com/L4tfr3on/r3drecon_V_1.1.git
cd r3drecon
bash install.sh
```
  
## Usage 

```sh
r3drecon -h
```
This will display help for the tool. Here are all the switches it supports.
  
```console
[ABOUT:]
   Streamline your recon and vulnerability detection process with r3drecon,
   A recon and initial vulnerability detection tool built using shell script and open source tools.


[Usage:]
   r3drecon [MODE] [FLAGS]
   r3drecon -m EXP -d target.com -c /path/to/config.yaml


[MODES:]
    ['-m'/'--mode']
         Available Options for MODE: 
         SUB | sub | SUBDOMAIN | subdomain           Run r3drecon in SUBDOMAIN ENUMERATION mode
         URL | url                                   Run r3drecon in URL ENUMERATION mode
         EXP | exp | EXPLOIT | exploit               Run r3drecon in Full Exploitation mode


         Feature of EXPLOI mode :                    subdomain enumaration, URL Enumeration,
                                                     Vulnerability Detection with Nuclei,
                                                     and Scan for SUBDOMAINE TAKEOVER

[FLAGS:]
    [TARGET:]   -d, --domain    target domain to scan

    [CONFIG:]   -c, --config    path of your configuration file for subfinder

    [HELP:]     -h, --help      to get help menu  
      
    [UPDATE:]   -u, --update    to update tool
  
[Examples:]
     Run r3drecon in full Exploitation mode
         r3drecon -m EXP -d target.com


     Use your own CONFIG file for subfinder
         r3drecon -m EXP -d target.com -c /path/to/config.yaml


     Run r3drecon in SUBDOMAIN ENUMERATION mode
         r3drecon -m SUB -d target.com


     Run r3drecon in URL ENUMERATION mode
         r3drecon -m SUB -d target.com

```

  
## MODES 
### 1. FULL EXPLOITATION MODE <br>
Run r3drecon in FULL EXPLOITATION MODE
```sh
  r3drecon -m EXP -d target.com
```
  
FULL EXPLOITATION MODE contains following functions
- Effective Subdomain Enumeration with different services and open source tools
- Effective URL Enumeration ( HTTP and HTTPs service )
- Run Vulnerability Detection with Nuclei
- Subdomain Takeover Test on previous results
<br>
  
### 2. SUBDOMAIN ENUMERATION MODE <br>
Run r3drecon in SUBDOMAIN ENUMERATION MODE
```sh
  r3drecon -m SUB -d target.com
```
SUBDOMAIN ENUMERATION MODE contains following functions
- Effective Subdomain Enumeration with different services and open source tools
- You can use this mode if you only want to get subdomains from this tool
  or we can say Automation of Subdmain Enumeration by different tools
<br>
  
### 3. URL ENUMERATION MODE <br>
Run r3drecon in URL ENUMERATION MODE
```sh
  r3drecon -m URL -d target.com
```
URL ENUMERATION MODE contains following functions
  - Same Feature as SUBDOMAIN ENUMERATION MODE but also identifies HTTP or HTTPS service
  
Using your own CONFIG File for subfinder
```sh
  r3drecon -m EXP -d target.com -c /path/to/config.yaml
```
You can also provie your own CONDIF file with your API Keys for subdomain enumeration with subfinder
  
Updating tool to latest version
You can run following command to update tool
```sh
  r3drecon -u
```
### 3. ENCODING PYTHON V1  <br>

you can uses this script to 
1-URL-encoded
2-Hex-encoded
3-Base64-encoded
4-HTML-encoded
5-UTF-8-encoded
6-UTF-16-encoded
7-UTF-32-encoded
8-ASCII-encoded
9-Unicode-encoded


You can run following command to run encoding script
```sh
  python3 encode.py
```

An Example of config.yaml
```yaml
binaryedge:
  - 0bf8919b-aab9-42e4-9574-d3b639324597
  - ac244e2f-b635-4581-878a-33f4e79a2c13
censys:
  - ac244e2f-b635-4581-878a-33f4e79a2c13:dd510d6e-1b6e-4655-83f6-f347b363def9
certspotter: []
passivetotal:
  - sample-email@user.com:sample_password
securitytrails: []
shodan:
  - AAAAClP1bJJSRMEYJazgwhJKrggRwKA
github:
  - ghp_lkyJGU3jv1xmwk4SDXavrLDJ4dl2pSJMzj4X
  - ghp_gkUuhkIYdQPj13ifH4KA3cXRn8JD2lqir2d4
zoomeye:
  - zoomeye_username:zoomeye_password
```
  
## For Developers
If you have ideas for new functionality or modes that you would like to see in this tool, you can always submit a pull request (PR) to contribute your changes.
  
If you have any other queries, you can always contact me on <a href="https://www.linkedin.com/in/abdelrahem-mekky-0917871a6/">linkedin(l4tfr3on) </a>
  

## Credits
I would like to express my gratitude to all of the open source projects that have made this tool possible and have made recon tasks easier to accomplish.
