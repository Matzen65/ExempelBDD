
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


@then(u'blir användaren inloggad och kan se saldot')
def step_user_is_logged_in(context):
    assert context.login_result is True, "inloggningen misslyckades"
    print("Inloggning ok")


@when(u'användaren anger Kalle som användarnamn')
def step_when_user_kalle(context):
    context.username ="kalle"
    context.password =""
    context.login_result = login(context.username, context.password)
    print("Loggade in med kalle")


@then(u'visa ett felmeddelande om användarnamn och lösenord')
def step_then_failed_login(context):
    assert context.login_result is False, "Inloggning lyckad trots fel uppgifter"


@when(u'användaren inte skriver in något alls')
def step_when_user_no_username(context):
    context.username = ""
    context.password = ""
    context.login_result = login(context.username, context.password)
    print("Anv inga uppgifter")

@when(u'användaren anger "{username}" och "{password}”')
def step_when_username_and_password(context, username, password):
    context.login_result = login(username, password)
    print("Testar {username} och {password}")




