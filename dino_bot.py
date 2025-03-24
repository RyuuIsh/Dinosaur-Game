from PIL import Image
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import keyboard

TARGETCOLOR = 83
INITIAL_X_POSITION_RANGE = [315, 320]  # Smaller initial X coordinate range to check
Y_POSITION_RANGE = [540, 631]  # Y coordinate range to check
INCREMENT_FACTOR = 10  # Factor to adjust increment

# Set up the Selenium Chrome driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Open the specified URL
url = "https://elgoog.im/dinosaur-game/"
driver.get(url)
driver.maximize_window()

# Wait for the page to load completely
time.sleep(5)
pyautogui.press('space')  # Start the game
screenshot_path = 'dino.jpg'  # Path to save the screenshot


def is_target_color(image, x_position_range):
    """Check if any pixel in the specified range matches the target color."""
    for x in range(x_position_range[0], x_position_range[1]):
        for y in range(Y_POSITION_RANGE[0], Y_POSITION_RANGE[1]):
            r, g, b = image.getpixel((x, y))
            if (r, g, b) != (255, 255, 255):  # Detect any color other than white
                return True
    return False


# Define the region for the screenshot (entire screen starting from y=102)
screenshot_region = (0, 102, 1920, 1080)

game_on = True
start_time = time.time()

while game_on:
    elapsed_time = time.time() - start_time
    speed_increment = int(elapsed_time * INCREMENT_FACTOR)
    current_x_position_range = [
        INITIAL_X_POSITION_RANGE[0] + speed_increment,
        INITIAL_X_POSITION_RANGE[1] + speed_increment
    ]

    # Remove old screenshot if it exists
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

    # Take a new screenshot of the specified region
    image = pyautogui.screenshot(region=screenshot_region)
    image.save(screenshot_path)

    # Check for the target color
    with Image.open(screenshot_path) as image:
        if is_target_color(image, current_x_position_range):
            pyautogui.press('space')  # Jump over the obstacle
            print(f"Jumped at X range: {current_x_position_range}")

    # Check if 'q' key is pressed to quit the game
    if keyboard.is_pressed('q'):
        game_on = False
        driver.quit()
