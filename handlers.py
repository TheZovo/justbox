import os
import random
import sqlite3
from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import F
from aiogram.utils.markdown import hlink

import admin_settings
from keyboards import *
from states import *
from admin_settings import *
from db import db, DB
from config import config



router = Router()



@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    telegram_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    try:
        with DB("justbox.db") as db_instance:
            db_instance.add_user(telegram_id, username)
        await message.answer("""
    😉Добро пожаловать в бот группы Just Box!

    Наша группа поможет Вам выкупить товары с ЛЮБЫХ китайских площадок, например:
    1⃣ POIZON (DEWU)
    2⃣ taobao.com
    3⃣ и другие.

    ⛔️Все расчеты, заказы и оплата производятся ТОЛЬКО В БОТЕ. Мы не принимаем оплату в личных сообщениях!⛔️

    ⚠️ Товар возврату и обмену не подлежит. Мы оказываем услуги только выкупа и доставки товаров.
                            """, reply_markup=start_keyboard)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")

@router.callback_query(F.data == 'place_order')
async def process_callback_order(call: CallbackQuery, state: FSMContext):
    await call.message.answer_photo(
        photo = FSInputFile("./images/1.png"),
        caption='''Пожалуйста проверьте свой товар, на наличие ≈ (приблизительного равно), к сожалению данные товары наша команда выкупить для Вас не сможет.

Почему? Товары с ≈ доставляются в Китай из другой страны, а из-за таможенных лимитов Китайской таможенной службы, к сожалению выкуп данных товаров невозможен.

Просто нажмите ДАЛЕЕ, чтобы перейти к следующему шагу.''',
        reply_markup=order_keyboard_1
    )
    

@router.message(F.text == 'Далее')
async def process_order1(message: Message, state: FSMContext):
    await message.answer_photo(
    photo = FSInputFile("./images/2.png"),
    caption='''Пожалуйста, подтвердите, что Ваш товар не имеет ≈ приблизительного равно, перед ценой. 

Такие товары к сожалению мы выкупить не сможем.

Просто нажмите далее, чтобы перейти к следующему шагу.''', reply_markup=order_keyboard_2
)

@router.message(F.text == 'Дальше')
async def process_order2(message: Message, state: FSMContext):
    await message.answer_photo(
    photo = FSInputFile("./images/3.png"),
    caption='''Вы уверены, что Ваш товар не имеет ≈ приблизительного равно перед ценой?

Такие товары к сожалению мы выкупить не сможем.''', reply_markup=order_keyboard_3
)

@router.message(F.text == 'Да, уверен!')
async def process_order3(message: Message, state: FSMContext):
    await message.answer_photo(
    photo = FSInputFile("./images/4.png"),
    caption='''📊 В нашем калькуляторе Вы можете сделать расчет стоимости товара с 🚚 доставкой до России.

‼️ Товары с ≈ НЕ ВЫКУПАЕМ.

⚠️ Товар возврату и обмену не подлежит. Мы оказываем услуги только выкупа и доставки товаров.''', reply_markup=order_kb_all
)

@router.message(F.text == 'Вернуться в меню')
async def process_order_cancel(message: Message, state: FSMContext):
    await message.answer("""
😉Добро пожаловать в бот группы Just Box!

Наша группа поможет Вам выкупить товары с ЛЮБЫХ китайских площадок, например:
1⃣ POIZON (DEWU)
2⃣ taobao.com
3⃣ и другие.

⛔️Все расчеты, заказы и оплата производятся ТОЛЬКО В БОТЕ. Мы не принимаем оплату в личных сообщениях!⛔️

⚠️ Товар возврату и обмену не подлежит. Мы оказываем услуги только выкупа и доставки товаров.
                        """, reply_markup=start_keyboard)

