import face_recognition
from PIL import Image

face_landmarks_set = []

# generate facial landmark for all the members 
def import_facial_landmarks():
    print("Importing headshot...")
    for image_name in glob.glob('Face_set/*.jpg'):
        try:
            temp_image = face_recognition.load_image_file(image_name)
            temp_face_landmarks = face_recognition.face_landmarks(temp_image)[0]
            face_landmarks_set.append(temp_face_landmarks)
        except IndexError:
            print("I wasn't able to locate any faces in " + image_name + ". Check the image files. Aborting...")
    print("Headshot imported!")

def high_gender(image):
    return 0

def high_skin_color(image):
    return 0

def high_skin_color(image):
    return 0

def high_meeting_times(image):
    return 0

def low_glasses(image):
    return 0

# return a list of possible people with probaility
def low_facial_landmarks(possible_list, image):

	face_landmarks_list = face_recognition.face_landmarks(image)

	# generate possibilty for all people in the possible_list
	
    return 0

def main():
# reads image
	face_recognition.face_landmarks(image)
    high_gender()
    
main()