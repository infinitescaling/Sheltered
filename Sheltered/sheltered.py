import os

def find_picture():
    picture_list = []
    print('cwd file path is ' + os.getcwd())
    print('Filepath is ' + os.path.join(os.getcwd(),"Sheltered/static/images/"))
    for filename in os.listdir(os.path.join(os.getcwd(),"Sheltered/static/images/")):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            picture_list.append(os.path.join("/static/images",filename))
    return picture_list

