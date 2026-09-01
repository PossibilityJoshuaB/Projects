import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

pythonJobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
pythonJobCards = [
    h2_element.parent.parent.parent for h2_element in pythonJobs
]

for jobCard in pythonJobCards:
    titleElement = jobCard.find("h2", class_="title")
    companyElement = jobCard.find("h3", class_="company")
    locationElement = jobCard.find("p", class_="location")
    link = jobCard.find_all("a", class_="card-footer-item")[1]["href"]
    print(titleElement.text.strip())
    print(companyElement.text.strip())
    print(locationElement.text.strip())
    print(f"Apply here {link}")


