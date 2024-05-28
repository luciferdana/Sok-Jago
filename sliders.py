import pygame

class Slider:
    def __init__(self, x, y, length, height, knob_radius):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.knob_radius = knob_radius
        self.knob_x = x + length / 2
        self.dragging = False

        # Colors
        self.slider_bg_color = (255, 255, 255)
        self.slider_fg_color = (0, 150, 255)
        self.knob_color = (0, 150, 255)

    def draw(self, screen):
        # Draw the slider background
        pygame.draw.rect(screen, self.slider_bg_color, (self.x, self.y - self.height // 2, self.length, self.height))
        # Draw the slider foreground (filled part)
        pygame.draw.rect(screen, self.slider_fg_color, (self.x, self.y - self.height // 2, self.knob_x - self.x, self.height))
        # Draw the knob
        pygame.draw.circle(screen, self.knob_color, (self.knob_x, self.y), self.knob_radius)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if (self.knob_x - event.pos[0]) ** 2 + (self.y - event.pos[1]) ** 2 <= self.knob_radius ** 2:
                    self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.knob_x = min(max(event.pos[0], self.x), self.x + self.length)

    def get_volume(self):
        # Calculate the volume level (0.0 to 1.0)
        return (self.knob_x - self.x) / self.length