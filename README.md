# ProfanityFilter
Simple profanity filter and sentiment classifier in python

NOTE: To add words to the database, add the newline separated words to `data/feed_list.txt` and run `FeedList.py` with 2-letter language code as command line
argument. \
eg. `python FeedList.py -l en`
## Instructions:

- <h3>Docker:</h3> 
    - Build: `docker-compose build` 
    - Run: `docker-compose up` 
- ### API: 
    - URL: [http://localhost:5000/](http://localhost:5000/) 
    - Endpoints:  
        - **/process** ```["POST"]```
            * *request* - JSON in the following format:
            
                        ````json
                            {
                                "post": <text>,
                                "options": ["filter", "sentiment" / "sentiment_heavy"],
                                "wordlist_url": <url of external newline-separated wordlist(optional)>,
                                "ignore_words_url": <url of newline-separated list of words to ignore(optional)>
                            }
                        ```
            * *response* - JSON in the following format:
                        
                        if "sentiment" in request:
                        ```json
                            {
                                "profanities": [<list of words found>],
                                "sentiment": 
                                    {
                                        "confidence": "med" / "high" / "low",
                                        "polarity": -1 to +1 (-ve to +ve)
                                    }
                            }
                        ```

                    
                        if "sentiment_heavy" in request:
                        ```json
                            {
                                "profanities": [<list of words found>],
                                "sentiment": 
                                    {
                                        "polarity": -1 to +1 (-ve to +ve)
                                    }
                            }
                        ```


        **NOTE**: ```sentiment_heavy``` is *slow* but more accurate. use ```sentiment``` first and then ```sentiment_heavy``` can be used based on the confidence level returned.
        
        Meanings of *confidence levels*:
        - high: **high polarity** and **low subjectivity**
        - med: **high polarity** and **high subjectivity** (classification is mostly correct but exact score may be inaccurate) - ```sentiment_heavy``` might give a better score.
        - low: **low polarity** and **high subjectivity** - low accuracy possible. Use ```sentiment_heavy``` instead.


    ## Examples:

    1. 
    ```json
    req: {
	        "post": "Well, I completely disagree with this “wonderful” lady who doesn’t know anything and acts like she has never set foot in Spain. God, I’d like to gag her! fuck chutiya",
	        "options": ["filter"],
         }

    res: {
            "profanities": [
                "fuck",
                "chutiya"
            ],
            
        }
    ```
    
    2. 
    ```json
    req: {
	        "post": "Well, I completely disagree with this “wonderful” lady who doesn’t know anything and acts like she has never set foot in Spain. God, I’d like to gag her! fuck chutiya",
	        "options": ["filter"],
            "url": "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en"
         }

    res: {
            "profanities": [
                "fuck",
                "chutiya"
            ],
            
        }
    ```

    3. 
    ```json
    req: {
	        "post": "Well, I completely disagree with this “wonderful” lady who doesn’t know anything and acts like she has never set foot in Spain. God, I’d like to gag her! fuck chutiya",
	        "options": ["filter", "sentiment"],
            "url": "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en"
         }

    res: {
            "profanities": [
                "fuck",
                "chutiya"
            ],
            "sentiment": {
                "confidence": "low",
                "polarity": 0.2
            }
         }
    ```

    4. 
    ```json
    req: {
	        "post": "Well, I completely disagree with this “wonderful” lady who doesn’t know anything and acts like she has never set foot in Spain. God, I’d like to gag her! fuck chutiya",
	        "options": ["filter", "sentiment_heavy"],
            "url": "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en"
         }

    res: {
            "profanities": [
                "fuck",
                "chutiya"
            ],
            "sentiment": {
                "polarity": -0.8
            }
         }
    ```
