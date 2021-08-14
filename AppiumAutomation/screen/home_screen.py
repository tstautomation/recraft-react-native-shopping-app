import random
import string

from screen.base_screen import BaseScreen


def random_char(x):
    return ''.join(random.choice(string.ascii_letters) for x in range(x))


class HomeScreen(BaseScreen):

    def __init__(self):
        super(HomeScreen, self).__init__()

    def verify_launch_screen(self):
        self.assert_present(self.submision_league_title)

    def do_login(self, email, password):
        self.click(self.signin_btn)
        self.send_keys(self.email_input, email)
        self.send_keys(self.password_input, password)
        self.click(self.signin_submit_btn)
        self.wait_for_visible(self.search_bar_input)

    def verify_user_on_homescreen_after_login(self):
        self.wait_for_visible(self.search_bar_input)
        self.assert_present(self.search_bar_input)

    def do_signup(self, role):
        self.click(self.signup_btn)
        self.send_keys(self.email_input, random_char(10) + "@mailinator.com")
        self.send_keys(self.password_input, random_char(10))
        self.click(self.signup_submit_btn)
        self.wait_for_visible(self.coach_btn)
