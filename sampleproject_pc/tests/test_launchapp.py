from playwright.sync_api import Page, expect

def test_launch_navigate_url(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    # Fetch URL of Application
    url=page.url
    print("URL of Application :"+url)
    # Title of Application
    title=page.title()
    print("Title of Application :"+title)