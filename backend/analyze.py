from clarifai import rest
from clarifai.rest import ClarifaiApp
import server_config

# Create your API key in your account's `Manage your API keys` page:
# https://clarifai.com/developer/account/keys

app = ClarifaiApp(api_key=server_config.CLARIFAI_TOKEN)
# get the general model
model = app.models.get("general-v1.3")

# predict with the model
model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
