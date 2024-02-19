from PIL import ImageGrab

def take_screenshot(filename="screenshot.png"):
    """Takes a screenshot and saves it to the specified filename."""
    screenshot = ImageGrab.grab()
    screenshot.save(filename)
    return filename
