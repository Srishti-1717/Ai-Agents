def get_openai_api_key():
    return "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"

import json

def pretty_print_result(result):
    """
    Nicely prints the result in JSON format with indentation.
    
    Args:
        result (dict): The result to be printed.
    """
    try:
        print(json.dumps(result, indent=4, ensure_ascii=False))
    except (TypeError, ValueError):
        print("Unable to pretty print result. Here is the raw output:")
        print(result)


import os

import os

def get_serper_api_key():
    key = os.getenv("SERPER_API_KEY")
    if not key:
        raise ValueError("SERPER_API_KEY not found in environment variables.")
    return key
