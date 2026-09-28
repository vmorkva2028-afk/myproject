from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from datetime import datetime

# ---------- Тёмный фон ----------
Window.clearcolor = (0, 0, 0, 1)   # чёрный


class ClockApp(App):
    def build(self):
        # контейнер, центрирует метку
        layout = BoxLayout(
            orientation='vertical',
            padding=20
        )

        # ---------- Часы ----------
        self.time_label = Label(
            text='00:00:00',
            font_size='70sp',      # масштабируемый размер
            color=(0, 1, 0, 1),    # зелёный
            bold=True
        )

        layout.add_widget(self.time_label)

        # ---------- Автообновление каждую секунду ----------
        Clock.schedule_interval(self.update_time, 1)

        return layout

    def update_time(self, dt):
        now = datetime.now()
        self.time_label.text = now.strftime('%H:%M:%S')


if __name__ == '__main__':
    ClockApp().run()