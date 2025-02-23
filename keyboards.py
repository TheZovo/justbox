from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from admin_settings import reviews_link

start_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Оформить заказ ❤️", callback_data="place_order"),
        ],
        [
            types.InlineKeyboardButton(text="Калькулятор стоимости 💰", callback_data="calc_cost"),
        ],
        [
            types.InlineKeyboardButton(text="Отзывы о нашей работе ✉️", url=f"https://t.me/{reviews_link}"),
        ],
        [
            types.InlineKeyboardButton(text="Ответы на популярные вопросы ❓", callback_data="faq"),
        ],
        [
            types.InlineKeyboardButton(text="Задать вопрос 📞", callback_data="ask_question"),
        ],
        [
            types.InlineKeyboardButton(text="Скачать POIZON iOS 📱", url="https://apps.apple.com/ru/app/得物-得到运动x潮流x好物/id1012871328"),
        ],
        [
            types.InlineKeyboardButton(text="Скачать POIZON Android 🤖", url="https://m.anxinapk.com/rj/12201303.html"),
        ]
    ])


faq_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Что такое POIZON?", callback_data="what_is_poizon"),
        ],
        [
            types.InlineKeyboardButton(text="Безопасны ли платежи здесь?", callback_data="safe_payment"),
        ],
        [
            types.InlineKeyboardButton(text="Какая у вас комиссия?", callback_data="commission"),
        ],
        [
            types.InlineKeyboardButton(text="Какой срок доставки?", callback_data="delivery_time"),
        ],
        [
            types.InlineKeyboardButton(text="В какие страны доставляетесь?", callback_data="delivery_countries"),
        ],
        [
            types.InlineKeyboardButton(text="Какие методы оплаты?", callback_data="payment_methods"),
        ],
        [
            types.InlineKeyboardButton(text="Получить товар применив QR код?", callback_data="qr_code"),
        ],
        [
            types.InlineKeyboardButton(text="Как отслеживать заказ?", callback_data="track_order"),
        ],
        [
            types.InlineKeyboardButton(text="Как правильно подобрать размер?", callback_data="correct_size"),
        ],
        [
            types.InlineKeyboardButton(text="Как заказать с 95 товаров по акции?", callback_data="order_with_95"),
        ],
        [
            types.InlineKeyboardButton(text="Как найти кроссовки?", callback_data="find_sneakers"),
        ],
        [
            types.InlineKeyboardButton(text="Не нашел нужной категории", callback_data="other_categories"),
        ],
        [
            types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back_to_menu"),
        ],
    ])

order_keyboard_1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Далее")],
        [KeyboardButton(text="Вернуться в меню")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

order_keyboard_2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Дальше")],
        [KeyboardButton(text="Вернуться в меню")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

order_keyboard_3 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да, уверен!")],
        [KeyboardButton(text="Вернуться в меню")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

order_kb_all = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="👞 Обувь", callback_data="category_shoes"),
        InlineKeyboardButton(text="🧥 Верхняя одежда", callback_data="category_outerwear")
    ],
    [
        InlineKeyboardButton(text="👖 Штаны", callback_data="category_pants"),
        InlineKeyboardButton(text="🩲 Нижнее белье", callback_data="category_underwear")
    ],
    [
        InlineKeyboardButton(text="🧢 Головные уборы", callback_data="category_headwear"),
        InlineKeyboardButton(text="🧦 Носки", callback_data="category_socks")
    ],
    [
        InlineKeyboardButton(text="👜 Сумки / рюкзаки", callback_data="category_bags"),
        InlineKeyboardButton(text="🛍 Аксессуары", callback_data="category_accessories")
    ],
    [
        InlineKeyboardButton(text="💄 Косметика", callback_data="category_cosmetics"),
        InlineKeyboardButton(text="📱 Электроника", callback_data="category_electronics")
    ],
    [
        InlineKeyboardButton(text="🏀 Спорт", callback_data="category_sport"),
        InlineKeyboardButton(text="🐻 Фигурки", callback_data="category_figures")
    ],
    [
        InlineKeyboardButton(text="⬅️ Назад", callback_data="category_back")
    ]
])

shoes_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Кроссовки", callback_data="sneakers")
    ],
    [
        InlineKeyboardButton(text="Ботинки", callback_data="boots"),
        InlineKeyboardButton(text="Кеды", callback_data="kedi")
    ],
    [
        InlineKeyboardButton(text="Шлепанцы", callback_data="flip-flops"),
        InlineKeyboardButton(text="Сандали", callback_data="sandals")
    ],
    [
        InlineKeyboardButton(text="Бутсы", callback_data="football_boots"),
        InlineKeyboardButton(text="Туфли", callback_data="shoes")
    ],
    [
        InlineKeyboardButton(text="⬅️ Назад", callback_data="category_back")
    ]
])

outerwear_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Пуховик", callback_data="downjacket"),
        InlineKeyboardButton(text="Жилетка", callback_data="vest")
    ],
    [
        InlineKeyboardButton(text="Парка", callback_data="parka"),
        InlineKeyboardButton(text="Легкая куртка", callback_data="lightjacket")
    ],
    [
        InlineKeyboardButton(text="Ветровка", callback_data="windbreaker"),
        InlineKeyboardButton(text="Пиджак", callback_data="blazer")
    ],
    [
        InlineKeyboardButton(text="Худи / Толстовка", callback_data="hoodie"),
        InlineKeyboardButton(text="Лонгслив", callback_data="longslive")
    ],
    [
        InlineKeyboardButton(text="Футболка / Рубашка", callback_data="shirts"),
        InlineKeyboardButton(text="Топ", callback_data="top")
    ],
    [
        InlineKeyboardButton(text="⬅️ Назад", callback_data="category_back")
    ]
])

