"""_module summary_"""
import importlib

import View.LoginScreen.login_screen
from View import LoginScreenView

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.LoginScreen.login_screen)


class LoginScreenController:
    """
    The `LoginScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel
        self.views = [LoginScreenView(self, self.model)]


    def get_views(self) -> list[LoginScreenView]:
        """Gets the view connected to this controller.

        Returns:
            LoginScreenView: The view connected to this controller.
        """
        return self.views

    def get_then_clear(self): 
        # print(self.views[0].store_input())
        self.get_list_view()
        self.clear_tf()

    def get_list_view(self):
        self.logindata = self.views[0].store_input()
        self.model.check_data(self.logindata)
    
    def clear_tf(self):
        self.views[0].ids.textfld_username.text = ""
        self.views[0].ids.textfld_pw.text = ""
    