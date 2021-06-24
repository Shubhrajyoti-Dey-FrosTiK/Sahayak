# Sahayak

This is a discord bot which will help people to get notifications about the available vaccine slots near its locality/ District. 
User will get notifications after a fixed interval of time specified by user about the slots available.

## Usage

In the discord app 

Go to the link of your bot and invite the bot to the server
Type `-hi` and press enter to get the welcome message
All the instructions about the command will be given there

# Installation for Development

## Dependencies :

<B> Python Version installed should be 3.x.x </B>

### BeautifulSoup4 :
```
`pip install beautifulsoup4`
```

### Selenium :
 ```
For Windows : `pip install selenium`
For Mac/Linux : `pip3 install selenium`
```

### ChromeDriver :
```
https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver
```
Sometimes you need to download the chromedriver file also for executioin of Chromedriver
```
https://chromedriver.chromium.org/downloads
```
Download it and keep it in the project directory

### Discord :
```
pip install discord
```

### Asyncio :

Generally this module is present inside Python itself but if module error comes install it
```
pip install asyncio
```

## After the Installations

Fork this repo and put it in a directory

Change the `YOUR_TOKEN` in `Connect.py` to your Token of Discord

Run `Connect.py` to start the bot server to accept requests from user
