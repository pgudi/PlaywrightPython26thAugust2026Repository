from playwright.sync_api import Page,expect

def test_launch_navigate_url(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    # Fetch URL of Application
    url=page.url
    print("URL of the Application :"+url)
    # Fetch Title of The Application
    title=page.title()
    print("Title of the Application :"+title)
