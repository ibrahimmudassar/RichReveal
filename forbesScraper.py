import collections;
from bs4 import BeautifulSoup;
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
import pandas as pd;
import matplotlib.pyplot as plt;


#Retrieve Forbes page content
URL = "https://www.forbes.com/real-time-billionaires/";
#page = requests.get(URL);
browser = webdriver.Chrome(ChromeDriverManager().install());
browser.get(URL);
html = browser.page_source;
soup = BeautifulSoup(html, "lxml");
#print(soup.prettify());

#Retrieve age and name info from website and organize into dictionary
names = [];
billiInfo = {};
billionaires = soup.find_all("tr", class_="base ng-scope");

for billionaire in billionaires:
    age = int(billionaire.find("td", class_="age").find("span", class_="ng-binding").get_text())
    
    if(age not in billiInfo.keys()):
        billiInfo[age] = [[], 1];
    else:
        billiInfo[age][1] = billiInfo[age][1] + 1;

    name = billionaire.find("td", class_="name").find("a", class_="ng-binding").get_text();
    billiInfo[age][0].append(name);

orderedBilliInfo = collections.OrderedDict(sorted(billiInfo.items()));
#print(billiInfo);

ageFreq = pd.DataFrame(orderedBilliInfo);

frequencies = ageFreq.iloc[1];
