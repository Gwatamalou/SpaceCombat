import arcade
import arcade.gui
import game
from constants import *




class MainView(arcade.View):
    """окно начального экрана"""

    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()

        self.b_v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(text="Start", width=200)
        self.b_v_box.add(start_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
        self.b_v_box.add(settings_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.b_v_box.add(quit_button)

        @start_button.event('on_click')
        def on_click_start_button(event):
            main_view = game.MyGame()
            main_view.setup()
            self.window.show_view(main_view)

        @settings_button.event('on_click')
        def on_click_settings_button(event):
            main_view = MenuView(self)
            self.window.show_view(main_view)

        @quit_button.event('on_click')
        def on_click_quit_button(event):
            arcade.exit()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.b_v_box))

    def on_show_view(self):
        arcade.set_background_color((4, 10, 20))
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        self.clear()
        self.manager.draw()


class MenuView(arcade.View):
    """окно меню"""

    def __init__(self, main_view):
        super().__init__()

        self.manager = arcade.gui.UIManager()

        self.b_v_box = arcade.gui.UIBoxLayout()

        back_button = arcade.gui.UIFlatButton(text="Back", width=200)
        self.b_v_box.add(back_button)

        @back_button.event('on_click')
        def on_click_quit_button(event):
            self.window.show_view(main_view)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.b_v_box))

        self.main_view = main_view

    def on_hide_view(self):
        self.manager.disable()

    def on_show_view(self):
        arcade.set_background_color((4, 10, 20))

        self.manager.enable()

    def on_draw(self):
        self.clear()
        self.manager.draw()


class MenuWindow(arcade.Window):

    # создание окна
    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT, window_title=WINDOW_TITLE):
        super().__init__(window_width, window_height, window_title)


def main():
    window = MenuWindow()
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


if __name__ == '__main__':
    main()