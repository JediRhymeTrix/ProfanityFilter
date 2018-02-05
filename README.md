# ProfanityFilter
Simple profanity filter and sentiment classifier in python

## Instructions:
- ### Docker: 
    - Build: `docker-compose build` 
    - Run: `docker-compose up` 
- ### API: 
    - URL: [http://localhost:5000/](http://localhost:5000/) 
    - Endpoints:  
        - **/process** 
            * *request* - JSON in the following format:

                        ```json
                            {
                                "post": <text>,
                                "options": ["filter", "sentiment" / "sentiment_heavy"],
                                "url": <url of external newline-separated wordlist(optional)>
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
