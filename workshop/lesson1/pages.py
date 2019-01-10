# This file defines how the participants move from page to another.
# Each page is a python class.
# Under the class, you can define for example:
#### - Form fields to collect data with
#### - Template variables (custom variables) for the page
#### - Conditions to whom or when the page is shown
#### - Wait pages that make sure the group members enter a page at the same time
#### - Trigger functions that for example calculate the payoffs before the results page

# Each page has a corresponding html template under the templates/lesson1 folder

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

# For this exercise, you create a two player game where the two players have two roles:
# Trustee and the truster
# The two people receive at first common instructions, after which the truster decides how much to trust and then
# the trustee decides how much to return back.

# The model is ready set, the game has 2 players, form fields for trust decision and reciprocity decision,
# variables and functions for payoffs

# Task 1: Create the first page for instructions shown to all called "Instructions"
# 1. Create a class Instructions that herits from the general oTree Page
# 2. Create in the templates/lesson1 a html file called Instructions.html and add the instructions there.
# 3. Add Instructions first on the page sequence

# In doing the page, you can replace the default pages such as "MyPage" either by deleting it or by refactoring and
# renaming it.


class MyPage(Page):
    pass


# Task 2: The page for the truster decision is ready made, called TrustDecision. Using this as the model,
# Create the ReciprocityDecision page. Note that you need a similar waiting page as well.
# Create class called ReciprocityDecision inheriting from the oTree Page
# Add formfield for reciprocity under the group
# Create class ReciprocityWaitPage inheriting from the oTree WaitPage
# Add the after_all_players_arrive function to the ReciprocityWaitPage and trigger the payoff function after by adding:
####
# Create html page called ReciprocityDecision in the templates/lesson1 folder
# Add the required instructions and form field on the html page
# Add the new pages to the page sequence

class TrustDecision(Page):
    pass


class TrustWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage,
    TrustDecision,
    ResultsWaitPage,
    Results
]
