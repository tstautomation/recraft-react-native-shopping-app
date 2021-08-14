from behave import use_step_matcher, step

from core.driver_manager import DriverFactory
from screen.home_screen import HomeScreen

use_step_matcher("re")


@step('User has launched the application')
def step_impl(context):
    DriverFactory().start()

