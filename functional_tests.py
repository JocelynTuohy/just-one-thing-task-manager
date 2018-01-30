"""Just One Thing functional testing module"""

# standard library imports


# pip installed
from selenium import webdriver

# app modules


browser = webdriver.Firefox()

# Amber has heard about a cool new online to-do app. She goes to check out its
# homepage.
browser.get('http://localhost:8000')

# She notices the page title and header mention 'Just One Thing'
assert 'Just One Thing' in browser.title

# She is invited to log in straight away.

# There is an option for her to register an account if she hasn't already.

# She attempts to log in but can't since she hasn't registered yet.

# She registers for a new account with amber@email.com.

# She creates a password and mistypes its confirmation.

# The website lets her know that she mistyped her password confirmation.

# This time she types in her new password correctly.

# The website confirms that she has registered (sending a confirmation email).

# There is a link so she can go log in now, and she follows it.

# She goes to log in but mistypes her password.

# The website does not allow her to log in with the wrong password.

# She types her password correctly this time.

# Now Amber is successfully logged in, and she arrives at her personal
# dashboard page.

# The dashboard displays a single task.

# The dashboard also displays a headline with a suggestion.

# The dashboard has a navigation section to the left.

# Amber has to rush off because she has an appointment, but she doesn't want
# her husband snooping in her account since she has tasks related to his
# surprise birthday party, so she logs off.

# Amber closes the browser and leaves for her appointment.abs

# Amber returns and is presented with the login screen again.

# Amber forgot her password while she was out, but fortunately there is a
# link to reset her password.

# She clicks the reset password link.

# A page asks her for her email address.

# She enters her email address incorrectly and hits submit.

# The page reads that a reset email will arrive if an account is found for that
# email address.

# Amber waits, but does not receive the email (since she typed her address
# incorrectly). There is a link to go back to the login page.

# She clicks the link and it takes her back to the login page.

# She clicks the reset password link again.

# She enters her email address correctly this time and hits submit.

# The page reads that a reset email will arrive if an account is found for that
# email address.

# Amber receives the password reset email and clicks the link in it.

# The link takes her to a page where it asks her to create and confirm her
# new password.

# She incorrectly types her password confirmation.

# The page tells her that the two fields don't match and lets her try again.

# She resets her password correctly this time.

# The page confirms success and asks her to try logging in again.

# She clicks the link to return to the login page.

# She logs in using the new password.

# She reaches the dashboard.

# She is sleepy, so she goes to bed.

# When Amber wakes up in the morning, she returns to the website to discover
# that it automatically keeps her logged in unless she logs out.

assert 'Django' in browser.title