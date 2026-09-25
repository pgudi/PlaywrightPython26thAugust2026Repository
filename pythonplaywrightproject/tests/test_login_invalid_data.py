from playwright.sync_api import Page, expect

def test_login_invalid_data(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    page.locator("//input[@name='username']").fill("pgudi123")
    page.locator("//input[@name='password']").fill("pgudi123")
    page.locator("//button[normalize-space()='Sign In']").click()
    page.wait_for_timeout(3000)
    errorObject=page.locator("//p[normalize-space()='Invalid username or password']")
    expect(errorObject).to_have_text("Invalid username or password")