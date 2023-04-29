import openai

def getImage(text):
    response = openai.Image.create(
        prompt=text,
        n=1,
        size="256x256"
    )
    return response["data"][0]["url"]