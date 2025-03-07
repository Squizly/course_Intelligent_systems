import customtkinter, os
from PIL import Image


class RealEstateApp(customtkinter.CTk):
    def __init__(self):

        # === === === === === === === === === === === === === === === === === #
        # Инициализация графического интерфейса
        # === === === === === === === === === === === === === === === === === #

        # Конструктор родительского класса
        super().__init__()

        # Настройка окна приложения
        self.title("Интеллектуальные системы")
        self.geometry("750x450")

        # Делаем размер окна статичным
        self.resizable(False, False)

        # Подключаем изображения
        self.connect_image()

        # Устанавливаем размер сетки 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Создаем навигационное в меню и делаем окна под них
        self.create_navigation_menu()

        # Настройка фрейма под недвижимость
        self.create_real_estate_frame()

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
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Системная", "Тёмная", "Светлая"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # === === === === === === === === === === === === === === === === === === === === === === === === #
    
    def create_real_estate_frame(self):
        # === === === === === === === === === === === === === === === === === #
        # Создаем фрейм под недвижимость
        # === === === === === === === === === === === === === === === === === #

        # Область под недвижимость
        self.real_estate_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.real_estate_frame.grid_columnconfigure(0, weight=1)

        # Кнопка предсказать -> получить результат
        self.home_frame_button_predict = customtkinter.CTkButton(self.real_estate_frame, text="Предсказать", width=400, height=70, 
                                                                 command=self.get_predict_real_estate, fg_color="#0078D7", corner_radius=15,
                                                                 hover_color="#005A9E", font=("Comic Sans MS", 30, "bold"))
        self.home_frame_button_predict.grid(row=1, columnspan=2, padx=10, pady=(20,40))


        # === === === Бюджет на покупку === === === #

        self.budget_label = customtkinter.CTkLabel(self.real_estate_frame, text="Какую сумму (в рублях) вы готовы потратить на покупку недвижимости?",
                                                   font=("Verdana", 12, "bold"), wraplength=320)
        self.budget_label.grid(row=2, column=0, padx=20, pady=15, sticky="w")

        # Добавим проверку на ввод бюджета ---> только числовые значения
        vcmd = (self.register(self.validate_budget), "%P")

        self.input_budget_entry = customtkinter.CTkEntry(self.real_estate_frame, width=100, font=("Vedana",12,"bold"),validate="key", validatecommand=vcmd)
        self.input_budget_entry.grid(row=2, column=1, padx=20, pady=15, sticky="w")


        # === === === Семейное положение === === === #

        self.family_label = customtkinter.CTkLabel(self.real_estate_frame, text="Состоите ли вы в каком-либо браке?", font=("Verdana", 12, "bold"))
        self.family_label.grid(row=3, column=0, padx=20, pady=15, sticky="w")

        self.input_family_combobox = customtkinter.CTkComboBox(self.real_estate_frame, values=["Нет", "Да"], justify="center", 
                                                               font=("Verdana", 12, "bold"), width=100, state="readonly")
        self.input_family_combobox.grid(row=3, column=1, padx=20, pady=15, sticky="w")

        # Установка значения по умолчанию
        self.input_family_combobox.set("Нет")

        # === ==== === Количество детей === ==== === # 

        self.children_label = customtkinter.CTkLabel(self.real_estate_frame, text="Сколько у вас детей?", font=("Verdana", 12, "bold"))
        self.children_label.grid(row=4, column=0, padx=20, pady=15, sticky="w")

        self.input_children_combobox = customtkinter.CTkComboBox(self.real_estate_frame, values=["0","1","2","3","4","5"], 
                                                                 justify="center", font=("Verdana", 12, "bold"), width=100, state="readonly")
        self.input_children_combobox.grid(row=4, column=1, padx=20, pady=15, sticky="w")

        # Установка значения по умолчанию
        self.input_children_combobox.set("0")

        # ==== === ==== Инфраструктура ==== === ==== #

        self.infrastructure_label = customtkinter.CTkLabel(self.real_estate_frame, text="Вам важно наличие развитой инфраструктуры?", font=("Verdana", 12, "bold"))
        self.infrastructure_label.grid(row=5, column=0, padx=20, pady=15, sticky="w")

        self.input_infrastructure_combobox = customtkinter.CTkComboBox(self.real_estate_frame, values=["Да", "Нет"], justify="center", 
                                                                       font=("Verdana", 12, "bold"), width=100, state="readonly")
        self.input_infrastructure_combobox.grid(row=5, column=1, padx=20, pady=15, sticky="w")

        # Установка значения по умолчанию
        self.input_infrastructure_combobox.set("Да")
    
    def validate_budget(self, new_value):

        # === === === === === === === === === === === === === === === === === #
        # Ограничения на ввод бюджета
        # Это должно быть только числовое значение
        # === === === === === === === === === === === === === === === === === #

        if new_value.isdigit() or new_value == "":
            return True
        
        return False

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