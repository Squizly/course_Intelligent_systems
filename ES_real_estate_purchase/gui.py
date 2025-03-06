import customtkinter


class RealEstateApp(customtkinter.CTk):
    def __init__(self):
        # Конструктор родительского класса
        super().__init__()

        # Настройка окна приложения
        self.title("Экспертная система по подбору недвижимости")
        self.geometry("750x450")