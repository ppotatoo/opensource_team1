import openai
import googletrans

translator = googletrans.Translator()

def getImage(user_query):
    en_title = translator.translate(user_query, src='ko', dest='en').text
    response = openai.Image.create(
        prompt = en_title +', digital art',
        n=1,
        size="256x256"
    )
    return response["data"][0]["url"]