
import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 设置窗口大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("飞机大战")

# 飞机类
class Plane(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, keys_pressed=None):
        if keys_pressed is not None:  # 检查是否有按键信息传入
            if keys_pressed[pygame.K_a]:
                self.rect.x -= 5
            if keys_pressed[pygame.K_d]:
                self.rect.x += 5
            if keys_pressed[pygame.K_w]:
                self.rect.y -= 5
            if keys_pressed[pygame.K_s]:
                self.rect.y += 5

    def is_out_of_bounds(self):
        return not (0 <= self.rect.left <= SCREEN_WIDTH and 0 <= self.rect.right <= SCREEN_WIDTH and
                    0 <= self.rect.top <= SCREEN_HEIGHT and 0 <= self.rect.bottom <= SCREEN_HEIGHT)

# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 1

    def update(self):
        self.rect.y -= self.speed
        if self.rect.top < 0:
            self.kill()

# 敌机类
class EnemyPlane(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()

# 游戏状态
class GameState:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.game_over = False

    def add_score(self, points):
        self.score += points

    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game_over = True

# 创建飞机、子弹和敌机组
player = Plane((255, 0, 0), SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
player_group = pygame.sprite.GroupSingle(player)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
game_state = GameState()

# 游戏主循环
running = True
while running:
    keys_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Bullet(player.rect.centerx, player.rect.top)
            bullets.add(bullet)
            all_sprites.add(bullet)

    player_group.update(keys_pressed)  # 更新玩家飞机，传入按键信息
    all_sprites.update()  # 更新其他所有精灵，不包括玩家飞机

    # 生成敌机
    if random.random() < 0.01:
        enemy = EnemyPlane(random.randint(0, SCREEN_WIDTH - 50), -50)
        enemies.add(enemy)
        all_sprites.add(enemy)

    # 检测子弹与敌机的碰撞
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for collision in collisions.values():
        game_state.add_score(len(collision))
        for enemy in collision:
            enemies.remove(enemy)

    # 检测飞机与敌机的碰撞
    collisions = pygame.sprite.spritecollide(player, enemies, False)
    if collisions:
        game_state.lose_life()
        if game_state.game_over:
            break

    # 检查飞机是否飞出屏幕
    if player.is_out_of_bounds():
        game_state.lose_life()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

    # 显示得分和生命值


    
    score_font = pygame.font.SysFont('arial', 24)
    score_text = score_font.render(f"Score: {game_state.score}", True, (255, 255, 255))
    lives_text = score_font.render(f"Lives: {game_state.lives}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (SCREEN_WIDTH - 10 - lives_text.get_width(), 10))

    if game_state.game_over:
        game_over_font = pygame.font.SysFont('arial', 48)
        game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

pygame.quit()
sys.exit()