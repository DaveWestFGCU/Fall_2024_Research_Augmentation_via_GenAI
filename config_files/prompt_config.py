prompt = \
    {
        "name": "from dissimilar label",
        "query": f"Using the {dataset_details["text_source"]} \"{original_record["text"]}\" which portrays the emotion{original_record["label"]}, generate a {dataset_details["text_source"]} similar in style and content that instead portrays {target_label}. Only give the generated {dataset_details["text_source"]}."
    }