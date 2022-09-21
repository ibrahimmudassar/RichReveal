import requests;
from bs4 import BeautifulSoup;

#Retrieve Forbes page content
URL = "https://www.forbes.com/real-time-billionaires/#7ff1165e3d78";
page = requests.get(URL);
soup = BeautifulSoup(page.content, "html.parser");

#Retrieve age and name info from website and organize into dictionary
names = [];
billiInfo = {};
billionaires = soup.find_all("tr", class_="base ng-scope");

for billionaire in billionaires:
    age = int(billionaire.find("td", class_="age").find("span", class_="ng-binding").get_text())
    
    if(age not in billiInfo.keys()):
        billiInfo[age] = [[], 0];
    else:
        billiInfo[age][1] = billiInfo[age][1] + 1;

    name = billionaire.find("td", class_="name").find("a", class_="ng-binding").get_text();
    billiInfo[age][0].append(name);
