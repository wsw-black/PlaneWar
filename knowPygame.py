import pygame
# pygame.init()
# print("游戏的代码")
# pygame.quit()

# hero_rect = pygame.Rect(100,500,120,125)
# print("坐标原点 %d %d" %(hero_rect.x,hero_rect.y))
# print("英雄大小: %d %d" %hero_rect.size )

pygame.init()
# background 尺寸是 480 * 700
screen = pygame.display.set_mode((480,700))  # 创建游戏主窗口
# 绘制背景图片
# 1.更新背景
bg = pygame.image.load("./images/background.png")
# 2.绘制在屏幕上
screen.blit(bg,(0,0))
# 3. 更新显示
# pygame.display.update()

# 创建英雄飞机
# 1. 更新背景
hero = pygame.image.load("./images/me1.png")
# 2. 绘制在屏幕上
screen.blit(hero,(200,500))
# 3. 更新显示
pygame.display.update()
# 游戏循环
while True:
    pass
pygame.quit()