@router.callback_query(F.data == 'category_shoes')
async def process_callback_shoes(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬 Выберите подходящий раздел:", reply_markup=shoes_kb)



@router.callback_query(F.data == 'calc_cost')
async def process_callback_calc(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите вес (в кг) и расстояние (в км) для расчета стоимости доставки.")
    await state.set_state(Calc.cost)
    await call.answer()

@router.message(Calc.cost)
async def process_cost(message: Message, state: FSMContext):
    try:
        weight, distance = map(float, message.text.split())
        costRUB = admin_settings.costRUB(weight, distance)
        costUSD = admin_settings.costUSD(weight, distance)
        await message.answer(f"""Стоимость доставки: 
{costRUB:.2f} RUB
{costUSD:.2f} USD""", reply_markup=menu_back)
        await state.clear()
    except ValueError:
        await message.answer("Пожалуйста, введите вес и расстояние в формате 'вес кг расстояние км' (например, '2 500').")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")

@router.callback_query(F.data == 'faq')
async def process_callback_faq(call: CallbackQuery, state: FSMContext):
    await call.message.answer("😉 Ответы на самые популярные вопросы уже ждут Вас.", reply_markup=faq_keyboard)
    await call.answer()


@router.callback_query(F.data.in_(list(faq_answers.keys())))
async def process_faq_answer(call: CallbackQuery, state: FSMContext):
    answer = faq_answers[call.data]
    await call.message.edit_text(answer, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Вернуться в меню", callback_data="back_to_menu")]
    ]))
    await call.answer()


@router.callback_query(F.data == 'ask_question')
async def process_callback_ask_question(call: CallbackQuery, state: FSMContext):
    await call.message.answer(ask_question, reply_markup=menu_back)
    
@router.callback_query(F.data == 'back_to_menu')
async def process_back_to_menu(call: CallbackQuery):
    await call.message.edit_text("""
😉Добро пожаловать в бот группы Just Box!

Наша группа поможет Вам выкупить товары с ЛЮБЫХ китайских площадок, например:
1⃣ POIZON (DEWU)
2⃣ taobao.com
3⃣ и другие.

⛔️Все расчеты, заказы и оплата производятся ТОЛЬКО В БОТЕ. Мы не принимаем оплату в личных сообщениях!⛔️

⚠️ Товар возврату и обмену не подлежит. Мы оказываем услуги только выкупа и доставки товаров.
                        """, reply_markup=start_keyboard)


