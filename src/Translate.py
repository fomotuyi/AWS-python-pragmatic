import boto3

client = boto3.client('translate', region_name="us-east-1")
text = 'My name is omotuyi fiyinfoluwa'
result = client.translate_text(Text=text, SourceLanguageCode='en', TargetLanguageCode='es-ES')
print(result["TranslatedText"])