pants_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Джинсы", callback_data="jeans"),
        InlineKeyboardButton(text="Брюки", callback_data="pants")
    ],
    [
        InlineKeyboardButton(text="Шорты", callback_data="shorts"),
    ],
    [
        InlineKeyboardButton(text="⬅️ Назад", callback_data="category_back")
    ]
])

underwear_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Нижнее белье (муж)", callback_data="underwearMen")
    ],
    [
        InlineKeyboardButton(text="Нижнее белье (жен)", callback_data="underwearWomen")
    ],
    [
        InlineKeyboardButton(text="Комплект нижнего белья", callback_data="completeUnderwear")
    ],
    [
        InlineKeyboardButton(text="⬅️ Назад", callback_data="category_back")
    ]
])

hats_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Шапка", callback_data="hat")
    ],
    [
        InlineKeyboardButton(text="Кепка", callback_data="kepka")
    ],
    [
        InlineKeyboardButton(text="Снуд", callback_data="snud")
    ],
    [
        InlineKeyboardButton(text="Теплый шарф", callback_data="warm_scarf")
    ],
    [
        InlineKeyboardButton(text="Легкий шарф", callback_data="light_scarf")
    ],
    [
        InlineKeyboardButton(text="⬅️ Назад", callback_data="category_back")
    ]
])

socks_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1 пара", callback_data="1pair")
    ],
    [
        InlineKeyboardButton(text="2 пары", callback_data="2pairs")
    ],
    [
        InlineKeyboardButton(text="3 пары", callback_data="3pairs")
    ],
    [
        InlineKeyboardButton(text="⬅️ Назад", callback_data="category_back")
    ]
])

bags_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Женская сумка маленькая", callback_data="woman_small_bag")
    ],
    [
        InlineKeyboardButton(text="Женская сумка большая", callback_data="woman_big_bag")
    ],
    [
        InlineKeyboardButton(text="Рюкзак", callback_data="bag")
    ],
    [
        InlineKeyboardButton(text="Чемодан", callback_data="suitcase")
    ],
    [
        InlineKeyboardButton(text="Дорожная сумка", callback_data="roadbag")
    ],
    [
        InlineKeyboardButton(text="Сумка через плечо", callback_data="bag_shoulder")
    ],
    [
        InlineKeyboardButton(text="Бананка", callback_data="bananka")
    ],
    [
        InlineKeyboardButton(text="⬅️ Назад", callback_data="category_back")
    ]
])

accessory_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Очки", callback_data="glasses")],
    [InlineKeyboardButton(text="Часы", callback_data="nails")],
    [InlineKeyboardButton(text="Украшения", callback_data="jewelry")],
    [InlineKeyboardButton(text="Ремни", callback_data="belts")],
    [InlineKeyboardButton(text="Перчатки", callback_data="gloves")],
    [InlineKeyboardButton(text="Назад", callback_data="back_accessory")],
])


cosmetics_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Парфюм", callback_data="perfume")],
    [InlineKeyboardButton(text="Крем для лица/рук", callback_data="cream")],
    [InlineKeyboardButton(text="Помада", callback_data="lipstick")],
    [InlineKeyboardButton(text="Прочие", callback_data="other")],
    [InlineKeyboardButton(text="Назад", callback_data="category_back")],
])


electronics_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ноутбук", callback_data="laptop")],
    [InlineKeyboardButton(text="Телефон", callback_data="phone")],
    [InlineKeyboardButton(text="Платформы", callback_data="platforms")],
    [InlineKeyboardButton(text="Часы", callback_data="watches")],
    [InlineKeyboardButton(text="Наушники TWS", callback_data="tws_earbuds")],
    [InlineKeyboardButton(text="Проводные наушники", callback_data="wired_earbuds")],
    [InlineKeyboardButton(text="Клавиатура", callback_data="keyboard")],
    [InlineKeyboardButton(text="Мышь", callback_data="mouse")],
    [InlineKeyboardButton(text="Видеокарта", callback_data="graphics_card")],
    [InlineKeyboardButton(text="Системный блок", callback_data="pc_case")],
    [InlineKeyboardButton(text="Назад", callback_data="category_back")]
])


sport_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Баскетбольный мяч", callback_data="basketball_ball")],
    [InlineKeyboardButton(text="Футбольный мяч", callback_data="football_ball")],
    [InlineKeyboardButton(text="Волейбольный мяч", callback_data="volleyball_ball")],
    [InlineKeyboardButton(text="Шлем", callback_data="helmeet")],
    [InlineKeyboardButton(text="Другое", callback_data="other_sport")],
    [InlineKeyboardButton(text="Назад", callback_data="category_back")]
])

figures_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Bearbrick 100%", callback_data="bb100")],
    [InlineKeyboardButton(text="Bearbrick 400%", callback_data="bb400")],
    [InlineKeyboardButton(text="Bearbrick 1000%", callback_data="bb1000")],
    [InlineKeyboardButton(text="Назад", callback_data="category_back")]
])

deliveries_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Автомобильная доставка", callback_data="autodelivery")]
])

skip_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Пропустить")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

order_confirmation_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Изменить", callback_data="edit_order")],
    [InlineKeyboardButton(text="Все верно", callback_data="confirm_order_final")],
])

menu_back = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вернуться в меню")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)