from behave import given, when, then


@given('Open Reely main page')
def open_reelly(context):
    context.app.signin_page.open_signin_page()

@when('Logged in')
def logged_in(context):
    context.app.signin_page.sign_in()

@when('Click on Settings button')
def click_settings(context):
    context.app.settings_page.click_settings()

@when('Click on User guide button')
def click_user_guide(context):
    context.app.userguide_page.click_userguide()

@then('Verify that the right page opens')
def verify_right_page_opens(context):
    context.app.userguide_page.verify_userguide_page()

@then('Verify that all lesson videos contain titles')
def verify_lesson_videos(context):
    context.app.userguide_page.verify_video_block_title()