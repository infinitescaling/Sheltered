import os

def find_picture():
    picture_list = []
    for filename in os.listdir(os.path.join(os.getcwd(),"static/images/")):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            picture_list.append(os.path.join("/static/images",filename))
    return picture_list

