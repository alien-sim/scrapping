from selenium import webdriver
from bs4 import BeautifulSoup
import pandas
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(executable_path="chromedriver.exe",options=chrome_options)

driver.get("https://www.flipkart.com/search?q=laptop%20ubuntu%20i5&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
products,prices,ratings = ([] for i in range(3))
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
	name=a.find('div', attrs={'class':'_3wU53n'})
	price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
	rating=a.find('div', attrs={'class':'hGSR34'})
	products.append(name.text)
	prices.append(price.text)
	try:
		ratings.append(rating.text) 
	except:
		ratings.append(rating)
driver.quit()

df = pandas.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
# df.to_csv('products.csv', index=False, encoding='utf-8')
print(df)

