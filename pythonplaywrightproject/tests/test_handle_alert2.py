from playwright.sync_api import Page, expect

def test_handle_confirm_alert(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.wait_for_timeout(3000)

    # Event Listener

    page.on("dialog", lambda dialog:(print("Confimr Message :",dialog.message), dialog.accept()))
    # Click on JS Confimr
    page.locator("//button[normalize-space()='Click for JS Confirm']").click()
    page.wait_for_timeout(3000)

    # validation
    expect(page.locator("//p[@id='result']")).to_have_text("You clicked: Ok")


def test_handle_prompt_alert(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.wait_for_timeout(3000)

    # Event Listener
    page.on("dialog", lambda dialog:(print( "Prompt Message :",dialog.message), dialog.accept("PLAYWRIGHT")))
    
    # Click on JS Prompt
    page.locator("//button[normalize-space()='Click for JS Prompt']").click()
    page.wait_for_timeout(3000)

    # validation
    expect(page.locator("//p[@id='result']")).to_have_text("You entered: PLAYWRIGHT")
