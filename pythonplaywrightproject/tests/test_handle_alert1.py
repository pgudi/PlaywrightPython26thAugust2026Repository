from playwright.sync_api import Page, expect

def test_handle_simple_alert01(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.wait_for_timeout(3000)

    # Event Listener
    def handle_alert(dialog):
        message=dialog.message
        print("Alert Message:",message)
        dialog.accept()

    page.on("dialog",handle_alert)
    # Click on JS Alert
    page.locator("//button[normalize-space()='Click for JS Alert']").click()
    page.wait_for_timeout(3000)

    # validation
    expect(page.locator("//p[@id='result']")).to_have_text("You successfully clicked an alert")


def test_handle_simple_alert02(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.wait_for_timeout(3000)

    # Event Listener
    page.on("dialog", lambda dialog:(print( "Alert Message :",dialog.message), dialog.accept()))
    
    # Click on JS Alert
    page.locator("//button[normalize-space()='Click for JS Alert']").click()
    page.wait_for_timeout(3000)

    # validation
    expect(page.locator("//p[@id='result']")).to_have_text("You successfully clicked an alert")
