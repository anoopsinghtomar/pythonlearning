# from vibiumScript.vibiumautomation import browser_sync as browser

from vibium import browser_sync as browser

# Launch a browser (you'll see it open!)
vibe = browser.launch()

# Go to a website
vibe.go("https://www.python.org/")
print("Loaded example.com")

# Take a screenshot
png = vibe.screenshot()
with open("screenshot.png", "wb") as f:
    f.write(png)
print("Saved screenshot.png")

# Find and click the link
link = vibe.find("a")
print("Found link:", link.text())
link.click()
print("Clicked!")

# Close the browser
vibe.quit()
print("Done!")