import pygame


class Button:
    def __init__(self, x, y, height, width, text, size):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font("../Design/Fonts/ofont.ru_Pixy.ttf", size)
        self.color = (15, 116, 45)
        self.hover_color = (46, 178, 86)
        self.clicked_color = (1, 101, 31)

    def draw(self, surface):
        mouse_pod = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pod):
            pygame.draw.rect(surface, self.hover_color, self.rect, border_radius=6)
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(surface, self.clicked_color, self.rect, border_radius=6)
        else:
            pygame.draw.rect(surface, self.color, self.rect, border_radius=6)

        text_surfaсe = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surfaсe.get_rect(center=self.rect.center)
        surface.blit(text_surfaсe, text_rect)
