class Configuration(object):
    def __init__(self, timeout = 2, query = ""):
        self.PUBLICATIONS = ["CNN"] #list of publications to scrape
        self.MAX_ARTICLES = 300 # max article per listed publication. None for scraping all.
        self.START_DATE = "2025-07-25T18:03:04Z" #default to latest 
        self.END_DATE = "1923-07-25T18:03:04Z" #run till MAX_ARTICLES 
        
        self.timeout = timeout #number of seconds to stop after every request
        self.query = query
        self.headers =  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
 'Accept-Language': 'en-US,en;q=0.9',
 'Accept-Encoding': 'gzip, deflate, br'}