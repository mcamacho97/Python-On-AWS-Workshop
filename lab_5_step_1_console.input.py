import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText']) 

text = input("Provide the text you want to translate: ")
source_language_code = input("Provide the source language code: ")
target_language_code = input("Provide the target language code: ")

def main():
    translate_text(
        Text = text,
        SourceLanguageCode = source_language_code,
        TargetLanguageCode = target_language_code
    )

if __name__=="__main__":
    main()
