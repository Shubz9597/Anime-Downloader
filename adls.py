#Anime Downloader
#Comment or Uncomment respective web browser users
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import urllib.parse
from urllib.request import urlopen
import downloader
 
class AnimeDLR():

    def userInput(self):
        print("Which Anime You want to Download")
        self.name =input()
        return self.name

    def queryCreator(self,searchString):
        self.searchString = searchString
        self.query = urllib.parse.quote(self.searchString)

 
    def setUp(self, chromedriver):
        #For Chrome
        self.chromedriver =  chromedriver
        self.driver = webdriver.Chrome(self.chromedriver)
        #For FireFox
        #binary = FirefoxBinary('firefox')
        #self.driver = webdriver.Firefox(firefox_binary=binary)
 
    def urlOpen(self):
        driver = self.driver
        self.url = "https://www.animeout.xyz/?s="+self.query
        driver.get(self.url)
 
 
    def animeSelect(self):
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #Added if you want to scroll to the bottom
        self.searchNames = self.driver.find_elements_by_xpath('//article/div/div[@class="post-header"]/h3/a')
        self.episodes =[]
        for x in range(len(self.searchNames)):
            print (self.searchNames[x].text)
        print("Which Series to download")
        self.choice= int(input())
        self.searchNames[self.choice-1].click()
        epiList = self.driver.find_elements_by_link_text("Direct Download")
        if len(epiList) == 0:
            epiList = self.driver.find_elements_by_partial_link_text("Episode")
        print("From Which Episodes you want to download, If you are continuing the series, Enter 1 if you want the series from Start")
        seriesNo = int(input())
        for x in range((seriesNo-1), len(epiList)):
            qlink ="http://public.animeout.xyz"+((epiList[x].get_attribute('href')).split('/',1)[1])
            self.episodes.append(qlink)
        return self.episodes
    
 
    def shutDown(self):
        self.driver.quit()
 
 #Function Calling

if __name__ == "__main__":
    x = AnimeDLR()
    animeName = x.userInput()
    x.queryCreator(animeName)
    x.setUp("C:/chromedriver/chromedriver.exe") #Put your ChromeDriver driver path here
    x.urlOpen()
    list1= x.animeSelect()
    downloader.main(list1)
    x.shutDown()
    print(x.chromedriver)
