import requests
from bs4 import BeautifulSoup
import re


def get_wayback_url(url):
    return f"https://web.archive.org/save/{url}"


def save_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)


def spider(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract subdomains
    subdomains = set()
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and domain in href:
            subdomain = urlparse(href).netloc.split(domain)[0]
            subdomains.add(subdomain)

    return subdomains


def js_finder(url):
    response = requests.get(url)
    html_content = response.text
    js_files = re.findall(r'<script.?src=["\'](.?)["\']', html_content)
    return js_files


def main():
    # Get input from the user
    elephant_name = input("Enter the name of the elephant: ")
    url = f"https://{elephant_name}.example.com"

    # Spider to find subdomains
    subdomains = spider(url)
    subdomains_output = "\n".join(subdomains)
    save_to_file("subdomains.txt", subdomains_output)

    # JS Finder to find JS files
    js_files = js_finder(url)
    js_files_output = "\n".join(js_files)
    save_to_file("js_files.txt", js_files_output)

    # Wayback Machine URL
    wayback_url = get_wayback_url(url)
    print("Wayback Machine URL:", wayback_url)


if _name_ == "_main_":
    main()
