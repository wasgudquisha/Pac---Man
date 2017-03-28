from gamelib import *

game = Game(1024,688, "Five Nights At Pac-Man" )

bk = Image("images\\backround3.jpg",game)
game.setBackground(bk)

pacman = Animation("images\\pacsprite.png",4,game,800/2,800/2)
pacman.resizeTo(50,50)

boss = Image("images\\spooky2.png",game)
boss.resizeTo(200,200)

fruit = Image("images\\TheRealGoldenFruit.png",game)
fruit.resizeTo(20,20)
fruit.visible = False

dark = Image("images\\darksphere.png",game)
dark.resizeTo(20,20)
dark.visible = False

title = Image("images\\start.jpg",game)
title.draw()
game.drawText("Press [ SPACE ] to play",320,588)
game.update(1)
game.wait(K_SPACE)


s = Sound("sound\\pacmanintro.wav",1)

pg = Sound("sound\\aliengun.wav",2)

sg = Sound("sound\\bomb.wav",3)


while not game.over:
    game.processInput()

    bk.draw()
    pacman.move()
    boss.move()
    fruit.move()
    dark.move()
    s.play()


    if keys.Pressed[K_w] and pacman.y > 10 :
        pacman.y -=1
    if keys.Pressed[K_s] and pacman.y < game.height :
        pacman.y +=1
    if keys.Pressed[K_a] and pacman.x > 10 :
        pacman.x -=1
    if keys.Pressed[K_d] and pacman.y < game.width :
        pacman.x +=1
    
    if keys.Pressed[K_UP] and boss.y > 10 :
        boss.y -=1
    if keys.Pressed[K_DOWN] and boss.y < game.height :
        boss.y +=1
    if keys.Pressed[K_LEFT] and boss.x > 10 :
        boss.x -=1
    if keys.Pressed[K_RIGHT] and boss.y < game.width :
        boss.x +=1

    if keys.Pressed[K_f]:
        fruit.visible = True
        fruit.moveTo(pacman.x,pacman.y)
        fruit.setSpeed(5,-90)
        pg.play()

  
    if boss.collidedWith(fruit):
        boss.health -= 5
        fruit.visible = False
       

    if keys.Pressed[K_l]:
        dark.visible = True
        dark.moveTo(boss.x,boss.y)
        dark.setSpeed(5,90)
        sg.play()


    if dark.collidedWith(pacman):
        pacman.health -= 5
        dark.visible = False


    if pacman.health < 1 or boss.health < 1:
        game.over = True 
        

    game.drawText("Pac Man:" + str(pacman.health),5,5)
    game.drawText("Spooky:" + str(boss.health),930,5)
    game.update(120)

game.drawText("Game Over",game.width/4,game.height/3,Font(green,90,yellow))
game.drawText("Press [ESC] to Exit",game.width/2 + 80,game.height - 50,Font(yellow,40,green))
game.update()
game.wait(K_ESCAPE)
game.quit()
    







