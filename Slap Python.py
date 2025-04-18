import pygame
import random
pygame.init()

R, G, B = 0, 0, 0
R2, G2, B2 = 255, 255, 255
R3, G3, B3 = 0, 255, 0
R4, G4, B4 = 0, 0, 255

time = 0
score = 0
glove = 'Default'

gamepass = 0
lobby = 1
diamondability = 0
ghostability = 0
brickability = 0
kill_reaper = 0
kill_killstreak = 0
brickcount = 0
bot1kill = 0 
bot2kill = 0
bot3kill = 0
play = 0
play2 = 0
admin = 1
megarock_time = 0
megarock = 0

x5 = -100
y5 = -100
x6 = -100
y6 = -100
x7 = -100
y7 = -100
x8 = -100
y8 = -100
x9 = -100
y9 = -100
x10 = -100
y10 = -100

font = pygame.font.Font(None, 36)

x = random.randrange(0, 600, 40)
y = random.randrange(0, 600, 40)

x2 = random.randrange(0, 600, 40)
y2 = random.randrange(0, 600, 40)

x3 = random.randrange(0, 600, 40)
y3 = random.randrange(0, 600, 40)

x4 = random.randrange(0, 600, 40)
y4 = random.randrange(0, 600, 40)

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

def PlayMusic(name, volume, loop, stop):
    mixer = pygame.mixer.music
    mixer.load(name)
    mixer.set_volume(volume)
    mixer.play(loop)
    if stop == True:
        mixer.stop()

