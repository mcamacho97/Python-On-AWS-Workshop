import boto3

client = boto3.client("translate")

def translate_text(): # declare the function using def, name, braces for parameters and a colon
    response = client.translate_text(
        Text = 'I am learning to code in AWS',
        SourceLanguageCode = 'en',
        TargetLanguageCode = 'es'
    )
    print(response['TranslatedText'])

translate_text()
