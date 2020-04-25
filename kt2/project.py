import pygame, sys
from random import choice

size = width, height = 550, 450
screen = pygame.display.set_mode(size)
pygame.display.set_caption('pepe')
fps = 60
clock = pygame.time.Clock()
cell_size = 50
black = 0, 0, 0


def load_image(name):
    fullname = "C:\\Users\\iriska\\my_project\\kt2\\sprites\\"+name
    if fullname[-3::] == "png": 
        image = pygame.image.load(fullname).convert_alpha()
    else:
        image = pygame.image.load(fullname).convert()
    return image
def terminate():
    pygame.quit()
    sys.exit()
def load_level(name):
    fullname = "C:\\Users\\iriska\\my_project\\kt2\\levels\\" + name
    with open(fullname, "r") as f:
        level_map = []
        for line in f:
            line = line.strip()
            level_map.append(line)
    return level_map
def draw_level(level_map, wall_image, ground_image, queen_image, portal_image):
    new_player, x, y, portals = None, None, None, []
    for y in range(len(level_map)):
        for x in range(len(level_map[y])):
            if level_map[y][x] == "#":
                Tile(wall_image, x, y, "wall")
            elif level_map[y][x] == "*":
                Tile(ground_image, x, y)
            elif level_map[y][x] == "%":
                Tile(ground_image, x, y)
                new_player = Player(x, y)
            elif level_map[y][x] == "&":
                queen = Queen(x, y, queen_image)
                Tile(ground_image, x, y)
            elif level_map[y][x] == "+":
                Tile(ground_image, x, y)
                portals.append(Tile(portal_image, x, y, "portal"))
            elif level_map[y][x] == "!":
                Tile(wall_image, x, y, "wall")
                Tile("torch.png", x, y, "torch")
            elif level_map[y][x] == "~":
                Tile("water.jpg", x, y, "wall")
            elif level_map[y][x] == ".":
                Tile("sand.jpg", x, y)
            elif level_map[y][x] == "@":
                Tile(ground_image, x, y)
                Enemy("angry_pepe_small.png", x, y)

    return new_player, queen, portals, x, y
def draw_text(txt):
    pygame.font.init()
    font = pygame.font.Font(None, 80)
    text = font.render(txt,1,black)
    text_w, text_h = text.get_width(), text.get_height()
    text_x = (width - text_w )// 2
    text_y = (height - text_h) // 2
    screen.blit(text,(text_x, text_y))


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, group = None):
        if group == "wall":
            super().__init__(walls_group, tiles_group, all_sprites)
            self.type = "wall"
        elif group == "portal":
            super().__init__(tiles_group, all_sprites, portal_group)
            self.type = "portal"
        elif group == "torch":
            super().__init__(tiles_group, all_sprites, torch_group)
            self.type = "torch"
        else:
            super().__init__(tiles_group, all_sprites)
            self.type = "ground"
        self.image = load_image(image)
        self.rect = self.image.get_rect().move(cell_size*x, cell_size*y)
        self.add(tiles_group, all_sprites)
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__(player_group, all_sprites)
        self.image = load_image("Pepe.png")
        self.rect = self.image.get_rect().move(cell_size*x, cell_size*y)
        self.portal = True
        self.add(player_group, all_sprites)
    def move_up(self):
        self.rect = self.rect.move(0, -cell_size)
        if pygame.sprite.spritecollideany(self, walls_group):
            self.rect = self.rect.move(0, cell_size)
    def move_down(self):
        self.rect = self.rect.move(0, cell_size)
        if pygame.sprite.spritecollideany(self, walls_group):
            self.rect = self.rect.move(0, -cell_size)
    def move_left(self):
        self.rect = self.rect.move(-cell_size, 0)
        if pygame.sprite.spritecollideany(self, walls_group):
            self.rect = self.rect.move(cell_size, 0)
    def move_right(self):
        self.rect = self.rect.move(cell_size, 0)
        if pygame.sprite.spritecollideany(self, walls_group):
            self.rect = self.rect.move(-cell_size, 0)
    def move_portal(self, portals_n):
        if self.portal:
            for i in range(len(portals_n)):
                if pygame.sprite.collide_rect(self, portals_n[i]):
                    self.rect.x = portals_n[(i+1) % len(portals_n)].rect.x
                    self.rect.y = portals_n[(i+1) % len(portals_n)].rect.y
                    self.portal = False
                    break
class Queen(pygame.sprite.Sprite):
    def __init__(self, x, y, image_queen):
        super().__init__(queen_group, all_sprites)
        self.image = load_image(image_queen)
        self.rect = self.image.get_rect().move(cell_size*x, cell_size*y)

        self.add(queen_group, all_sprites)
class Camera:
    def __init__(self, field_size):
        self.dx = 0
        self.dy = 0
        self.field_size = field_size
    
    def apply(self, obj):

        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, sprite):
        self.dx = -(sprite.rect.x + sprite.rect.w // 2 - width // 2)
        self.dy = -(sprite.rect.y + sprite.rect.h // 2 - height // 2)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_enemy, x, y):
        super().__init__(all_sprites, enemy_group)
        self.delay = 0
        self.image = load_image(image_enemy)
        self.rect = self.image.get_rect().move(x*cell_size, y*cell_size)
        self.add(all_sprites, enemy_group)

    def move(self):
        if self.delay % fps == 0:
            move = choice([[50,0],[-50,0],[0,50],[0,-50]])
            self.rect.move_ip(move)
            if pygame.sprite.spritecollideany(self, walls_group):
                self.rect.move_ip([-i for i in move])
        self.delay +=1

def level_1():

    player, door, portals, level_x, level_y  = draw_level(load_level("level1.txt"), "box.png", "grass.png", "door.png","portal.png")
    camera = Camera((level_x, level_y))
    color = (2, 153, 60)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                player.move_up()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                player.move_down()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                player.move_left()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                player.move_right()

           
        camera.update(player)
        for sprite in all_sprites:
             camera.apply(sprite)
        for enemy in enemy_group:
            enemy.move()
        if pygame.sprite.spritecollideany(player, portal_group):
            player.move_portal(portals)
        else:
            player.portal = True

        if not pygame.sprite.collide_rect(player, door):
            screen.fill(color)
            tiles_group.draw(screen)
            enemy_group.draw(screen)
            torch_group.draw(screen)
            player_group.draw(screen)
            queen_group.draw(screen)
        else:
            all_sprites.empty()
            player_group.empty()
            tiles_group.empty()
            queen_group.empty()
            walls_group.empty()
            del(portals, camera, level_x, level_y, color)
            running = False
        
        pygame.display.flip()
        clock.tick(fps)
def level_2():
    
    player, queen, portals, level_x, level_y   = draw_level(load_level("level2.txt"), "ice.png" , "snow.jpg",  "door.png","portal.png")
    camera = Camera((level_x, level_y))
    color = (83, 83, 219)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                player.move_up()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                player.move_down()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                player.move_left()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                player.move_right()

        camera.update(player)
        for sprite in all_sprites:
             camera.apply(sprite) 

        if pygame.sprite.spritecollideany(player, portal_group):
            player.move_portal(portals)
        else:
            player.portal = True

        if not pygame.sprite.collide_rect(player, queen):
            screen.fill(color)
            tiles_group.draw(screen)
            player_group.draw(screen)
            queen_group.draw(screen)
        else:
            all_sprites.empty()
            player_group.empty()
            tiles_group.empty()
            queen_group.empty()
            walls_group.empty()
            draw_text("хз что написать")
        
        pygame.display.flip()
        clock.tick(fps)

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
queen_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()
torch_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

level_1()
level_2()
terminate()