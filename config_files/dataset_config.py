dataset = \
    [
        {
            "name": "EmoEvent (English)",
            "source": "https://github.com/fmplaza/EmoEvent",
            "text_source": "tweet",
            "filetype": "tsv",
            "location": "local",
            "is_split": False,
            "label_type": "single",
            "relpath": "./original_datasets/EmoEvent/en/emoevent_en.csv",

            "train_relpath": "./original_datasets/EmoEvent/en/train.tsv",
            "test_relpath":  "./original_datasets/EmoEvent/en/test.tsv",
            "dev_relpath":   "./original_datasets/EmoEvent/en/dev.tsv",
            "unused_columns": ["id", "offensive"],
            "remap_columns": {"tweet": "text", "emotion":"label"},
            "unlabeled_label": "others"
        },
        #{
        #    "name": "EmoEvent (Spanish)",
        #    "source": "https://github.com/fmplaza/EmoEvent",
        #    "text_source": "tweet",
        #    "filetype": "tsv",
        #    "location": "local",
        #    "is_split": True,
        #    "label_type": "single",
        #    "train_relpath": "./original_datasets/EmoEvent/es/train.tsv",
        #    "test_relpath":  "./original_datasets/EmoEvent/es/test.tsv",
        #    "dev_relpath":   "./original_datasets/EmoEvent/es/dev.tsv",
        #    "unused_columns": ["id", "event", "offensive"],
        #    "remap_columns": {"tweet": "text", "emotion":"label"},
        #    "unlabeled_label": "others"
        #},
        #{
        #    "name": "GoEmotions",
        #    "source": "https://github.com/google-research/google-research/tree/master/goemotions",
        #    "filetype": "parquet",
        #    "location": "HuggingFace",
        #    "hf_name": "go_emotions",
        #    "hf_subset": "raw"
        #}
    ]


#synthetic_dataset_name = 'synthetic_datasets.parquet'
#synthetic_dataset_dir = 'synthetic_datasets/'
#
#
#