from gamelib import*

game = Game(800,600,"Death Match")
alien = Image("deathmatch\\alien.png",game)
droid1 = Image("deathmatch\\droid1.png",game)
bk = Image("deathmatch\\apocalypse.jpg",game)
crosshair = Image("images\\crosshair.png",game)
crosshair.resizeTo(100,100)

bk.resizeTo(800,600)
alien.resizeTo(100,100)
droid1.resizeTo(100,100)
alien.setSpeed(6,60)
droid1.setSpeed(6,60)
droid1.moveTo(150,150)

title = Image("deathmatch\\DeathMatchTitle.gif",game)
bk.draw()
title.draw()
game.drawText("Press [SPACE] to play",320,400,Font(green,25,black))
game.drawText("TA Games",50,50,Font(red,40,black))
game.update(1)
game.wait(K_SPACE)




while not game.over:
    game.processInput()
    bk.draw()
    alien.move("True")
    droid1.move("True")

    crosshair.moveTo(mouse.x,mouse.y)
    if alien.collidedWith(mouse) and mouse.LeftButton: 
        game.score+=10
        x = randint(150,650)
        y = randint(150,450)
        alien.moveTo(x,y)
        
    if droid1.collidedWith(mouse) and mouse.LeftButton:
        game.score+=10
        x = randint(150,650)
        y = randint(150,450)
        droid1.moveTo(x,y)
        



    if droid1.collidedWith(alien):
        game.score-=8

    

    if game.score>=200:
        game.drawText("You win",300,0,Font(blue,40,black))
        game.drawText("Game Over",game.width/4,game.height/3,Font(blue,90,black))
        game.drawText("Press [ESC] to Exit",game.width/2 + 80,game.height - 50,Font(black,40,blue))
        game.over = True
        game.update(1)
        game.wait(K_ESCAPE)
    
    game.displayScore()
    game.update(20)
game.quit()
    
    




