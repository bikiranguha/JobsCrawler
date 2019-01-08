import requests
from selenium import webdriver
from bs4 import BeautifulSoup

# target (want to initially get a list of all job postings from this careers section)
url = "https://careers.pnnl.gov/psc/hrmsx/EMPLOYEE/HRMS/c/HRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL?FOCUS=Applicant&"




####### ways to query a webpage

## using requests
#epri_jobs = requests.get("https://www.epri.com/#/careers/list")

#### using beautiful soup
#epri_soup = BeautifulSoup(epri_jobs.content, 'html.parser')
#epri_soup = BeautifulSoup(epri_jobs.content, 'lxml')
#job_name = epri_soup.find(class_="md-button md-no-style")
#print job_name.get_text()


# import dryscrape
# from bs4 import BeautifulSoup
# session = dryscrape.Session()
# my_url = "https://www.epri.com/"
# session.visit(my_url)
# response = session.body()
# soup = BeautifulSoup(response)
# soup.find(id="intro-text")

## using selenium webdriver (executes a headless browser to help with dynamic webpages)
# driver = webdriver.Chrome()
# driver.get(url)

# html = driver.execute_script("return document.documentElement.innerHTML")
# #soup = BeautifulSoup(html,"lxml")
# soup = BeautifulSoup(html.content,"html.parser")





# ## using urllib
# import urllib.request
# url = "https://www.epri.com/#/careers/list"
# with urllib.request.urlopen(url) as response:
#    html = response.read()
##############

######## ways to get the content written
"""
with open("epri.html", "w") as f:
    f.write(soup.text)
"""
#results = soup.select("a.md-no-style.md-button.md-orange-theme.md-ink-ripple")
#temp = soup.find(class_="md-no-style md-button md-orange-theme md-ink-ripple").get_text()
#print temp

"""
with open("epri.html", "w") as f:
    f.write(soup.text)
"""
######



##### spynner
# import spynner

# browser = spynner.Browser() 
# browser.load("http://www.wordreference.com") 
# browser.runjs("console.log('I can run Javascript!')") 
# browser.runjs("_jQuery('div').css('border', 'solid red')") # and jQuery! 
# browser.select("#esen") 
# browser.fill("input[name=enit]", "hola") 
# browser.click("input[name=b]") 
# browser.wait_page_load() 
# sprint browser.url, 
# len(browser.html) browser.close()
########


#### selenium phantomjs
from selenium import webdriver
import codecs
driver = webdriver.PhantomJS()
my_url = "https://www.epri.com/#/careers/list"
driver.get(my_url)

html = driver.page_source
f = codecs.open('abc.html','w', encoding='utf8')
f.write(html)
#f.write(u'\u201c')
"""
with open('abc.html','w') as f:
    f.write(html)
"""
#print type(html)
#p_element = driver.find_element_by_class_name('md-no-style.md-button.md-orange-theme.md-ink-ripple')
#print(p_element.text)
####