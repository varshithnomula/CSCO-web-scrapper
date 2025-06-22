import requests
from bs4 import BeautifulSoup
import csv

url = "https://github.com/trending"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the top 5 trending repositories (each is inside an <article> with class 'Box-row')
repos = soup.find_all("article", class_="Box-row")[:5]

# Open a CSV file to write repository names and links
with open("trending_repos.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Repository Name", "Link"])  
    
    # Extract and write repository name and link for each of the top 5 repos
    for r in repos:
        f_name = r.h2.a["href"].strip()           # Extract the relative URL of the repo
        name = f_name.strip("/")                 
        link = f"https://github.com{f_name}"      
        writer.writerow([name, link])             
