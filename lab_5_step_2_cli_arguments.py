import argparse # argparse is a built in python package, we add it with an import statement
import boto3

# Define the parser variable to equal argparse.ArgumentParser()
parser = argparse.ArgumentParser(description="Provides translation between one souurce language and another of the same set of languages.") 

# Add each of the arguments to the parser.add_argument() method
parser.add_argument("--text", type=str, dest="Text",     help="The text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character set, this may be fewer than 5,000 characters", required=True)
parser.add_argument("--source-language-code", type=str, dest="SourceLanguageCode", help="The language code for the language of the source text. The language must be a language supported by Amazon Translate", required=True)
parser.add_argument("--target-language-code", type=str, dest="TargetLanguageCode", help="The language code for the language of the target text. The language must be a language supported by Amazon Translate", required=True)

# This will inspect the command line, convert each argument to the appropriate type, and then invoke the appropriate action
args = parser.parse_args()

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)

def main():
    translate_text(**vars(args))

if __name__=="__main__":
    main()


# To run this file: python lab_5_step_2_cli_arguments.py --text "we are learning python on AWS" --source-language-code en --target-language-code fr
