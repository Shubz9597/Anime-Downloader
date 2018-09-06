from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import urllib.parse
from urllib.request import urlopen
import downloader
 
class AnimeDLR():

    def userInput(self):
        print("\n")
        print("Which Anime You want to Download")
        self.name =input()
        return self.name

    def queryCreator(self,searchString):
        self.searchString = searchString
        self.query = urllib.parse.quote(self.searchString)

 
    def setUp(self, chromedriver):
        self.chromedriver =  chromedriver
        self.driver = webdriver.Chrome(self.chromedriver)
        #binary = FirefoxBinary('firefox')
        #self.driver = webdriver.Firefox(firefox_binary=binary)
 
    def urlOpen(self):
        driver = self.driver
        self.url = "https://www.animeout.xyz/?s="+self.query
        #print(self.url)
        driver.get(self.url)
        # search = driver.find_element_by_id("s")
        # search.send_keys(self.searchItem)
        # search.send_keys(Keys.RETURN)
 
 
    def animeSelect(self):
        searchNames = self.driver.find_elements_by_xpath('//article/div/div[@class="post-header"]/h3/a')
        self.episodes =[]
        for x in range(len(searchNames)):
            print (searchNames[x].text)
        print("Which Series to download")
        choice= int(input())
        searchNames[choice-1].click()
        epiList = self.driver.find_elements_by_link_text("Direct Download")
        for x in range(len(epiList)):
            qlink ="http://public.animeout.xyz"+ ((epiList[x].get_attribute('href')).split('/',1)[1])
            self.episodes.append(qlink)
            print(self.episodes[x])

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
