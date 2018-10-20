from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='a2596d582f04477d847353f2c60e4ed1')

# get the general model
model = app.models.get("general-v1.3")

# predict with the model
print(model.predict_by_url(url='https://scontent-ort2-1.xx.fbcdn.net/v/t1.0-9/27654941_592960624369581_6880587150061114791_n.jpg?_nc_cat=103&_nc_ht=scontent-ort2-1.xx&oh=f924f97b0fdd21d054056763988861c1&oe=5C5CEBE7').outputs.data.concepts)
