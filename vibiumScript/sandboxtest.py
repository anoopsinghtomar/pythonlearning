import os
from vibium import browser_sync as browser

# ---- STEP 1: Specify the clicker binary path ----
# Make sure this points to the vibium_win32_x64 folder in your venv
clicker_path = os.path.join(
    "D:/MYFILES/pythonlearning/.venv/Lib/site-packages/vibium_win32_x64"
)

# ---- STEP 2: Launch the browser ----
try:
    vibe = browser.launch(executable_path=clicker_path)
    print("Browser launched successfully!")
except Exception as e:
    print(f"Failed to launch Vibium browser: {e}")
    raise

# ---- STEP 3: Go to a website ----
vibe.go("https://www.python.org/")

# ---- STEP 4: Interact with the page ----
# Example: print page title
print("Page title:", vibe.title())
