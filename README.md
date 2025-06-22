GitHub Trending Repositories Scraper
This Python script scrapes the top 5 trending repositories from GitHub and saves their names and links into a CSV file.

Features
Fetches the current trending repositories from https://github.com/trending.
Extracts the repository name and its direct link.
Saves the data into a trending_repos.csv file.
Prerequisites
Before running the script, ensure you have the following installed:

Python 3.x
requests library
BeautifulSoup4 library
You can install the required libraries using pip:

Bash

pip install requests beautifulsoup4
How to Use
Save the script: Save the provided Python code as, for example, github_trending.py.

Run the script: Open your terminal or command prompt, navigate to the directory where you saved the script, and run it using:

Bash

python github_trending.py
View the output: After running the script, a new file named trending_repos.csv will be created in the same directory. This CSV file will contain two columns: "Repository Name" and "Link", listing the top 5 trending GitHub repositories.

Example trending_repos.csv Output
Code snippet

Repository Name,Link
owner1/repo1,https://github.com/owner1/repo1
owner2/repo2,https://github.com/owner2/repo2
owner3/repo3,https://github.com/owner3/repo3
owner4/repo4,https://github.com/owner4/repo4
owner5/repo5,https://github.com/owner5/repo5
Disclaimer
This script is intended for educational and personal use to demonstrate web scraping. Please be mindful of GitHub's terms of service when accessing their website. Excessive or automated scraping may lead to your IP being blocked.
