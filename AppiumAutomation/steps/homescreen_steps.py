from behave import use_step_matcher, when, then

from screen.home_screen import HomeScreen

use_step_matcher("re")


@when(u'User does login with (?P<email>\S+) and (?P<password>\S+)')
def step_impl(context, email, password):
    HomeScreen().do_login(email, password)


@then(u'Verify user on homescreen after login')
def step_impl(context):
    HomeScreen().verify_user_on_homescreen_after_login()


@when(u'User signup for the (?P<role>\S+) role')
def step_impl(context, role):
    HomeScreen().do_signup(role)
