prompt = \
    {
        "EmoEvent (Raw)" :
            {
                'text' :
                    """
                    The following is a tweet portraying <original_record.labels>. 
                    \"<original_record.text>\"
                    Using this tweet, generate a tweet about the same subject and similar in style that instead portrays <target_label>. Only give the generated tweet.
                    """,

                'labels' :
                    """
                    Classify the tweet \"<synthetic_text>\" by the single most represented emotion ONLY from the following list:
                    1. Anger (also includes annoyance, rage)
                    2. Disgust (also includes disinterest, dislike, loathing)
                    3. Fear (also includes apprehension, anxiety, terror)
                    4. Joy (also includes serenity, ecstasy)
                    5. Sadness (also includes pensiveness, grief)
                    6. Surprise (also includes distraction, amazement)
                    Give only the label.
                    """
            },

        "EmoEvent (Tokenized)" :
            {
                'text' :
                    """
                    The following is a tweet with any usernames, names, hashtags, and URLs tokenized with an all-caps generalized term. 
                    \"<original_record.text>\"
                    Using this tweet, which portrays the emotion <original_record.labels>, generate a tweet about the same subject and similar in style that instead portrays <target_label>. Only give the generated tweet.
                    """,

                'text_response_start' :
                    "Here is a similar tweet portraying <target_label>:\n\n\"",

                'labels' :
                    """
                    Classify the tweet \"<synthetic_text>\" by the single most represented emotion ONLY from the following list:
                    1. Anger (also includes annoyance, rage)
                    2. Disgust (also includes disinterest, dislike, loathing)
                    3. Fear (also includes apprehension, anxiety, terror)
                    4. Joy (also includes serenity, ecstasy)
                    5. Sadness (also includes pensiveness, grief)
                    6. Surprise (also includes distraction, amazement)
                    Give only the label.
                    """
            },

        "enISEAR" :
            {
                'text' :
                    """
                    The following is a sentence portraying the emotion <original_record.labels>: 
                    \"<original_record.text>\"
                    Using this sentence, create a sentence about the same subject and similar in style that instead portrays <target_label>. Only give the generated sentence.
                    """,

                'labels' :
                    """
                    Classify the sentence \"<synthetic_text>\" by the single most represented emotion ONLY from the following list:"
                    1. Anger
                    2. Disgust
                    3. Fear
                    4. Guilt
                    5. Joy
                    6. Sadness
                    7. Shame
                    Give only the label.
                    """
            },

        "StackOverflow" :
            {
                'text' :
                    """
                    
                    """,

                'labels' :
                    """
                    Classify the Stack Overflow post \"<synthetic_text>\" by the single most represented emotion ONLY from the following list:"
                    1. ANGER
                    2. FEAR
                    3. JOY
                    4. LOVE
                    5. SADNESS
                    6. SURPRISE
                    Give only the label.
                    """
            }
    }