while True:
    if lobby == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_5:
                    if score < 250:
                        print('not 250 slaps')
                    if score >= 250:
                        glove = 'Snow'
                        print("Selected Snow")
                if event.key == pygame.K_6:
                    if score < 500:
                        print('not 500 slaps')
                    if score >= 500:
                        glove = 'Bull'
                        print("Selected Bull")
                if event.key == pygame.K_7:
                    if score < 666:
                        print('not 666 slaps')
                    if score >= 666:
                        glove = 'Ghost'
                        print("Selected Ghost")
                if event.key == pygame.K_8:
                    if score < 1500:
                        print('not 1500 slaps')
                    if score >= 1500:
                        glove = 'Space'
                        print("Selected Space")
                if event.key == pygame.K_9:
                    if score < 3500:
                        print('not 3500 slaps')
                    if score >= 3500:
                        glove = 'Reaper'
                        print("Selected Reaper")
                if event.key == pygame.K_w:
                    lobby = 2
                if event.key == pygame.K_d:
                    lobby = 3
                if event.key == pygame.K_e:
                    lobby = 1
                if event.key == pygame.K_0:
                    print("1-Default, 2-Dual, 3-Diamond, 4-Brick, 5-Snow, 6-Bull, 7-Ghost, 8-Space, 9-Reaper")
                    print("d-next, w-badge gloves, e-exit")
                if event.key == pygame.K_1:
                    glove = 'Default'
                    print("Selected Default")
                if event.key == pygame.K_2:
                    if score < 10:
                        print('not 10 slaps')
                    if score >= 10:
                        glove = 'Dual'
                        print("Selected Dual")
                if event.key == pygame.K_3:
                    if score < 45:
                        print('not 45 slaps')
                    if score >= 45:
                        glove = 'Diamond'
                        print("Selected Diamond")
                if event.key == pygame.K_4:
                    if score < 105:
                        print('not 105 slaps')
                    if score >= 105:
                        glove = 'Brick'
                        print("Selected Brick")
            time += 3
            if time > 200:
                time = 0
                R, G, B = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                screen.fill((R, G, B))
                score_text = font.render("Slaps: " + str(score), True, (255, 255, 255))
                screen.blit(score_text, (10, 10))
                score_text = font.render("Glove: " + str(glove), True, (255, 255, 255))
                screen.blit(score_text, (10, 25))
                pygame.display.update()
                clock.tick(60)
    if lobby == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    print("1-OVERKILL, 2-MEGAROCK")
                    print("s-back, e-exit")
                if event.key == pygame.K_1:
                    if gamepass == 0:
                        print('cannot get this')
                    if gamepass == 1:
                        glove = 'OVERKILL'
                        print("Selected OVERKILL")
                if event.key == pygame.K_2:
                    if megarock == 0:
                        print("get 'WHY?' badge for this glove")
                    if megarock == 1:
                        print("Selected MEGAROCK(W.I.P)")
                        glove = "MEGAROCK"
                if event.key == pygame.K_s:
                    lobby = 0
                if event.key == pygame.K_e:
                    lobby = 1
                    continue
    if lobby == 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    print("1-Reverse, 2-Killstreak, 3-Gods's Hand, 4-The Flex")
                    print("a-back, w-badge gloves, e-exit")
                if event.key == pygame.K_1:
                    if score < 5000:
                        print('not 5000 slaps')
                    if score >= 500:
                        glove = 'Reverse'
                        print("Selected Reverse(W.I.P)")
                if event.key == pygame.K_2:
                    if score < 5500:
                        print('not 5500 slaps')
                    if score >= 5500:
                        glove = 'Killstreak'
                        print("Selected Killstreak")
                if event.key == pygame.K_3:
                    if score < 56000:
                        print('not 56000 slaps')
                    if score >= 56000:
                        glove = "God's Hand"
                        print("Selected God's Hand")
                if event.key == pygame.K_4:
                    if score < 100000:
                        print('not 100000 slaps')
                    if score >= 100000:
                        glove = 'The Flex'
                        print("Selected The Flex")
                if event.key == pygame.K_a:
                    lobby = 0
                if event.key == pygame.K_w:
                    lobby = 2
                if event.key == pygame.K_e:
                    lobby = 1
                    continue
    if lobby == 4:
        if admin == 0:
            print("BAN! reason: cheater")
            quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    print("1-Barzil")
                    print("q-set slaps, e-exit")
                if event.key == pygame.K_1:
                    glove = "Barzil"
                    print("Selected Barsil(W.I.P)")
                    print("WARNING WITH ADMIN ABUSE BE CAREFUL")
                if event.key == pygame.K_q:
                    print("WARNING WITH ADMIN ABUSE BE CAREFUL")
                    slaps = int(input("Enter slaps count:"))
                    continue
                if event.key == pygame.K_e:
                    lobby = 1
                    continue
        score_text = font.render("Slaps: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        score_text = font.render("Glove: " + str(glove), True, (255, 255, 255))
        screen.blit(score_text, (10, 25))
        if glove == "Reaper":
            score_text = font.render("Kills: " + str(kill_reaper), True, (255, 255, 255))
            screen.blit(score_text, (10, 40))
        if glove == "Killstreak":
            score_text = font.render("Kills: " + str(kill_killstreak), True, (255, 255, 255))
            screen.blit(score_text, (10, 40))
        pygame.display.update()
    if lobby == 1:
        if time > 200:
            time = 0
            if kill_killstreak >= 25 and kill_killstreak <= 49:
                R, G, B = 50, 0, 255
            if kill_killstreak >= 50 and kill_killstreak <= 74:
                R, G, B = 50, 0, 0
            else:
                R, G, B = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            if bot1kill == 1:
                bot1kill = 0
                kill_reaper += 1
            if bot2kill == 1:
                bot2kill = 0
                kill_reaper += 1
            if bot3kill == 1:
                bot3kill = 0
                kill_reaper += 1
            if kill_reaper == 0 and kill_killstreak == 0:
                PlayMusic("Reaper1Kills.mp3", 8, -1, True)
            if kill_reaper >= 1 and kill_reaper <= 3:
                if play == 0:
                    play = 1
                    PlayMusic("Reaper1Kills.mp3", 8, -1, False)
            if kill_reaper >= 4 and kill_reaper <= 8:
                if play == 1:
                    play = 0
                    PlayMusic("Reaper1Kills.mp3", 8, -1, True)
                    PlayMusic("Reaper4Kills.mp3", 8, -1, False)
            if kill_reaper >= 9 and kill_reaper <= 18:
                if play == 0:
                    play = 1
                    PlayMusic("Reaper4Kills.mp3", 8, -1, True)
                    PlayMusic("Reaper9Kills.mp3", 8, -1, False)
            if kill_reaper >= 19:
                if play == 1:
                    play = 0
                    PlayMusic("Reaper9Kills.mp3", 8, -1, True)
                    PlayMusic("Reaper19Kills.mp3", 8, -1, False)
            if kill_killstreak >= 4 and kill_killstreak <= 9:
                if play2 == 0:
                    play2 = 1
                    PlayMusic("Killstreak4Kills.mp3", 8, -1, False)
            if kill_killstreak >= 10 and kill_killstreak <= 24:
                if play2 == 1:
                    play2 = 0
                    PlayMusic("Killstreak10Kills.mp3", 8, -1, False)
            if kill_killstreak >= 25 and kill_killstreak <= 49:
                if play2 == 0:
                    play2 = 1
                    PlayMusic("Killstreak25Kills.mp3", 8, -1, False)
            if kill_killstreak >= 50 and kill_killstreak <= 74:
                if play2 == 1:
                    play2 = 0
                    PlayMusic("Killstreak50Kills.mp3", 8, -1, False)
            if kill_killstreak >= 75 and kill_killstreak <= 99:
                if play2 == 0:
                    play2 = 1
                    PlayMusic("Killstreak75Kills.mp3", 8, -1, False)
            if kill_killstreak >= 100 and kill_killstreak <= 249:
                if play2 == 1:
                    play2 = 0
                    PlayMusic("Killstreak100Kills.mp3", 8, -1, False)
            if kill_killstreak >= 250 and kill_killstreak <= 999:
                if play2 == 0:
                    play2 = 1
                    PlayMusic("Killstreak250Kills.mp3", 8, -1, False)
            if kill_killstreak >= 1000:
                if play2 == 1:
                    play2 = 0
                    PlayMusic("Killstreak1000Kills.mp3", 8, -1, False)
            if diamondability == 0:
                megarock_time = 0
            if diamondability == 1:
                megarock_time += 1
            if megarock_time >= 100:
                if megarock == 0:
                    print("Badge awarded: WHY?")
                    megarock = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y -= 40
                if event.key == pygame.K_s:
                    y += 40
                if event.key == pygame.K_a:
                    x -= 40
                if event.key == pygame.K_d:
                    x += 40
                if event.key == pygame.K_r:
                    lobby = 0
                    continue
                if event.key == pygame.K_q:
                    if admin == 1:
                        lobby = 4
                        continue
                if glove == 'Default':
                    if event.key == pygame.K_e:
                        x += 80
                        y += 80
                if glove == 'Diamond':
                    if diamondability == 0:
                        if event.key == pygame.K_e:
                            x10 = x
                            y10 = y
                            x += 80000
                            y += 80000
                            diamondability = 1
                    else:
                        if event.key == pygame.K_e:
                            x10 = -100
                            y10 = -100
                            x -= 80000
                            y -= 80000
                            diamondability = 0
                if glove == 'Ghost':
                    if event.key == pygame.K_e:
                        if ghostability == 0:
                            x += 80000
                            y += 80000
                            ghostability = 1
                if glove == "Brick":
                    if event.key == pygame.K_e:
                        if brickability == 0:
                            x5 = x
                            y5 = y
                        if brickcount == 1:
                            x6 = x
                            y6 = y
                        if brickcount == 2:
                            x7 = x
                            y7 = y
                        if brickcount == 3:
                            x8 = x
                            y8 = y
                        if brickcount == 4:
                            x9 == x
                            y9 = y
                        if brickcount >= 5:
                            brickcount = 1
                        brickability = 1
                        brickcount += 1
                if glove == "Space":
                    if event.key == pygame.K_e:
                        for i in range(4):
                            y -= 40
                if glove == "Killstreak":
                    if event.key == pygame.K_e:
                        if kill_killstreak >= 75 and kill_killstreak <= 99:
                            x2 += 40
                            y2 -= 40
                            x3 += 40
                            y3 -= 40
                            x4 += 40
                            y4 -= 40
                        if kill_killstreak >= 100 and kill_killstreak <= 249:
                            x2 += 80
                            y2 -= 80
                            x3 += 80
                            y3 -= 80
                            x4 += 80
                            y4 -= 80
                            score += 1
                        if kill_killstreak >= 250 and kill_killstreak <= 999:
                            x2 += 160
                            y2 -= 160
                            x3 += 160
                            y3 -= 160
                            x4 += 160
                            y4 -= 160
                            score += 2
                        if kill_killstreak >= 1000:
                            R2, G2, B2 = 255, 255, 0
                            R3, G3, B3 = 255, 255, 0
                            R4, G4, B4 = 255, 255, 0
                            score += 3
        if x == x2 and y == y2:
            if glove == "God's Hand" or glove == 'OVERKILL':
                x2 += 60000
                y2 += 60000
            else:
                if glove == "Reaper":
                    bot1kill = 1
                if glove == "Killstreak":
                    kill_killstreak += 1
                x2 = random.randrange(0, 600, 40)
                y2 = random.randrange(0, 600, 40)
            if glove == 'Dual' or glove == 'Snow' or glove == 'Bull':
                score += 2
            elif glove == 'The Flex':
                R2, G2, B2 = 255, 255, 0
                score += 1
            else:
                score += 1
            x -= 40
            y -= 40
            x2 += 40
            y2 += 40
            if x > 600 or y > 600 or x < 0 or y < 0:
                x = random.randrange(0, 600, 40)
                y = random.randrange(0, 600, 40)
                kill_reaper = 0
        if x-80000 == x2 and y-80000 == y2:
            x2 = random.randrange(0, 600, 40)
            y2 = random.randrange(0, 600, 40)
            x -= 80000
            y -= 80000
            score += 1
            ghostability = 0
        if x == x3 and y == y3:
            if glove == "God's Hand" or glove == 'OVERKILL':
                x3 += 60000
                y3 += 60000
            else:
                if glove == "Reaper":
                    bot2kill = 1
                if glove == "Killstreak":
                    kill_killstreak += 1
                x3 = random.randrange(0, 600, 40)
                y3 = random.randrange(0, 600, 40)
            if glove == 'Dual' or glove == 'Snow' or glove == 'Bull':
                score += 2
            elif glove == 'The Flex':
                R3, G3, B3 = 255, 255, 0
                score += 1
            else:
                score += 1
            x -= 40
            y -= 40
            x3 += 40
            y3 = 40
            if x > 600 or y > 600 or x < 0 or y < 0:
                x = random.randrange(0, 600, 40)
                y = random.randrange(0, 600, 40)
                kill_reaper = 0
        if glove == 'Ghost':
            if x-80000 == x3 and y-80000 == y3:
                x3 = random.randrange(0, 600, 40)
                y3 = random.randrange(0, 600, 40)
                x -= 80000
                y -= 80000
                score += 1
                ghostability = 0
        if x == x4 and y == y4:
            if glove == "God's Hand" or glove == 'OVERKILL':
                x4 += 60000
                y4 += 60000
            if glove == "Reaper":
                bot3kill = 1
            else:
                if glove == "Reaper":
                    bot2kill = 1
                if glove == "Killstreak":
                    kill_killstreak += 1
                x4 = random.randrange(0, 600, 40)
                y4 = random.randrange(0, 600, 40)
            if glove == 'Dual' or glove == 'Snow' or glove == 'Bull':
                score += 2
            elif glove == 'The Flex':
                R4, G4, B4 = 255, 255, 0
                score += 1
            else:
                score += 1
            x -= 40
            y -= 40
            x4 += 40
            y4 += 40
            if x > 600 or y > 600 or x < 0 or y < 0:
                x = random.randrange(0, 600, 40)
                y = random.randrange(0, 600, 40)
                kill_reaper = 0
        if glove == 'Ghost':
            if x-80000 == x4 and y-80000 == y4:
                x4 = random.randrange(0, 600, 40)
                y4 = random.randrange(0, 600, 40)
                x -= 80000
                y -= 80000
                score += 1
                ghostability = 0
        if x2 == x5 and y2 == y5 or x2 == x6 and y2 == y6 or x2 == x7 and y2 == y7 or x2 == x8 and y2 == y8 or x2 == x9 and y2 == y9:
            if brickability == 1:
                score += 1
                x2 = random.randrange(0, 600, 40)
                y2 = random.randrange(0, 600, 40)
        if x3 == x5 and y3 == y5 or x3 == x6 and y3 == y6 or x3 == x7 and y3 == y7 or x3 == x8 and y3 == y8 or x3 == x9 and y3 == y9:
            if brickability == 1:
                score += 1
                x3 = random.randrange(0, 600, 40)
                y3 = random.randrange(0, 600, 40)
        if x4 == x5 and y4 == y5 or x4 == x6 and y4 == y6 or x4 == x7 and y4 == y7 or x4 == x8 and y4 == y8 or x4 == x9 and y4 == y9:
            if brickability == 1:
                score += 1
                x2 = random.randrange(0, 600, 40)
                y2 = random.randrange(0, 600, 40)
        if x == x2-80 and y == y2-80 or x == x2-40 and y == y2-40:
            x2 -= 40
            y2 -= 40
        if x == x2-80 and y == y2+80 or x == x2-40 and y == y2+40:
            x2 -= 40
            y2 += 40
        if x == x2+80 and y == y2-80 or x == x2+40 and y == y2-40:
            x2 += 40
            y2 -= 40
        if x == x2+80 and y == y2+80 or x == x2+40 and y == y2+40:
            x2 -= 40
            y2 -= 40
        if x == x3-80 and y == y3-80 or x == x3-40 and y == y3-40:
            x3 -= 40
            y3 -= 40
        if x == x3-80 and y == y3+80 or x == x3-40 and y == y3+40:
            x3 -= 40
            y3 += 40
        if x == x3+80 and y == y3-80 or x == x3+40 and y == y3-40:
            x3 += 40
            y3 -= 40
        if x == x3+80 and y == y3+80 or x == x3+40 and y == y3+40:
            x3 -= 40
            y3 -= 40
        if x == x4-80 and y == y4-80 or x == x4-40 and y == y4-40:
            x4 -= 40
            y4 -= 40
        if x == x4-80 and y == y4+80 or x == x4-40 and y == y4+40:
            x4 -= 40
            y4 += 40
        if x == x4+80 and y == y4-80 or x == x4+40 and y == y4-40:
            x4 += 40
            y4 -= 40
        if x == x4+80 and y == y4+80 or x == x4+40 and y == y4+40:
            x4 -= 40
            y4 -= 40
        if x2 > 600 or y2 > 600 or x2 < 0 or y2 < 0:
                x2 = random.randrange(0, 600, 40)
                y2 = random.randrange(0, 600, 40)
                kill_reaper = 0
        if x3 > 600 or y3 > 600 or x3 < 0 or y3 < 0:
                x3 = random.randrange(0, 600, 40)
                y3 = random.randrange(0, 600, 40)
                kill_reaper = 0
        if x4 > 600 or y4 > 600 or x4 < 0 or y4 < 0:
                x4 = random.randrange(0, 600, 40)
                y4 = random.randrange(0, 600, 40)
                kill_reaper = 0

        time += 3

        screen.fill((R, G, B))
        pygame.draw.rect(screen, (100, 100, 100), (x10, y10, 30, 30))
        if kill_reaper >= 19:
            pygame.draw.circle(screen, (0, 0, 0), (x,y), 20)
            pygame.draw.circle(screen, (255, 0, 0), (x,y), 30, 2)
        if kill_killstreak >= 250 and kill_killstreak <= 999:
            pygame.draw.circle(screen, (0, 0, 0), (x,y), 20)
            pygame.draw.circle(screen, (100, 0, 100), (x,y), 30, 10)
        else:
            pygame.draw.circle(screen, (255, 0, 0), (x,y), 20)
        pygame.draw.circle(screen, (R2, G2, B2), (x2,y2), 20)
        pygame.draw.circle(screen, (R3, G3, B3), (x3,y3), 20)
        pygame.draw.circle(screen, (R4, G4, B4), (x4,y4), 20)
        if brickability == 1:
            if brickcount >= 1:
                pygame.draw.circle(screen, (255, 255, 100), (x5, y5), 20)
                if brickcount >= 2:
                    pygame.draw.circle(screen, (255, 255, 100), (x6, y6), 20)
                    if brickcount >= 3:
                        pygame.draw.circle(screen, (255, 255, 100), (x7, y7), 20)
                        if brickcount >= 4:
                            pygame.draw.circle(screen, (255, 255, 100), (x8, y8), 20)
                            if brickcount >= 5:
                                pygame.draw.circle(screen, (255, 255, 100), (x9, y9), 20)
    score_text = font.render("Slaps: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    score_text = font.render("Glove: " + str(glove), True, (255, 255, 255))
    screen.blit(score_text, (10, 25))
    if glove == "Reaper":
        score_text = font.render("Kills: " + str(kill_reaper), True, (255, 255, 255))
        screen.blit(score_text, (10, 40))
    if glove == "Killstreak":
        score_text = font.render("Kills: " + str(kill_killstreak), True, (255, 255, 255))
        screen.blit(score_text, (10, 40))
    pygame.display.update()
    clock.tick(60)