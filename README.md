# 🦖 Automated Google Chrome Dinosaur Game Bot
This is a Python bot that automatically plays the Google Chrome Dinosaur Game using Selenium, PyAutoGUI, and PIL (Pillow). The bot detects obstacles and makes the dinosaur jump at the right moment to avoid collisions.

## Features
✅ Plays the Chrome Dino Game automatically 🎮<br>
✅ Detects obstacles dynamically using pixel color analysis 🎯<br>
✅ Increases speed as the game progresses ⏩<br>
✅ Uses PyAutoGUI for keyboard simulation ⌨<br>
✅ Allows manual exit by pressing the 'q' key ❌<br>

## How it Works 
1️⃣ Launches the Chrome Dinosaur Game in the browser using Selenium 🌐<br>
2️⃣ Starts the game automatically by pressing the spacebar 🎮<br>
3️⃣ Takes screenshots at regular intervals using PyAutoGUI 📸<br>
4️⃣ Scans pixels in a specified region to detect obstacles 🏗<br>
5️⃣ Jumps when an obstacle is detected using PyAutoGUI spacebar press ⬆<br>
6️⃣ Increases detection speed as the game progresses ⚡<br>
7️⃣ Quits the game if 'q' is pressed on the keyboard 🔚<br>

## Project Structure
```
/chrome_dino_bot
│── dino_bot.py           # Main Script
│── requirements.txt      # Python Dependencies
```

## Setup & Installation
### 1. Clone the Repository
```
git clone https://github.com/yourusername/Chrome-Dino-Bot.git
cd Chrome-Dino-Bot
```

### 2. Install Dependencies
```
pip install -r requirements.txt

```

### 3. Run the Bot
```
python dino_bot.py
```

## 🎯 How It Detects Obstacles
- The bot captures a screenshot of the game screen.
- It analyzes a specific pixel range for any non-white color (obstacle).
- If an obstacle is detected, it presses the spacebar to make the dino jump.
- The detection area dynamically moves forward as the game speed increases.
<br>
PYTHON
```
def is_target_color(image, x_position_range):
    """Check if any pixel in the specified range matches the target color."""
    for x in range(x_position_range[0], x_position_range[1]):
        for y in range(Y_POSITION_RANGE[0], Y_POSITION_RANGE[1]):
            r, g, b = image.getpixel((x, y))
            if (r, g, b) != (255, 255, 255):  # Detect any color other than white
                return True
    return False
```

## Future Enhancements
✅ Add AI-based Jump Prediction 🧠<br>
✅ Optimize Pixel Detection for Faster Reaction ⚡<br>
✅ Implement Neural Network-based Dino Learning 🤖<br>
✅ Train the bot to adapt to game difficulty dynamically 🎯<br>

## 💙 Connect With Me
💻 Developer: Ishaan Chhabra<br>
🔗 GitHub: RyuuIsh<br>
<br>
💙 Challenge the AI & Beat the Chrome Dinosaur Game! 🦖🚀










