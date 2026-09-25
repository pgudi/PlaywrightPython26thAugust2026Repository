from playwright.sync_api import Page, expect

def test_login_logout_scenario(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    #Validation
    expect(page).to_have_url("https://sgtestinginstituteapp.onrender.com/login")
    expect(page).to_have_title("S G Software Testing Institute")
    #Login Action
    page.locator("//input[@name='username']").fill("pgudi")
    page.locator("//input[@name='password']").fill("pgudi")
    page.locator("//button[normalize-space()='Sign In']").click()
    page.wait_for_timeout(3000)
    home_ui_object=page.locator("//h2[normalize-space()='S G Software Testing Institute']")
    #Validation on Home Page
    expect(home_ui_object).to_have_text("S G Software Testing Institute")
    # Logout Action
    page.locator("//button[normalize-space()='Logout']").click()
    page.wait_for_timeout(3000)
    expect(page.locator("//h2[normalize-space()='Login']")).to_have_text("Login")