import pyxel

class Joueur1:
    
    def __init__(self):
        self.x=10
        self.y=pyxel.height/2
        self.width=5
        self.high=20
        self.vitesse=4
    
    def update(self):
        if pyxel.btn(pyxel.KEY_A)==True:
            self.y-=self.vitesse
        elif pyxel.btn(pyxel.KEY_Q)== True:
            self.y+=self.vitesse
            
    def draw(self):
        pyxel.rect(self.x,self.y,self.width,self.high,7)  

    def collision(self,balle):
        if balle.x - balle.width/2 <= self.x + self.width and balle.x + balle.width/2 >= self.x and balle.y + balle.width >= self.y and balle.y - balle.width/2 <= self.y+self.high:
            balle.angle = 180 - balle.angle + pyxel.rndi(-10,10)
        
class Joueur2:
    
    def __init__(self):
        self.x=pyxel.width-15
        self.y=pyxel.height/2
        self.width=5
        self.high=20
        self.vitesse=4
    
    def update(self):
        if pyxel.btn(pyxel.KEY_UP)==True:
            self.y-=self.vitesse
        elif pyxel.btn(pyxel.KEY_DOWN)== True:
            self.y+=self.vitesse
            
    def draw(self):
        pyxel.rect(self.x,self.y,self.width,self.high,7)

    def collision(self,balle):
        if balle.x + balle.width/2 >= self.x  and balle.x + balle.width/2 <= self.x + self.width and balle.y + balle.width/2 >= self.y and balle.y - balle.width/2 <= self.y+self.high:
            balle.angle = 180 - balle.angle + pyxel.rndi(-10,10)


class Balle:
    
    def __init__(self):
        self.x = pyxel.width/2
        self.y = pyxel.height/2
        self.width = 4
        self.height = 4
        self.angle = pyxel.rndi(-40,40)+180*pyxel.rndf(0, 1)
        self.vitesse = 2
        self.game_over = False
        
    def update(self):
         if self.game_over==False:
            self.x=self.x+self.vitesse*pyxel.cos(self.angle)
            self.y=self.y-self.vitesse*pyxel.sin(self.angle)
            if self.y <= self.height - self.width/2 or self.y >= pyxel.height - self.width + self.width/2:
                self.angle = -1*self.angle
            if self.x - self.width/2 < 0:
                self.game_over=True
            if self.x + self.width /2 > pyxel.width:
                self.game_over=True

    
    def draw(self):
        pyxel.circ(self.x, self.y, self.width/2, 7)

class Game:

    def __init__(self):
        pyxel.init(420,280,fps = 60)
        self.j1 = Joueur1()
        self.j2 = Joueur2()
        self.balle = Balle()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.j1.update()
        self.j2.update()
        self.balle.update()
        self.j1.collision(self.balle)
        self.j2.collision(self.balle)


    def draw(self):
        pyxel.cls(0)
        self.j1.draw()
        self.j2.draw()
        self.balle.draw()
     
        
Game()