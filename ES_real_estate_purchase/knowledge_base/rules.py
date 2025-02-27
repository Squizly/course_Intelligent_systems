rules = [
    # --- Жилой тип недвижимости ---

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Низкий",
            "Ипотека": "Нет",
            "Семейное положение": "Нет",
            "Количество комнат": "1"
        },
        "then": "Компактная студия эконом-класса для одного человека"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Низкий",
            "Ипотека": "Нет",
            "Семейное положение": "Да",
            "Количество комнат": "1"
        },
        "then": "Однокомнатная квартира эконом-класса для молодой семьи"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Низкий",
            "Ипотека": "Да",
            "Семейное положение": "Нет",
            "Количество комнат": "1"
        },
        "then": "Однокомнатная квартира комфорт-класса с выгодными ипотечными условиями"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Низкий",
            "Ипотека": "Да",
            "Семейное положение": "Да",
            "Количество комнат": "2"
        },
        "then": "Двухкомнатная квартира эконом-класса с ипотекой для небольшой семьи"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Средний",
            "Ипотека": "Нет",
            "Семейное положение": "Нет",
            "Количество комнат": "1"
        },
        "then": "Современная однокомнатная квартира комфорт-класса с удобной планировкой"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Средний",
            "Ипотека": "Нет",
            "Семейное положение": "Да",
            "Количество комнат": "2"
        },
        "then": "Двухкомнатная квартира комфорт-класса для семьи в хорошем районе"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Средний",
            "Ипотека": "Да",
            "Семейное положение": "Нет",
            "Количество комнат": "1"
        },
        "then": "Однокомнатная квартира повышенной комфортности с ипотечным кредитом"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Средний",
            "Ипотека": "Да",
            "Семейное положение": "Да",
            "Количество комнат": "2"
        },
        "then": "Двухкомнатная квартира комфорт-класса с ипотечным кредитом для семьи"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Высокий",
            "Ипотека": "Нет",
            "Семейное положение": "Нет",
            "Количество комнат": "3",
            "Расположение": "Октябрьский"
        },
        "then": "Просторная квартира премиум-класса с тремя комнатами в престижном районе Октябрьский"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Высокий",
            "Ипотека": "Нет",
            "Семейное положение": "Да",
            "Количество комнат": "4",
            "Расположение": "Октябрьский"
        },
        "then": "Роскошная четырехкомнатная квартира премиум-класса для семьи в центре города"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Высокий",
            "Ипотека": "Да"
        },
        "then": "Элитный пентхаус премиум-класса с эксклюзивным дизайном и панорамными окнами"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Высокий",
            "Расположение": "Ленинский"
        },
        "then": "Элитная квартира премиум-класса в одном из лучших районов Ленинский"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Низкий",
            "Ипотека": "Нет",
            "Семейное положение": "Да",
            "Количество комнат": "2",
            "Расположение": "Пригород"
        },
        "then": "Двухкомнатная квартира эконом-класса для семейной жизни в пригороде"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Средний",
            "Ипотека": "Нет",
            "Семейное положение": "Нет",
            "Количество комнат": "1",
            "Расположение": "Пригород"
        },
        "then": "Современная студия комфорт-класса в тихом пригородном районе"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Средний",
            "Ипотека": "Да",
            "Семейное положение": "Да",
            "Количество комнат": "3",
            "Расположение": "Советский"
        },
        "then": "Трехкомнатная квартира комфорт-класса с ипотекой для большой семьи в районе Советский"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Высокий",
            "Ипотека": "Нет",
            "Семейное положение": "Нет",
            "Количество комнат": "2",
            "Расположение": "Кировский"
        },
        "then": "Стильная двухкомнатная квартира премиум-класса с современным дизайном в районе Кировский"
    },

    {
        "if": {
            "Тип недвижимости": "Жилой",
            "Бюджет": "Высокий",
            "Ипотека": "Да",
            "Семейное положение": "Да",
            "Количество комнат": "3"
        },
        "then": "Элитная трехкомнатная квартира с ипотечным кредитованием и эксклюзивным дизайном для семьи"
    },
    
    # --- Коммерческий тип недвижимости ---

    {
        "if": {
            "Тип недвижимости": "Коммерческий",
            "Бюджет": "Высокий",
            "Расположение": "Октябрьский"
        },
        "then": "Бизнес-центр премиум-класса с корпоративными офисами"
    },

    {
        "if": {
            "Тип недвижимости": "Коммерческий",
            "Бюджет": "Высокий",
            "Количество комнат": "3"
        },
        "then": "Элитный офисный комплекс с несколькими рабочими зонами"
    },

    {
        "if": {
            "Тип недвижимости": "Коммерческий",
            "Бюджет": "Высокий"
        },
        "then": "Современный корпоративный офис премиум-класса"
    },

    {
        "if": {
            "Тип недвижимости": "Коммерческий",
            "Бюджет": "Средний",
            "Расположение": "Ленинский"
        },
        "then": "Офисное помещение комфорт-класса в деловом центре Ленинского района"
    },

    {
        "if": {
            "Тип недвижимости": "Коммерческий",
            "Бюджет": "Средний",
            "Количество комнат": "2"
        },
        "then": "Двухкомнатное коммерческое помещение комфорт-класса (офис/магазин)"
    },

    {
        "if": {
            "Тип недвижимости": "Коммерческий",
            "Бюджет": "Средний"
        },
        "then": "Многофункциональное коммерческое пространство комфорт-класса"
    },

    {
        "if": {
            "Тип недвижимости": "Коммерческий",
            "Бюджет": "Низкий",
            "Расположение": "Пригород"
        },
        "then": "Малый торговый пункт или кабинет эконом-класса в пригороде"
    },

    {
        "if": {
            "Тип недвижимости": "Коммерческий",
            "Бюджет": "Низкий",
            "Количество комнат": "1"
        },
        "then": "Компактный офис-кабинет или торговый пункт эконом-класса"
    },

    {
        "if": {
            "Тип недвижимости": "Коммерческий",
            "Бюджет": "Низкий"
        },
        "then": "Основное коммерческое помещение эконом-класса"
    },
    
    # --- Инвестиционный тип недвижимости ---

    {
        "if": {
            "Тип недвижимости": "Инвестиционный",
            "Бюджет": "Высокий",
            "Расположение": "Октябрьский"
        },
        "then": "Современные апартаменты для аренды премиум-класса в районе Октябрьский"
    },

    {
        "if": {
            "Тип недвижимости": "Инвестиционный",
            "Бюджет": "Высокий",
            "Количество комнат": "3"
        },
        "then": "Просторные апартаменты для инвестиций премиум-класса с тремя комнатами"
    },

    {
        "if": {
            "Тип недвижимости": "Инвестиционный",
            "Бюджет": "Высокий"
        },
        "then": "Апартаменты для аренды премиум-класса"
    },

    {
        "if": {
            "Тип недвижимости": "Инвестиционный",
            "Бюджет": "Средний",
            "Количество комнат": "2"
        },
        "then": "Уютная двухкомнатная квартира для инвестиций комфорт-класса"
    },

    {
        "if": {
            "Тип недвижимости": "Инвестиционный",
            "Бюджет": "Средний",
            "Расположение": "Ленинский"
        },
        "then": "Квартира для инвестиций комфорт-класса в районе Ленинский"
    },

    {
        "if": {
            "Тип недвижимости": "Инвестиционный",
            "Бюджет": "Средний"
        },
        "then": "Квартира для инвестиций комфорт-класса"
    },

    {
        "if": {
            "Тип недвижимости": "Инвестиционный",
            "Бюджет": "Низкий",
            "Количество комнат": "1"
        },
        "then": "Компактное жилье для инвестиций эконом-класса"
    },

    {
        "if": {
            "Тип недвижимости": "Инвестиционный",
            "Бюджет": "Низкий",
            "Расположение": "Пригород"
        },
        "then": "Небольшая студия для инвестиций эконом-класса в пригороде"
    },

    {
        "if": {
            "Тип недвижимости": "Инвестиционный",
            "Бюджет": "Низкий"
        },
        "then": "Бюджетное жилье для инвестиций эконом-класса"
    }
]