class Camera:
    def __init__(self):
        self.pics = []  
        
    def take_pic(self, name): 
        self.pics.append(name)
        print("الصورة تمام.")
        
cam = Camera()

cam.take_pic("صورتي")
cam.take_pic("سيلفي")

print(cam.pics)
