# Anime-Downloader

An Automated Downloader that downloads episodes of the particular Anime, you want to Watch. Uses website [Animeout](http://www.Animeout.xyz)
Downloader Script Credits [Getit](http://www.github.com/ankitjain28may/getit)

## Installation

* Install `python` >= v3.0
	Download [Python](https://www.python.org/downloads/)

After Installing Python install these **packages**

* Install `selenium`

	```shell
	$pip install selenium
	```

* Install `colorama`
	
	```shell
	$pip install colorama
	```

* Install `Chromedriver`:- For Chrome Users
	Download `[Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)`

* Install `GeckoDriver`:- For FireFox Users
	Download `[GeckoDriver](https://github.com/mozilla/geckodriver/releases)`


## Usage

* Clone Both the Scripts into your desired location
* Put the _ChromeDriver_ or _GeckoDriver_ in the desired location after extraction
* Comment or Uncomment the desired **Webdriver** given in _setUp(self)_ function
* Put the path of the respective Driver in the Calling Function (Mentioned in the Comments)
* Run the script `adls.py` by using 
	```shell
		$ python adls.py
	```
* Write the name of the Anime you want to download.

Note:- The Episodes will be Downloaded in the same location where the scripts are presesnt. Desired Path Location will be added in future.
