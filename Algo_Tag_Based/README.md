# r2-facial_recognition_algorithm Tag-Based
The main idea is to assign tags to faces in the face dataset (potentially in a decision tree structure) and try to run the test face image with decision tree and filter out the face with low probability of matching. 
The tagging algorithms can either be trained on the existing dataset, or use pre-existing packages. 
The tags contain two kinds: high priority ones, to cross out irrelevant faces; low priority ones, to determine probability
1. Gender (high priority): in use of the voice recognition
2. Hair color (high priority)
3. Skin color (high priority)
4. Meeting Times(high priority): if someone one a different meeting time wants to sign in, parse him/her out
5. Wear glasses or not (low priority), greatly increase matching probability if both test and database face contains glasses
6. Facial Landmarks(low priority): locations of eyes, nose, mouth, etc. 

When applying the filter, we can run all the little identification algorithm concurrently to achieve fastest speed.
After all potential filters have been applied to the test face, we should get a probabiilty for all the faces that is left from the high priority tags. And we will choose the highest one.

# Algorithms for tagging algorithm
All the tagging algorithm will have the input of the test image, output of the list of names matched with the corresponsing tag. We will do a AND operation for all the lists of 
1. Gender: Result passed from the Voice Recognition module (detecting the gender of the voice "Check me in")
2. Hair color: 
3. Skin color: 