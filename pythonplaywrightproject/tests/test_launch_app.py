from playwright.sync_api import Page, expect

def test_launch_application(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    url=page.url
    print("URL of the Application:",url)
    title=page.title()
    print("Title of the Application:",title)