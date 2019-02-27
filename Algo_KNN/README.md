# r2-facial_recognition_algorithm_test3
A possible way to build our own facial recognition algorithm
Extract the face descriptors and use KNN to train our own classifier.

## Description
This algorithm uses KNN algorithm (K nearest neighbor) in machine learning to implement facial recognition.

### Ideas
Since this technique is non-parametric, it doesn't take any assumption of the data sets. The idea is that using KNN for classification, and detecting the faces with the highest similarities.

Also, since this is a small data set, we can actually do data filtering in advance to make the results more accurate.
For example, we can filter people by their races, therefore making it easier to implement the algorithm.

### Language used
python
### Steps
1. Obtains specific points that exist on every face
2. Use OpenCV’s affine transformation to do basic image transformations to make the eyes and lip, etc, always appear in the same location.
3. The face imaged are passed through a deep CNN to obtain a unit hypersphere.
4. Use ML classification method 
