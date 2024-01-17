import pygame
import subprocess
import sys
import os

pygame.init()

class AxIsColner:
    def __init__(self):
        self.width, self.height = 600, 300
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("GitHub Repository Cloner")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 36)
        self.repo_url = "https://github.com/Axel-AxIsWare/AxIsWare"

        self.buttons = [
            {"rect": pygame.Rect(50, 150, 250, 60), "text": "Clone AxIsWare", "action": self.clone_repository},
        ]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_button_click(event.pos)

            self.screen.fill((50, 50, 50))

            for button in self.buttons:
                pygame.draw.rect(self.screen, (0, 128, 255), button["rect"])
                button_text = self.font.render(button["text"], True, (255, 255, 255))
                text_rect = button_text.get_rect(center=button["rect"].center)
                self.screen.blit(button_text, text_rect)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def handle_button_click(self, pos):
        for button in self.buttons:
            if button["rect"].collidepoint(pos):
                button["action"]()

    def clone_repository(self):
        try:
            subprocess.run(["git", "clone", self.repo_url], check=True)
            self.show_message("Success", "Repository cloned successfully!")
        except subprocess.CalledProcessError as e:
            self.show_message("Error", f"Failed to clone repository. Error: {e}")

    def open_in_explorer(self):
        os.system(f"start explorer {os.path.basename(self.repo_url)}")

    def show_message(self, title, message):
        pygame.display.iconify()
        pygame.display.set_mode((1, 1))
        pygame.display.set_caption(title)
        pygame.time.delay(1500)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    app = AxIsColner()
    app.run()