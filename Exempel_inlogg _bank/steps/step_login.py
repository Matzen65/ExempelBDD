
from behave import given, when, then


def login(username, password):
    correct_username = "test"
    correct_password = "letmein"
    return username == correct_username and password == correct_password


@given(u'användaren befinner sig på inloggningssidan')
def step_given_login_page(context):
    context.page = "login_page"
    print("Användaren är på inloggningssidan")


@when(u'användaren anger sitt användarnamn och lösenord')
def step_when_username_and_password(context):
    context.username = "test"
    context.password = "letmein"
    context.login_result = login(context.username, context.password)
    print("Användaren angav rätt lösenord")


@when(u'klickar på logga in knappen')
def step_when_click_login(context):
    context.button = True
    print("knappen är tryckt")


@then(u'blir användaren inloggad och kan se saldot på startsidan')
def step_user_is_logged_in(context):
    assert context.login_result is True, "inloggningen misslyckades"
    print("Inloggning ok")

