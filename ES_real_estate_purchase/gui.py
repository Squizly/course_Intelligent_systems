import customtkinter, os
from PIL import Image


class RealEstateApp(customtkinter.CTk):
    def __init__(self):
        # Конструктор родительского класса
        super().__init__()

        # Настройка окна приложения
        self.title("Интеллектуальные системы")
        self.geometry("750x450")

        # Подключаем изображения
        self.connect_image()

        # Устанавливаем размер сетки 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Создаем навигационное в меню и делаем окна под них
        self.create_navigation_menu()

        # По-умолчанию выбран фрейм с недвижимостью
        self.select_frame_by_name("real_estate")
    
    def create_navigation_menu(self):
        # === === === === === === === === === === === === === === === === === #
        # Создаем навигационное меню
        # === === === === === === === === === === === === === === === === === #

        # Создаем фрейм под навигационное меню
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        # Добавляем баннер с изображением и надписью
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Экспертная система", image = self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(family="Verdana", size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Кнопка переключения на фрейм с недвижимостью
        self.real_estate_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Недвижимость",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.real_estate_image, anchor="w", command=self.real_estate_button_event,
                                                   font=customtkinter.CTkFont(family="Verdana", size=12, weight="bold"))
        self.real_estate_button.grid(row=1, column=0, sticky="ew")

        # Комбо-бокс с темами интерфейса (светлый/тёмный)
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Тёмная", "Светлая", "Системная"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # === === === === === === === === === === === === === === === === === === === === === === === === #

        # === === === ==== === === === === Создаем фрейм с недвижимостью === === === === ==== === === === #

        self.real_estate_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.real_estate_frame.grid_columnconfigure(0, weight=1)

        # === === === === === === === === === === === === === === === === === === === === === === === === #


    def select_frame_by_name(self, name):
        # === === === === === === === === === === === === === === === === === #
        # Переключаемся на заданный фрейм
        # === === === === === === === === === === === === === === === === === #

        # Устанавливаем цвет для выбранной кнпоки
        self.real_estate_button.configure(fg_color=("gray75", "gray25") if name == "real_estate" else "transparent")

        # Показываем выбранный фрейм
        if name == "real_estate":
            self.real_estate_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.real_estate_frame.grid_forget()

    def real_estate_button_event(self):
        # === === === === === === === === === === === === === === === === === #
        # Переключаемся на фрейм с недвижимостью
        # === === === === === === === === === === === === === === === === === #

        self.select_frame_by_name("real_estate")

    def change_appearance_mode_event(self, new_appearance_mode):
        # === === === === === === === === === === === === === === === === === #
        # Смена темы интерфейса
        # === === === === === === === === === === === === === === === === === #

        if new_appearance_mode == "Светлая":
            customtkinter.set_appearance_mode("Light")
        elif new_appearance_mode == "Тёмная":
            customtkinter.set_appearance_mode("Dark")
        else:
            customtkinter.set_appearance_mode("System")
    
    def connect_image(self):
        # === === === === === === === === === === === === === === === === === #
        # Подключаем изображения для кнопок и баннера
        # === === === === === === === === === === === === === === === === === #

        image_path = os.path.join(os.path.dirname(os.path.relpath(__file__)), "images")

        # Логотип баннера
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(25,32))

        # Иконка домика
        self.real_estate_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "real_estate_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "real_estate_light.png")), size=(20, 20))