@router.callback_query(F.data == 'category_shoes')
async def process_callback_shoes(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬 Выберите подходящий раздел:", reply_markup=shoes_kb)
@router.callback_query(F.data == 'category_outerwear')
async def process_callback_shoes(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬 Выберите подходящий раздел:", reply_markup=outerwear_kb)
@router.callback_query(F.data == 'category_pants')
async def process_callback_shoes(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬 Выберите подходящий раздел:", reply_markup=pants_kb)
@router.callback_query(F.data == 'category_underwear')
async def process_callback_shoes(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬 Выберите подходящий раздел:", reply_markup=underwear_kb)
@router.callback_query(F.data == 'category_headwear')
async def process_callback_shoes(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬 Выберите подходящий раздел:", reply_markup=hats_kb)
@router.callback_query(F.data == 'category_socks')
async def process_callback_shoes(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬 Выберите подходящий раздел:", reply_markup=socks_kb)
@router.callback_query(F.data == 'category_bags')
async def process_callback_shoes(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬 Выберите подходящий раздел:", reply_markup=bags_kb)
@router.callback_query(F.data == 'category_accessories')
async def process_callback_shoes(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬 Выберите подходящий раздел:", reply_markup=accessory_kb)
@router.callback_query(F.data == 'category_cosmetics')
async def process_callback_shoes(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬 Выберите подходящий раздел:", reply_markup=cosmetics_kb)
@router.callback_query(F.data == 'category_electronics')
async def process_callback_shoes(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬 Выберите подходящий раздел:", reply_markup=electronics_kb)
@router.callback_query(F.data == 'category_sport')
async def process_callback_shoes(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬 Выберите подходящий раздел:", reply_markup=sport_kb)
@router.callback_query(F.data == 'category_figures')
async def process_callback_shoes(call: CallbackQuery, state: FSMContext):
    await call.message.answer("💬 Выберите подходящий раздел:", reply_markup=figures_kb)

@router.callback_query(F.data.in_([
    'sneakers', 'boots', 'kedi', 'flip-flops', 'sandals', 'football_boots', 'shoes',
    'downjacket', 'vest', 'parka', 'lightjacket', 'windbreaker', 'blazer', 'hoodie', 'longslive', 'shirts', 'top',
    'jeans', 'pants', 'shorts',
    'underwearMen', 'underwearWomen', 'completeUnderwear',
    'hat', 'kepka', 'snud', 'warm_scarf', 'light_scarf',
    '1pair', '2pairs', '3pairs',
    'woman_small_bag', 'woman_big_bag', 'bag', 'suitcase', 'roadbag', 'bag_shoulder', 'bananka',
    'glasses', 'nails', 'jewelry', 'belts', 'gloves',
    'perfume', 'cream', 'lipstick', 'other',
    'laptop', 'phone', 'platforms', 'watches', 'tws_earbuds', 'wired_earbuds', 'keyboard', 'mouse', 'graphics_card', 'pc_case',
    'basketball_ball', 'football_ball', 'volleyball_ball', 'helmeet', 'other_sport',
    'bb100', 'bb400', 'bb1000',
    'category_back'
]))
async def process_product_item(call: CallbackQuery, state: FSMContext):
    callback_to_text = {
        'sneakers': 'Кроссовки', 'boots': 'Ботинки', 'kedi': 'Кеды', 'flip-flops': 'Шлепанцы', 'sandals': 'Сандали', 'football_boots': 'Бутсы', 'shoes': 'Туфли',
        'downjacket': 'Пуховик', 'vest': 'Жилетка', 'parka': 'Парка', 'lightjacket': 'Легкая куртка', 'windbreaker': 'Ветровка', 'blazer': 'Пиджак', 'hoodie': 'Худи / Толстовка', 'longslive': 'Лонгслив', 'shirts': 'Футболка / Рубашка', 'top': 'Топ',
        'jeans': 'Джинсы', 'pants': 'Брюки', 'shorts': 'Шорты',
        'underwearMen': 'Нижнее белье (муж)', 'underwearWomen': 'Нижнее белье (жен)', 'completeUnderwear': 'Комплект нижнего белья',
        'hat': 'Шапка', 'kepka': 'Кепка', 'snud': 'Снуд', 'warm_scarf': 'Теплый шарф', 'light_scarf': 'Легкий шарф',
        '1pair': '1 пара', '2pairs': '2 пары', '3pairs': '3 пары',
        'woman_small_bag': 'Женская сумка маленькая', 'woman_big_bag': 'Женская сумка большая', 'bag': 'Рюкзак', 'suitcase': 'Чемодан', 'roadbag': 'Дорожная сумка', 'bag_shoulder': 'Сумка через плечо', 'bananka': 'Бананка',
        'glasses': 'Очки', 'nails': 'Наши', 'jewelry': 'Украшения', 'belts': 'Ремни', 'gloves': 'Перчатки',
        'perfume': 'Парфюм', 'cream': 'Крем для лица/рук', 'lipstick': 'Помада', 'other': 'Прочие',
        'laptop': 'Ноутбук', 'phone': 'Телефон', 'platforms': 'Платформы', 'watches': 'Часы', 'tws_earbuds': 'Наушники TWS', 'wired_earbuds': 'Проводные наушники', 'keyboard': 'Клавиатура', 'mouse': 'Мышь', 'graphics_card': 'Видеокарта', 'pc_case': 'Системный блок',
        'basketball_ball': 'Баскетбольный мяч', 'football_ball': 'Футбольный мяч', 'volleyball_ball': 'Волейбольный мяч', 'helmeet': 'Шлем', 'other_sport': 'Другое',
        'bb100': 'Bearbrick 100%', 'bb400': 'Bearbrick 400%', 'bb1000': 'Bearbrick 1000%',
        'category_back': 'Назад'
    }
    
    item_name = callback_to_text.get(call.data, "Неизвестный товар")
    try:
        await call.message.answer_photo(
            photo=FSInputFile("./images/order_add.png"),
            caption=f'''
⚠️ Товар возврату и обмену не подлежит. Мы оказываем услуги только выкупа и доставки товаров.

🖼Пожалуйста, вставьте фото товара, как показано на примере:
Укажите детали заказа для выбранного товара: {item_name}
Пример: модель, размер, цвет, количество.'''
        )
        await state.set_state(Order.photo)
    except FileNotFoundError:
        await call.message.answer("Ошибка: изображение не найдено. Пожалуйста, проверьте путь к файлу.")
    await call.answer()
async def download_photo(bot: Bot, file_id, order_id):
    try:
        file = await bot.get_file(file_id)
        file_path = file.file_path
        downloaded_file = await bot.download_file(file_path)
        
        os.makedirs("order_photos", exist_ok=True)
        
        photo_path = f"order_photos/order_{order_id}.jpg"
        with open(photo_path, 'wb') as photo_file:
            photo_file.write(downloaded_file.read())
        return photo_path
    except Exception as e:
        print(f"Error downloading photo: {e}")
        return None

@router.message(Order.photo)
async def process_photo(message: Message, state: FSMContext):
    try:
        if not message.photo:
            raise ValueError("Пожалуйста, отправьте фотографию товара.")
        

        photo_file_id = message.photo[-1].file_id
        
        data = await state.get_data()
        order_id = data.get('order_id', random.randint(100000, 999999))
        
        bot = Bot(token=config.BOT_TOKEN)
        photo_path = await download_photo(bot, photo_file_id, order_id)
        if not photo_path:
            raise Exception("Не удалось сохранить фото.")


        await state.update_data(photo_path=photo_path)
        await state.set_state(Order.delivery)
        await message.answer("""📦 Укажите способ доставки:
🚚 Авто ~25 дней (с момента отправки)

⚠️ Товар возврату и обмену не подлежит. Мы оказываем услуги только выкупа и доставки товаров.""",
    reply_markup=deliveries_kb)

    except ValueError as e:
        await message.answer(str(e))
    except Exception as e:
        await message.answer(f"Произошла ошибка при сохранении фото: {e}")


@router.message(Order.delivery)
@router.callback_query(F.data == "autodelivery")
async def process_delivery(call: CallbackQuery, state: FSMContext):
    await state.update_data(delivery=call.message.text)
    await state.set_state(Order.link)
    photo = FSInputFile("./images/12.png")
    await call.message.answer_photo(
        photo=photo,
        caption='''⚠️ Товар возврату и обмену не подлежит. Мы оказываем услуги только выкупа и доставки товаров.

🔗Пожалуйста, отправьте ссылку на товар в нужном формате https://dw4.co/t/A/18KfFHsf:'''
        )


@router.message(Order.link)
async def process_link(message: Message, state: FSMContext):
    await state.update_data(link=message.text)
    try:
        await state.set_state(Order.size)
    except FileNotFoundError:
        await message.answer("Ошибка: изображение не найдено. Пожалуйста, проверьте путь к файлу.")
    photo = FSInputFile("./images/13.png")
    await message.answer_photo(
        photo=photo,
        caption='''⚠️ Товар возврату и обмену не подлежит. Мы оказываем услуги только выкупа и доставки товаров.

📏Пожалуйста, напишите размер товара (актуально для одежды и обуви). Например 42''', reply_markup=skip_kb
        )

@router.message(Order.size)
@router.message(F.text == "Пропустить")
async def process_size(message: Message, state: FSMContext):
    size = message.text if message.text != "Пропустить" else None
    await state.update_data(size=size)
    try:
        photo = FSInputFile("./images/14.png")
        await message.answer_photo(
            photo=photo,
            caption='''⚠️ Введите стоимость выбранной вещи В ЮАНЯХ.

⚠️ Товар возврату и обмену не подлежит. Мы оказываем услуги только выкупа и доставки товаров.

⛔️⛔️ Если Вы рассчитали или оплатили неверную сумму или заказали по ≈, то будет сделан возврат средств в течении 10 рабочих дней БЕЗ возможности доплаты! ⛔️⛔️'''
        )
        await state.set_state(Order.cost_uan)
    except FileNotFoundError:
        await message.answer("Ошибка: изображение не найдено. Пожалуйста, проверьте путь к файлу.")
    

@router.message(Order.cost_uan)
async def process_cost_uan(message: Message, state: FSMContext):
    await state.update_data(cost_uan=message.text)
    await state.set_state(Order.get_order)
    
    data = await state.get_data()
    required_fields = ['photo_path', 'delivery', 'link', 'cost_uan']
    if not all(field in data and data[field] for field in required_fields):
        await message.answer("❌ Не все обязательные поля заполнены. Проверьте данные.")
        return
    
    cost_uan = data['cost_uan']
    price_rub = convert_uan_to_rub(cost_uan)
    price_usdt = convert_uan_to_usdt(cost_uan)
    
    try:
        photo = FSInputFile("./images/1.png")
        await message.answer_photo(
            photo=photo,
            caption=f'''Ссылка на товар: {data['link']}
Размер товара: {data.get('size', 'Не указан')}
Стоимость в ЮАНЯХ: {cost_uan}
Стоимость в РУБЛЯХ: {price_rub:.2f}
Стоимость в USDT: {price_usdt:.2f}

❕Проверьте данные перед подтверждением. После оформления изменить заказ нельзя.

🚚 Доставка СДЭК по России оплачивается ОТДЕЛЬНО! Отправки идут из Москвы.

⚠️ Товар возврату и обмену не подлежит. Мы оказываем услуги только выкупа и доставки товаров.''',
            reply_markup=order_confirmation_kb
        )
    except FileNotFoundError:
        await message.answer("Ошибка: изображение не найдено. Проверьте путь к файлу.")


@router.callback_query(F.data == 'confirm_order_final')
async def confirm_order(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = call.from_user.id
    username = call.from_user.username or call.from_user.first_name
    order_id = data.get('order_id', random.randint(100000, 999999))


    order_data = {
        'order_id': order_id,
        'photo_path': data.get('photo_path', ''),
        'delivery': data.get('delivery', 'Авто'),
        'link': data.get('link', ''),
        'size': data.get('size', 'Не указан'),
        'cost_uan': data.get('cost_uan', '0'),
        'price_rub': convert_uan_to_rub(data.get('cost_uan', '0')),
        'price_usdt': convert_uan_to_usdt(data.get('cost_uan', '0'))
    }

    try:
        
        with DB("justbox.db") as db_instance:
            db_instance.add_order(user_id, order_data)
            db_instance.execute("UPDATE users SET orders = orders + 1 WHERE telegram_id = ?", (user_id,))
            db_instance.commit()


        order_details = f"📦 Новый заказ от {call.from_user.full_name} (<a href='tg://user?id={user_id}'>{username}</a>)\n\n"
        order_details += f"🔗 Ссылка: {order_data['link']}\n"
        order_details += f"📏 Размер: {order_data['size']}\n"
        order_details += f"💰 Стоимость: {order_data['cost_uan']} ЮАН / {order_data['price_rub']:.2f} RUB / {order_data['price_usdt']:.2f} USDT\n"
        try:
                photo = FSInputFile(order_data['photo_path'])
                await call.bot.send_photo(chat_id=1141474614, photo=photo, caption=order_details, parse_mode="HTML")
        except Exception as e:
                await call.bot.send_message(6567758362, f"Ошибка при отправке фото: {e}\n{order_details}", parse_mode="HTML")
        await call.message.answer("✅ Ваш заказ оформлен и отправлен в обработку. Ожидайте подтверждения.", reply_markup=start_keyboard)
        await state.clear()
    except sqlite3.Error as e:
        await call.message.answer(f"Ошибка при сохранении заказа: {e}")
    await call.answer()




@router.callback_query(F.data == "edit_order")
async def edit_order(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(Order.photo) 
    await call.message.answer("🔄 Давайте начнем заново. Пожалуйста, отправьте фото товара.")



def convert_uan_to_rub(uan: str) -> float:
    try:
        uan_float = float(uan.replace(',', '.'))
        return uan_float * uan_to_rub
    except ValueError:
        return 0.0

def convert_uan_to_usdt(uan: str) -> float:
    try:
        uan_float = float(uan.replace(',', '.'))
        return uan_float * uan_to_usd  # 1 CNY ≈ 0.14 USDT
    except ValueError:
        return 0.0