import pygame, random

bird_body_col = (255, 255, 0)
bird_beak_col = (153, 76, 0)
bird_wing_col = (255, 51, 51)
pipe_col = (0, 235, 0)
sky_col = (0, 255, 255)
grass_col = (0, 155, 0)
sun_col = (255, 255, 102)
blk = (0, 0, 0)

gravity = 15
fps = 60
bird_pos = 225
bird_vel = 0
high_score = 0

pipe_vel = 2
pipe_start_pos = 500
pipe_start_gap = random.randint(84, 416)

pygame.init()
size = (500, 500)
cap = pygame.display.set_caption("Flappy Bird")
disp = pygame.display.set_mode(size)
clock = pygame.time.Clock()

def draw_bird_falling(height):
    pygame.draw.rect(disp, bird_body_col, (220, height, 30, 30))
    pygame.draw.rect(disp, bird_beak_col, (250, height+10, 10, 10))
    pygame.draw.rect(disp, (0, 0, 0), (240, height+6, 4, 4))
    pygame.draw.polygon(disp, bird_wing_col, [(215, height-10), (220, height+15), (235, height+15)])

def draw_bird_flying(height):
    pygame.draw.rect(disp, bird_body_col, (220, height, 30, 30))
    pygame.draw.rect(disp, bird_beak_col, (250, height+10, 10, 10))
    pygame.draw.rect(disp, (0, 0, 0), (240, height+6, 4, 4))
    pygame.draw.polygon(disp, bird_wing_col, [(215, height+35), (220, height+15), (235, height+15)])

def draw_background():
    disp.fill((0, 0, 0))
    pygame.draw.rect(disp, grass_col, (0, 490, 500, 15))
    pygame.draw.rect(disp, sky_col, (0, 0, 500, 490))
    pygame.draw.circle(disp, sun_col, (0, 0), 85)

def draw_startground():
    pygame.draw.rect(disp, grass_col, (0, 400, 500, 100))
    pygame.draw.rect(disp, sky_col, (0, 0, 500, 400))
    pygame.draw.circle(disp, sun_col, (0, 0), 85)


myfont = pygame.font.SysFont('Comic Sans MS', 20)
def draw_caption():
    mystartmenu = "Press Enter to start"
    textsurface = myfont.render(mystartmenu, False, blk)
    disp.blit(textsurface, (100, 100))
def draw_jumps(jumps):
    jumps_caption = str(jumps) + " flaps!"
    textsurface = myfont.render(jumps_caption, False, blk)
    disp.blit(textsurface, (350, 10))
def draw_score(score):
    score_caption = str(score) + " points!"
    textsurface = myfont.render(score_caption, False, blk)
    disp.blit(textsurface, (350, 50))
def draw_high_score(high):
    high_caption = "High Score: " + str(high)
    textsurface = myfont.render(high_caption, False, blk)
    disp.blit(textsurface, (300, 90))
def draw_pipe(x_coord, gap_center):
    pygame.draw.rect(disp, pipe_col, (x_coord, 0, 95, gap_center-83))
    pygame.draw.rect(disp, pipe_col, (x_coord, gap_center+83, 95, 417-gap_center))

running = True
started = False

while running and not started:
    draw_startground()
    draw_caption()
    pygame.display.flip()
    total_jumps = 0
    score = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                started = True
    while running and started:
        draw_background()
        draw_pipe(pipe_start_pos, pipe_start_gap)
        if bird_vel >= 0:
            draw_bird_falling(bird_pos)
        else:
            draw_bird_flying(bird_pos)
        draw_jumps(total_jumps)
        draw_score(score)
        draw_high_score(high_score)
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                elif e.key == pygame.K_SPACE:
                    if bird_vel > 0.5:
                        total_jumps += 1
                        bird_vel = -6
                        bird_pos += bird_vel
                        
        bird_vel += gravity/fps
        bird_pos += bird_vel
        pipe_vel = (score/10) + 2
        if 0 >= bird_pos or bird_pos > 465:
            started = False
        if pipe_start_pos > -95 and started:
            pipe_start_pos -= pipe_vel
            if 130 < pipe_start_pos < 265:
                lower_bound = pipe_start_gap + 83
                upper_bound = pipe_start_gap - 83
                bird_lower = bird_pos + 30
                if bird_pos < upper_bound:
                    started = False
                elif bird_lower > lower_bound:
                    started = False
        else:
            pipe_start_pos = 503
            pipe_start_gap = random.randint(84, 416)
            score += 1
            print(pipe_vel)

        clock.tick(fps)
        if not started:
            if high_score < score:
                high_score = score
            bird_vel = 0
            bird_pos = 225
            pipe_start_pos = 503
            pipe_start_gap = random.randint(84, 416)
            pipe_vel = 2