import turicreate as tc
import os

# Load images
data = tc.image_analysis.load_images('asianwomen', with_path=True)
testImage = tc.image_analysis.load_images('tetsdata')
# From the path-name, create a label column
data['label'] = data['path'].apply(lambda path: 'lw' if '/lw' in path  else 'feifei' if '/Lifeifei' in path
                                                 else 'hs' if '/hs' in path else 'xmy' )

# Save the data for future use
data.save('asianw.sframe')

# Load the data
data = tc.SFrame('asianw.sframe')

# Create the model
model = tc.image_classifier.create(data, target='label')

# Save predictions to an SArray
predictions = model.predict(testImage)
print(testImage)
print("The prediction is:" , predictions)

# Save the model for later use in Turi Create
model.save('asianModel.model')

# Export for use in Core ML
model.export_coreml('MyCustomImageClassifier.mlmodel')