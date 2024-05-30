encode = {
    'admiration': 0,
    'amusement': 1,
    'anger': 2,
    'annoyance': 3,
    'approval': 4,
    'caring': 5,
    'confusion': 6,
    'curiosity': 7,
    'desire': 8,
    'disappointment': 9,
    'disapproval': 10,
    'disgust': 11,
    'embarrassment': 12,
    'excitement': 13,
    'fear': 14,
    'gratitude': 15,
    'grief': 16,
    'joy': 17,
    'love': 18,
    'nervousness': 19,
    'optimism': 20,
    'pride': 21,
    'realization': 22,
    'relief': 23,
    'remorse': 24,
    'sadness': 25,
    'surprise': 26,
    'neutral': 27
}

inverse_encode = {
    0: 'admiration',
    1: 'amusement',
    2: 'anger',
    3: 'annoyance',
    4: 'approval',
    5: 'caring',
    6: 'confusion',
    7: 'curiosity',
    8: 'desire',
    9: 'disappointment',
    10: 'disapproval',
    11: 'disgust',
    12: 'embarrassment',
    13: 'excitement',
    14: 'fear',
    15: 'gratitude',
    16: 'grief',
    17: 'joy',
    18: 'love',
    19: 'nervousness',
    20: 'optimism',
    21: 'pride',
    22: 'realization',
    23: 'relief',
    24: 'remorse',
    25: 'sadness',
    26: 'surprise',
    27: 'neutral'
}

ekman_conversion = {
    # Anger
    'anger': 'anger',
    'annoyance': 'anger',
    'disapproval': 'anger',

    # Disgust
    'disgust': 'disgust',

    # Fear
    'fear': 'fear',
    'nervousness': 'fear',

    # Joy
    'joy': 'joy',
    'admiration': 'joy',
    'amusement': 'joy',
    'approval': 'joy',
    'caring': 'joy',
    'desire': 'joy',
    'excitement': 'joy',
    'gratitude': 'joy',
    'love': 'joy',
    'optimism': 'joy',
    'pride': 'joy',
    'relief': 'joy',

    # Sadness
    'sadness': 'sadness',
    'disappointment': 'sadness',
    'embarrassment': 'sadness',
    'grief': 'sadness',
    'remorse': 'sadness',

    # Surprise
    'surprise': 'surprise',
    'confusion': 'surprise',
    'curiosity': 'surprise',
    'realization': 'surprise',

    # Neutral
    'neutral': 'neutral'
}

ekman_encode = {
    'anger': 0,
    'disgust': 1,
    'fear': 2,
    'joy': 3,
    'sadness': 4,
    'surprise': 5,
    'neutral': 6
}

inverse_ekman_encode = {
    0: 'anger',
    1: 'disgust',
    2: 'fear',
    3: 'joy',
    4: 'sadness',
    5: 'surprise',
    6: 'neutral'
}