A possible way to build our own facial recognition algorithm:

Extract the face descriptors and use KNN to train our own classifier.
get the cropped face picture

1. Obtains specific points that exist on every face
2. Use OpenCV’s affine transformation to do basic image transformations to make the eyes and lip, etc, always appear in the same location.
3. The face imaged are passed through a deep CNN to obtain a unit hypersphere.
4. Use ML classification method 
