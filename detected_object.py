import numpy as np
import math

class DetectedObject:
    
    def __init__(self, idx_image, x_rel, y_rel, obj, target, c, r):
        self.idx_image = idx_image
        self.x_rel = x_rel
        self.y_rel = y_rel        
        self.obj = obj
        self.c = c
        self.r = r
        self.is_target = (obj == target)

        pos_img = np.array([[-c, -r], [0, -r], [-c, 0], [0, 0], [-int(c/2), -int(r/2)]])
        pos_rel = np.array([x_rel, y_rel]) 
        pos = pos_img[idx_image] + pos_rel
        self.x = pos[0]
        self.y = -pos[1]
        
    def pos_pix(self):
        c = self.c
        r = self.r
        inizio_immagine = np.array([[0, 0], [c, 0], [0, r], [c, r], [int(c/2), int(r/2)]])
        
        pos_pix = np.array([self.x_rel, self.y_rel]) + inizio_immagine[self.idx_image]
        x = pos_pix[0]
        y = pos_pix[1]
        return x, y
    
    def norm(self):
        pos = np.array([self.x, self.y])
        img_dim = np.array([self.c, self.r])
        norm = int( np.linalg.norm(pos) / np.linalg.norm(img_dim) * 100)
        return norm
    
    def angle(self):
        angle = int(math.degrees(math.atan2(self.y,self.x)))
        if (angle < 0):
            angle = angle + 360
        return angle        
    
    def zone(self):
        angle = self.angle()
        
        zones_names = ("right", "up right", "up", "up left", "left", "down left", "down", "down right", "right")
        zones_range = ([0,20], [20,70], [70,110], [110,160], [160,200], [200,250], [250,290], [290,340], [340,360])
        
        zone = "No zone found"
        for i, ran in enumerate(zones_range):
            if (angle >= ran[0] and angle <= ran[1]):
                zone = zones_names[i]
        return zone