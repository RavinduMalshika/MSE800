from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

class WindowsButton(Button):
    def click(self):
        print("Button Clicked in Windows")

class MacButton(Button):
    def click(self):
        print("Button Clicked in Mac")

class WindowsCheckbox(Checkbox):
    def check(self):
        print("Checked in Windows")

class MacCheckbox(Checkbox):
    def check(self):
        print("Checked in Mac")

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

WindowsFactory().create_button().click()
MacFactory().create_checkbox().check()
        