dataset = \
{
    "EmoEvent (English)" : {
        "id": "emoevent_en",
        "source": "https://github.com/fmplaza/EmoEvent",
        "text_source": "tweet",
        "filetype": "tsv",
        "location": "local",
        "is_split": False,
        "label_format": "single",
        "relpath": "./original_datasets/EmoEvent/en/emoevent_en.csv",
        "unused_columns": ["id", "offensive"],
        "remap_columns": {"tweet": "text", "emotion":"label"},
        "unlabeled_label": "others",
        "label_type": "emotion",
        "label_list": ["anger", "disgust", "fear", "joy", "sadness", "surprise"],
        "num_labelers": 3,
        "num_consensus": 2
    },
}
#{
#    "name": "EmoEvent (Spanish)",
#    "source": "https://github.com/fmplaza/EmoEvent",
#    "text_source": "tweet",
#    "filetype": "tsv",
#    "location": "local",
#    "is_split": True,
#    "label_type": "single",
#    "unused_columns": ["id", "event", "offensive"],
#    "remap_columns": {"tweet": "text", "emotion":"label"},
#    "unlabeled_label": "others"
#    #},
#    #{
#    "name": "GoEmotions",
#    "source": "https://github.com/google-research/google-research/tree/master/goemotions",
#    "filetype": "parquet",
#    "location": "HuggingFace",
#    "hf_name": "go_emotions",
#    "hf_subset": "raw"
#    #}
#    #synthetic_dataset_name = 'synthetic_datasets.parquet'
#synthetic_dataset_dir = 'synthetic_datasets/'
#
#
#