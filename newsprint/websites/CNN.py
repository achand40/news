class CNN(object): 
    def __init__(self, config): 
       self.config = config
       self.helper = Helpers()

    def retreive_article_data_cnn(self, json_object): 
        """
        input: the JSON response from the CNN API 
        output: a dictionary of all the parsed data
        """
        if json_object['type'] == "article":
            article_body = json_object['body']
            article_title = json_object['headline']
            article_published_date_first = json_object['firstPublishDate'] #ISO 8601
            article_published_date_latest = json_object['lastModifiedDate'] #ISO 8601
            try:
              article_location = json_object['location']
            except: 
                article_location = None
            article_category = json_object['section']
            article_authors = json_object['contributors'] #list of strings 
            article_thumbnail_image_url = json_object['thumbnail']
            article_url = json_object['url']
            list_of_tags = []
            for item in json_object['tags']:
                list_of_tags.append(item['label'])
        else: 
            return {}
            
        return {"Body" : article_body, "Title" : article_title, "Initial_Date" : article_published_date_first, "Latest_Date" : article_published_date_first,
            "Location" : article_location, "Category" : article_category, "Section" : article_category, "Authors" : article_authors, 
             "Thumbnail_Image" : article_thumbnail_image_url, "Article_URL" : article_url, "Tags" : list_of_tags}

    def make_request(self, current_page, search_query = None): 
        base_url = "https://search.api.cnn.com/"
        if search_query is None: 
           search_query = ""
        start_url =  base_url + "content?q=" + str(search_query) +"&size=50&from=0&page=1"  + str(current_page) + "&sort=newest"
        resp = requests.get(start_url, headers = self.config.headers).json()
        return resp

    def get_data(self, response): 
         major_dict = []
         for item in response['result']: 
             if self.config.START_DATE is not None and self.helper.compare_dates_iso(self.config.START_DATE, item["firstPublishDate"]): 
                if self.config.END_DATE is not None and not self.helper.compare_dates_iso(self.config.END_DATE, item["firstPublishDate"]):
                     data = self.retreive_article_data_cnn(item)
                     if len(data) > 1:
                         major_dict.append(data)

             

         return major_dict

      
            

         
         

        



    