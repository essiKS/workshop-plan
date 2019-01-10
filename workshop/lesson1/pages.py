from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

# This file defines how the participants move from one page to another.
# Each page is a python class.
# Under the class, you can define for example:
# ### - Form fields to collect data with
# ### - Template variables (custom variables) for the page
# ### - Conditions to whom or when the page is shown
# ### - Wait pages that make sure the group members enter a page at the same time
# ### - Trigger functions that for example calculate the payoffs before the results page

# Each page has a corresponding html template under the templates/lesson1 folder

# For this exercise, you create a two player game where the two players have two roles:
# Trustee and Trustor
# At first, the two receive common instructions
# This is followed by the trustor deciding how much to trust
# After which the trustee decides how much to return back.

# The model is ready set, the game has 2 players, form fields for trust decision and reciprocity decision,
# variables and functions for payoffs

# You can copy the right way to do things from the pages.py file of the previous session: welcome

# ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###


# Task 1: Create the first page for instructions shown to all participants called "Instructions"

# 1. Create a class Instructions that inherits from the general oTree Page
# 2. You find a corresponding Instructions.html file in the templates/lesson1 directory
# 3. Add Instructions first on the page sequence in the bottom of this file.

# In doing the page, you can replace the lines for the default page "MyPage"

class MyPage(Page):
    pass

# ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###


class TrustDecision(Page):
    def is_displayed(self):
        if self.player.role() == "trustor":
            return True

    form_model = 'group'
    form_fields = ['trust']


# Task 2: Page for the trustee's decision

# TIP: The pages for the trustor's decision is ready made, called TrustDecision.
# You can see it above and use it as a relevant example to copy paste from.

# 1. Create class called ReciprocityDecision inheriting from the oTree Page
# 2. Use the 'is_displayed' function to limit access to this page to only trustees
# 3. Add a formfield for 'reciprocity' under the 'group' model
# 4. Add a template variable for the multiplied points by using the vars_for_template(self) function:
#           def vars_for_template(self):
#           (indented) multiplied_points = 3 * self.group.trust
#           (indented) return {'multiplied': multiplied_points}
# 5. Add the page ReciprocityDecision to the page sequence in the bottom of this page

# ### The page information set above and the features of a html page called ReciprocityDecision must correspond. Thus:

# 6. Create html page called ReciprocityDecision in the templates/lesson1 folder
# ### (right click the lesson1 folder, select new HTML file)
# 7. Add the required instructions (feel free to modify):
# TIP: You can copy paste the usual Django functions from an existing html template
# #### - title: "Reciprocity decision"
# #### - results so far:    "A trustor has trusted {{ player.trust }} points to you.
#                           After multiplication, this amounts to {{ multiplied }} points."
# #### - decision: "How many points do you send to the trustor out of these {{ multiplied }} points?
# 8. Add the formfield group.reciprocity
# TIP: See MyPage.html in the welcome app for examples
# 9. Add a next_button

# ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###


class TrustWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


# Task 3: Wait page
# While one of the players is making a decision, the other is waiting.
# You can see an example of a wait page class above.

# 1. Create class ReciprocityWaitPage inheriting from the oTree WaitPage
# 2. Define the after_all_players_arrive function for the wait page
# 3. Trigger the payoff function 'set_payoffs' under the 'after_all_players_arrive' function by adding the following:
#    (indented) self.group.set_payoffs()
# 4. Add the page ReciprocityWaitPage to the page sequence in the bottom of this file.

# You do not need a corresponding waiting page template - the generic waiting page will do.
# If needed, you can modify the wait page, see instructions using the link below
# https://otree.readthedocs.io/en/latest/multiplayer/waitpages.html#customizing-the-wait-page-s-appearance


class Results(Page):
    pass

# Task 4: Modify the result page such that you show each player their payoffs.
# More instructions in the Results.html.

# Task 5: To have multiple rounds in the game:
# 1. Go to models.py file and change the num_rounds variable under the constants to 2.
# 2. Add a condition to the instruction page such that it is only displayed in the first round.
# TIP The variable round is stored under the player model.
# 3. Add the round marker to each of the decision pages, f. ex. in the title.

# Question: What does the "self" do?


page_sequence = [
    MyPage,
    TrustDecision,
    TrustWaitPage,
    Results
]
