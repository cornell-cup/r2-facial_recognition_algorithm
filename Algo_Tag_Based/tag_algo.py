import face_recognition
import glob
from PIL import Image, ImageDraw

face_landmarks_set = []

# generate facial landmark for all the members 
def import_facial_landmarks():
    print("Importing headshot...")
    for image_name in glob.glob('Face_set/*.JPG'):
        try:
            temp_image = face_recognition.load_image_file(image_name)
            temp_face_landmarks = face_recognition.face_landmarks(temp_image)[0]
            print(temp_face_landmarks)
            face_landmarks_set.append({
                "image_loc": image_name, "landmarks": temp_face_landmarks})
        except IndexError:
            print("I wasn't able to locate any faces in " + image_name + ". Check the image files. Aborting...")
    print("Headshot imported!")
    return face_landmarks_set

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

def save_drawn_pic(landmarks):
    for landmark in landmarks:
        img = Image.open(landmark["image_loc"])
        draw = ImageDraw.Draw(img)
        for key in landmark["landmarks"].keys():
            draw.point(landmark["landmarks"][key])
        img.save("test_set/" + landmark["image_loc"])

def main():
# reads image
    #face_recognition.face_landmarks(image)
    landmarks = import_facial_landmarks()
    #save_drawn_pic(landmarks)
    #high_gender()
    
main()
