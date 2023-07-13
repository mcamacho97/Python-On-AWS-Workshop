# Python...........................JSON
# dict.............................object
# list,tuple.......................array
# str..............................string
# int, float.......................number
# True.............................true
# False............................false
# None.............................null


# json.load() & json.dump() - Use to input and output JSON from files and into files
# json.loads() & json.dumps() - Use to input and output JSON from strings and into strings

import json

# This uses a json string as an input 
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]
}
"""

def main():
    json_input = json.loads(json_string)
    print(json_input)

if __name__ == "__main__":
    main()