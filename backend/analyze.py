from clarifai.rest import ClarifaiApp

# Create your API key in your account's `Manage your API keys` page:
# https://clarifai.com/developer/account/keys

app = ClarifaiApp(api_key='4fd793bbe57141c88ac881d6d7f10778:# QUESTION')

# You can also create an environment variable called `CLARIFAI_API_KEY`
# and set its value to your API key.
# In this case, the construction of the object requires no `api_key` argument.

app = ClarifaiApp()
