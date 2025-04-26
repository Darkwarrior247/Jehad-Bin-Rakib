import os
from github_contributions import Snake

# Replace with your GitHub username
GITHUB_USERNAME = 'Darkwarrior247'

# Create output directories if they don't exist
output_dir = 'dist'
os.makedirs(output_dir, exist_ok=True)

# Generate the snake
snake = Snake(username=GITHUB_USERNAME)
snake.generate()

# Save as SVG and GIF
snake.save_as_svg(os.path.join(output_dir, 'github-contribution-grid-snake.svg'))
snake.save_as_gif(os.path.join(output_dir, 'github-contribution-grid-snake.gif'))
