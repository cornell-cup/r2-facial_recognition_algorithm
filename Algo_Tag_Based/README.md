# r2-facial_recognition_algorithm Tag-Based
The main idea is to assign tags to faces in the face dataset (potentially in a decision tree structure) and try to run the test face image with decision tree and filter out the face with low probability of matching. 
The tagging algorithms can either be trained on the existing dataset, or use pre-existing packages. 
The tags contain two kinds: high priority ones, to cross out irrelevant faces; low priority ones, to determine probability
1. gender (high priority)
2. skin color (high priority)
3. wear glasses or not (low priority), greatly increase matching probability if both test and database face contains glasses
4. 
5. Facial Landmarks(low priority): locations of eyes, nose, mouth, etc.


When applying the filter, we can run all the little identification algorithm concurrently to achieve fastest speed.
After all potential filters have been applied to the test face, we can use another self-trained model to calculate the probability to match to each of the faces left, and choose the face with the highest probability.