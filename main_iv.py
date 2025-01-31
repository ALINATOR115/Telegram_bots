import telebot
from telebot import types

# Ваш токен и ссылка на фотографию
token = '6229861165:AAH6sih9Dop2ppT4cqbqdaEeFZ9ELmLED8A'
bot = telebot.TeleBot(token)
sent_photos = {}
sent_media = {}
user_states = {}
@bot.message_handler(commands=['start','menu'])
def menu(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('👉Как пользоваться Poizon👈', callback_data='how_to_use'))
    markup.add(types.InlineKeyboardButton('Рассчитать стоимость 📲', callback_data='categories'))
    markup.add(types.InlineKeyboardButton('Актуальный курс📈', callback_data='current_rate'))
    markup.add(types.InlineKeyboardButton('Ответы на вопросы ⁉️', callback_data='answers'))
    markup.add(types.InlineKeyboardButton('Комиссия сервиса 💵', callback_data='program'))
    markup.add(types.InlineKeyboardButton('👍Отзывы', url='https://t.me/otzavPoizonBrothers'))
    markup.add(types.InlineKeyboardButton('Оформить заказ👤',url='https://t.me/Hastkalove'))
    p1 = open('painting/brother.jpg','rb')
    bot.send_photo(message.chat.id,photo=p1, caption=f'<b>Привет, {message.from_user.first_name}!</b>\n\nДанный бот создан, чтобы устроить более качественное взаимодействие между вами и Poizon.\n\nЕсли вы готовы оформить заказ и уже знаете как и что у нас происходит - можете сразу писать сюда👉@Hastkalove\n\nЧто будем делать?',
                   parse_mode='html',reply_markup=markup)
    sent_photos[message.chat.id] = p1
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'how_to_use':
        handle_how_to_use(call)

    elif call.data == 'categories':
        handle_categories(call)
    elif call.data == 'no_categories':
        handle_no_categories(call)
    elif call.data == 'back_to_categories':
        handle_categories(call)
    elif call.data == 'shoes':
        handle_shoes(call)
    elif call.data == 'socks':
        handle_socks(call)
    elif call.data == 'laptop':
        handle_laptop(call)

    elif call.data == 'current_rate':
        handle_current_rate(call)

    elif call.data == 'answers':
        handle_answers(call)
    elif call.data == 'program':
        handle_program(call)

    elif call.data == 'what_poizon':
        handle_what(call)
    elif call.data == 'what_of_delivery':
        handle_what_of_delivery(call)
    elif call.data == 'why_of_us':
        handle_why_of_us(call)
    elif call.data == 'pay_upon_receipt':
        handle_pay_upon_receipt(call)
    elif call.data == 'size_not_fit':
        handle_size_not_fit(call)
    elif call.data == 'many_things':
        handle_many_things(call)

    elif call.data == 'registration_instructions':
        handle_registration_instructions(call)

    elif call.data == 'how_pick_size':
        handle_how_pick_size(call)

    elif call.data == 'meaning_of_the_buttons':
        handle_meaning_of_the_buttons(call)

    elif call.data == 'qr_code':
        handle_qr_code(call)

    elif call.data == 'hight_cours':
        handle_hight_cours(call)

    elif call.data == 'back_to_cours':
        handle_current_rate(call)

    elif call.data == 'back_to_question':
        handle_answers(call)

    elif call.data == 'back_to_how_to_use':
        handle_how_to_use(call)

    elif call.data == 'back_to_menu':
        menu(call.message)
@bot.callback_query_handler(func=lambda call: call.data == 'how_to_use')
def handle_how_to_use(call):
    chat_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Ссылка для скачивания | iOS', url='https://apps.apple.com/ru/app/得物-有毒的运动-潮流-好物/id1012871328')
    button2 = types.InlineKeyboardButton('Ссылка для скачивания | Android', url='https://m.anxinapk.com/rj/12201303.html')
    button3 = types.InlineKeyboardButton('Регистрация в приложении', callback_data='registration_instructions')
    button4 = types.InlineKeyboardButton('Как выбрать размер', callback_data='how_pick_size')
    button5 = types.InlineKeyboardButton('Обозначения кнопок',callback_data='meaning_of_the_buttons')
    button6 = types.InlineKeyboardButton('Проверка QR-кода', callback_data='qr_code')
    button7 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_menu')
    markup.add(button1),markup.add(button2),markup.add(button3),markup.add(button4),markup.add(button5),markup.add(button6),markup.add(button7)
        # Если фото не отправлено, отправьте фото и обновите словарь
    p1 = open('painting/how_to_use1.jpg', 'rb')
    bot.send_photo(chat_id, photo=p1,caption='В данном меню собраны все инструкции по использованию маркетплейса — Poizon.\n\n Выберите интересующий вас пункт ⤵️',reply_markup=markup)
    sent_photos[chat_id] = p1

@bot.callback_query_handler(func=lambda call: call.data == 'categories')
def handle_categories(call):
    chat_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Кроссовки  \ Кеды 👟', callback_data='shoes')
    button2 = types.InlineKeyboardButton('Зимняя обувь 👞 \ Ботинки 👟 \ Куртки❄️', callback_data='shoes')
    button3 = types.InlineKeyboardButton('Футболки 👕 \ Рубашки 👔 \ Шорты 🩳', callback_data='socks')
    button4 = types.InlineKeyboardButton('Носки 🧦 \ Кепки 🧢 \ Дешёвые аксессуары 👓', callback_data='socks')
    button5 = types.InlineKeyboardButton('Электроника 💻 \ Бытовая техника📺', callback_data='laptop')
    button6 = types.InlineKeyboardButton('Нет нужной категории?', callback_data='no_categories')
    button7 = types.InlineKeyboardButton('Оформить заказ👤',url='https://t.me/LiteScore')
    button8 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_menu')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)
    markup.add(button6)
    markup.add(button7)
    markup.add(button8)
    bot.send_message(chat_id,'<b>Выберите категорию товара:</b>',parse_mode='html',reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'no_categories')
def handle_no_categories(call):
    chat_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_categories')
    markup.add(button1)
    bot.send_message(chat_id,'<b>Друзья, в связи с тем, что некоторые категории товаров имеют слишком разнообразный выбор, просчитать их точную стоимость не является возможным,</b>так как одним из самых главных факторов при расчетах является — доставка...\n\nДоставка при перевозках из Китая в Россию высчитывается исключительно через объемный вес и килограммы.\n\nЕсли Вашей категории в списке для расчета нет, то напишите, пожалуйста, нашему менеджеру и он с удовольствием поможет рассчитать Ваш заказ 😊\n\n<b>👨‍💻Менеджер:</b>@Hastkalove',
                     parse_mode='html',reply_markup=markup)


# Добавьте глобальную переменную для отслеживания активной категории
active_category = None

@bot.callback_query_handler(func=lambda call: call.data == 'shoes')
def handle_shoes(call):
    chat_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    p12 = open('painting/secondbuttons1.jpg', 'rb')
    button1 = types.InlineKeyboardButton('Подробнее про цветные кнопки🟩⬛️', callback_data='meaning_of_the_buttons')
    button2 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_menu')
    markup.add(button1)
    markup.add(button2)
    bot.send_photo(chat_id, photo=p12, caption='• <b>По бирюзовой кнопке - выкупаем</b>\n\n<b>• По черной кнопке - выкупаем</b>\n\n<b>• По серой кнопке с числом 95 - выкупаем</b>\n\n<b>• По кнопке с волнистой ≈ линией - не выкупаем</b>\n\n❗️<b>Если у кнопки есть зачеркнутая цена, то при расчёте нужно указывать именно её, так как в 90% случаев это скидка на первый заказ. У нашего аккаунта этой скидки не будет.</b>\n\nА если всё же скидка относится к другой акции и она у нас применится, то мы компенсируем разницу. После каждого выкупа — мы присылаем чек, где видно итоговую стоимость.', parse_mode='html')
    bot.send_message(chat_id, '<b>💸Введите стоимость товара в юанях:</b>',
                     parse_mode='html',reply_markup=markup)
    sent_photos[chat_id] = p12
    # Установите активную категорию
    global active_category
    active_category = 'shoes'

@bot.callback_query_handler(func=lambda call: call.data == 'socks')
def handle_socks(call):
    chat_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    p = open('painting/tshirts1.jpg', 'rb')
    button1 = types.InlineKeyboardButton('Подробнее про цветные кнопки🟩⬛️', callback_data='meaning_of_the_buttons')
    button2 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_menu')
    markup.add(button1)
    markup.add(button2)
    bot.send_photo(chat_id, photo=p, caption='• <b>По бирюзовой кнопке - выкупаем</b>\n\n<b>• По черной кнопке - выкупаем</b>\n\n<b>• По серой кнопке с числом 95 - выкупаем</b>\n\n<b>• По кнопке с волнистой ≈ линией - не выкупаем</b>\n\n❗️<b>Если у кнопки есть зачеркнутая цена, то при расчёте нужно указывать именно её, так как в 90% случаев это скидка на первый заказ. У нашего аккаунта этой скидки не будет.</b>\n\nА если всё же скидка относится к другой акции и она у нас применится, то мы компенсируем разницу. После каждого выкупа — мы присылаем чек, где видно итоговую стоимость.', parse_mode='html')
    bot.send_message(chat_id, '<b>💸Введите стоимость товара в юанях:</b>',
                     parse_mode='html', reply_markup=markup)
    sent_photos[chat_id] = p

    # Установите активную категорию
    global active_category
    active_category = 'socks'

@bot.callback_query_handler(func=lambda call: call.data == 'laptop')
def handle_laptop(call):
    chat_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    p = open('painting/laptop1.jpg', 'rb')
    button1 = types.InlineKeyboardButton('Подробнее про цветные кнопки🟩⬛️', callback_data='meaning_of_the_buttons')
    button2 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_menu')
    markup.add(button1)
    markup.add(button2)
    bot.send_photo(chat_id, photo=p, caption='• <b>По бирюзовой кнопке - выкупаем</b>\n\n<b>• По черной кнопке - выкупаем</b>\n\n<b>• По серой кнопке с числом 95 - выкупаем</b>\n\n<b>• По кнопке с волнистой ≈ линией - не выкупаем</b>\n\n❗<b>Если у кнопки есть зачеркнутая цена, то при расчёте нужно указывать именно её, так как в 90% случаев это скидка на первый заказ. У нашего аккаунта этой скидки не будет.</b>\n\nА если всё же скидка относится к другой акции и она у нас применится, то мы компенсируем разницу. После каждого выкупа — мы присылаем чек, где видно итоговую стоимость.', parse_mode='html')
    bot.send_message(chat_id, '<b>💸Введите стоимость товара в юанях:</b>',
                     parse_mode='html',reply_markup=markup)
    sent_photos[chat_id] = p

    # Установите активную категорию
    global active_category
    active_category = 'laptop'



@bot.message_handler(func=lambda message: message.text.isdigit() and active_category == 'shoes', content_types=['text'])
def calculate_shoes_price(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Оформить заказ👤', url='https://t.me/Hastkalove'))
    markup.add(types.InlineKeyboardButton('Рассчитать ещё раз⏳', callback_data='shoes'))
    markup.add(types.InlineKeyboardButton('Вернуться в главное меню↩️', callback_data='back_to_menu'))
    price = float(message.text)
    total_price = 14 * price
    bot.send_message(chat_id, f'<b>Итоговый расчет ⤵️</b>\n\n<b>💹 Курс ¥: 14</b>\n\nСтоимость вещи: {round(total_price,1)} ₽\nСтраховка груза: бесплатно\nДоставка до России: 630 ₽ за кг\nКомиссия сервиса: 500₽\n\n<b>💵 Итог: {round(total_price,1) + 500} + доставка(для уточнения обращаться к менеджеру).</b>\n\n<b>❗️Итоговая стоимость указана без учета доставки. Доставка по России рассчитывается по тарифам почтовых служб и оплачивается при получении.</b>\n\n<b>Стоимость доставки до РФ:</b> 630 руб. за кг (оплачивается при взвешивании товара на складе).\n\n<b>Стоимость доставки по РФ:</b> от 300 до 800 руб., цена может меняться в зависимости от веса и объёма товара.\n\n<b>Средние сроки доставки с Китая до Мск, используя Boxberry ≈ 17 дней.</b>', parse_mode='html')
    bot.send_message(chat_id, '<b>Готовы оформить заказ или остались вопросы?</b>\n\n👨‍💻 <b>Наши менеджеры:@Hastkalove, @richvak</b>\n\n<b>Чтобы оформить заказ, нам нужно:</b>\n\n1)Скриншот товара\n2)Ссылка (по возможности)\n3)Размер\n4)ФИО\n5)Город получателя\n6)Адрес проживания и индекс почты (для таможенных служб)\n7)Номер телефона\n8) Ближайший адрес отделения Boxberry или Почта РФ\n\n<b>‼️ ОБРАТИТЕ ВНИМАНИЕ ‼️</b>\n\nВсе заказы осуществляются только через один аккаунт, который указан выше ☝️\n\n<b>Других аккаунтов у нас нет!</b>', parse_mode='html', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.isdigit() and active_category == 'socks', content_types=['text'])
def calculate_socks_price(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Оформить заказ👤', url='https://t.me/Hastkalove'))
    markup.add(types.InlineKeyboardButton('Рассчитать ещё раз⏳', callback_data='socks'))
    markup.add(types.InlineKeyboardButton('Вернуться в главное меню↩️', callback_data='back_to_menu'))
    price = float(message.text)
    total_price = 14 * price
    bot.send_message(chat_id, f'<b>Итоговый расчет ⤵️</b>\n\n<b>💹 Курс ¥: 14</b>\n\nСтоимость вещи: {round(total_price,1)} ₽\nСтраховка груза: бесплатно\nДоставка до России: 630 ₽ за кг\nКомиссия сервиса: 400₽\n\n<b>💵 Итог: {round(total_price,1) + 400} + доставка (для уточнения обращаться к менеджеру).</b>\n\n<b>❗️Итоговая стоимость указана без учета доставки. Доставка по России рассчитывается по тарифам почтовых служб и оплачивается при получении.</b>\n\n<b>Стоимость доставки до РФ:</b> 630 руб. за кг (оплачивается при взвешивании товара на складе).\n\n<b>Стоимость доставки по РФ:</b> от 300 до 800 руб., цена может меняться в зависимости от веса и объема товара.\n\n<b>Средние сроки доставки с Китая до Мск, используя Boxberry ≈ 17 дней.</b>', parse_mode='html')
    bot.send_message(chat_id, '<b>Готовы оформить заказ или остались вопросы?</b>\n\n👨‍💻 <b>Наши менеджеры:@Hastkalove, @richvak</b>\n\n<b>Чтобы оформить заказ, нам нужно:</b>\n\n1)Скриншот товара\n2)Ссылка (по возможности)\n3)Размер\n4)ФИО\n5)Город получателя\n6)Адрес проживания и индекс почты (для таможенных служб)\n7)Номер телефона\n8) Ближайший адрес отделения Boxberry или Почта РФ\n\n<b>‼️ ОБРАТИТЕ ВНИМАНИЕ ‼️</b>\n\nВсе заказы осуществляются только через один аккаунт, который указан выше ☝️\n\n<b>Других аккаунтов у нас нет!</b>', parse_mode='html', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.isdigit() and active_category == 'laptop', content_types=['text'])
def calculate_laptop_price(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Оформить заказ👤', url='https://t.me/Hastkalove'))
    markup.add(types.InlineKeyboardButton('Рассчитать ещё раз⏳', callback_data='laptop'))
    markup.add(types.InlineKeyboardButton('Вернуться в главное меню↩️', callback_data='back_to_menu'))
    price = float(message.text)
    total_price = 14 * price
    bot.send_message(chat_id, f'<b>Итоговый расчет ⤵️</b>\n\n<b>💹 Курс ¥: 14</b>\n\nСтоимость вещи: {round(total_price,1)} ₽\nСтраховка груза: бесплатно\nДоставка до России: 630 ₽ за кг\nКомиссия сервиса: 900₽(зависит от товара)\n\n<b>💵 Итог: {round(total_price,1) + 900} + доставка (для уточнения обращаться к менеджеру).</b>\n\n<b>❗️Итоговая стоимость указана без учета доставки. Доставка по России рассчитывается по тарифам почтовых служб и оплачивается при получении.</b>\n\n<b>Стоимость доставки до РФ:</b> 630 руб. за кг (оплачивается при взвешивании товара на складе).\n\n<b>Стоимость доставки по РФ:</b> от 300 до 800 руб., цена может меняться в зависимости от веса и объема товара.\n\n<b>Средние сроки доставки с Китая до Мск, используя Boxberry ≈ 17 дней.</b>\n\n<b>❗️Также есть возможность обезопасить ваш товар деревянными вставками</b>', parse_mode='html')
    bot.send_message(chat_id, '<b>Готовы оформить заказ или остались вопросы?</b>\n\n👨‍💻 <b>Наши менеджеры:@Hastkalove, @richvak</b>\n\n<b>Чтобы оформить заказ, нам нужно:</b>\n\n1)Скриншот товара\n2)Ссылка (по возможности)\n3)Размер\n4)ФИО\n5)Город получателя\n6)Адрес проживания и индекс почты (для таможенных служб)\n7)Номер телефона\n8) Ближайший адрес отделения Boxberry или Почта РФ\n\n<b>‼️ ОБРАТИТЕ ВНИМАНИЕ ‼️</b>\n\nВсе заказы осуществляются только через один аккаунт, который указан выше ☝️\n\n<b>Других аккаунтов у нас нет!</b>', parse_mode='html', reply_markup=markup)


@bot.message_handler(func=lambda message: not message.text.isdigit(), content_types=['text'])
def handle_invalid_input(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Некорректный ввод. Введите цену в юанях (число).')

# Другие обработчики сообщений

# Убедитесь, что активная категория сбрасывается при выходе из нее или при переходе в другую категорию.
@bot.callback_query_handler(func=lambda call: call.data == 'back_to_menu')
def handle_back_to_menu(call):
    global active_category
    active_category = None
    # Ваш код для обработки возвращения в главное меню








def handle_current_rate(call):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Почему курс выше ЦБ?🤬', callback_data='hight_cours')
    button2 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_menu')
    markup.add(button1)
    markup.add(button2)
    bot.send_message(call.message.chat.id, '<b>📈 Курс на сегодня:</b>\n\n<b>1¥ = 14₽</b>', parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'answers')
def handle_answers(call):
    chat_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Что за Poizon?', callback_data='what_poizon')
    button2 = types.InlineKeyboardButton('Какие сроки доставки?', callback_data='what_of_delivery')
    button3 = types.InlineKeyboardButton('Почему нам можно доверять?', callback_data='why_of_us')
    button4 = types.InlineKeyboardButton('Можно ли оплатить при получении?', callback_data='pay_upon_receipt')
    button5 = types.InlineKeyboardButton('Что делать, если не подошёл размер?', callback_data='size_not_fit')
    button6 = types.InlineKeyboardButton('Как рассчитать стоимость доставки?', callback_data='many_things')
    button7 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_menu')
    markup.add(button1),markup.add(button2),markup.add(button3),markup.add(button4),markup.add(button5),markup.add(button6),markup.add(button7)
    p6 = open('painting/faq1.png','rb')
    bot.send_photo(chat_id, photo=p6, caption="В данном меню собраны ответы на самые популярные вопросы\n\nВ дальнейшем, по мере поступления интересных вопросов — список будет пополняться.\n\nВыберите интересующий Вас пункт ⤵️", reply_markup=markup)
    sent_photos[chat_id] = p6
@bot.callback_query_handler(func=lambda call: call.data == 'program')
def handle_program(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Оформить заказ👤', url='https://t.me/Hastkalove'))
    markup.add(types.InlineKeyboardButton('Назад↩️', callback_data='back_to_menu'))
    bot.send_message(call.message.chat.id, '<b>💰Наша КОМИССИЯ и КУРС</b>💰\n\n⚫️<b>Комиссия</b> на каждый товар <b>500 рублей,</b> при заказе 5 и более товаров <b>400 рублей</b>\n\n⚫️<b>Комиссия</b> на  носки, кепки, дешевые аксессуары <b>350 рублей,</b> при заказе 5 и более товаров <b>300</b> рублей\n\n⚫️<b>Комиссия</b> на технику <b>900 рублей</b>\n\n❌<b>Промики не суммируются</b> с ценами на 5 и более товаров\n❌<b>5 и более </b>действует только на один тип товаров\n\n<b>💹Курс Юаня</b> ¥ = 14₽ (при изменение оповещаем)', parse_mode='html',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'what_poizon')
def handle_what(call):
    chat_id = call.message.chat.id
    # Здесь добавьте логику для инструкций по регистрации
    # Например, отправка инструкций по регистрации
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Какие сроки доставки?',callback_data='what_of_delivery')
    button2 = types.InlineKeyboardButton('Назад↩️',callback_data='back_to_question')
    markup.add(button1)
    markup.add(button2)
    p7 = open('painting/what_of_poizon1.jpg','rb')
    p14 = open('painting/16prover1.png','rb')
    bot.send_photo(chat_id,photo=p7)
    bot.send_message(chat_id,
                     '<b>Немного теории, что такое Poizon и почему там такие цены?</b>\n\nPoizon появился в 2015 году как онлайн-сообщество коллекционеров кроссовок и ценителей уличной моды. В 2022 году он развился до полноценного маркетплейса брендовых и дизайнерских вещей с оценкой <b>10 млрд. долларов</b>.\n\n<b>У Poizon своя логистика, база продавцов и система проверки подлинности товара.</b> Ориентированный на молодую аудиторию, маркетплейс «живёт» только в смартфоне. Аудитория площадки насчитывает свыше 100 млн пользователей, из которых 1,5 млн пользуются приложением ежемесячно.\n\nБлагодаря тому, что многие производства западных брендов расположены в Китае — такие бренды как: Nike, Jordan, New Balance, Adidas, Vans, Reebok, Puma, Bape, Stone Island, The North Face и другие можно найти <b>вполовину дешевле, чем в России и Европе.</b>\n\nОдно из ключевых преимуществ Poizon — <b>многоэтапная система верификации.</b> Перед отправкой, специалисты Poizon в своей лаборатории проверяют вещи на <b>подлинность. Например, кроссовки оценивают по 16 параметрам:</b> осматривают их полностью, включая подошву, ярлычок, стельку и коробку.(ниже показаны все проверки👇🏼)\n\n<b>Но если там такие низкие цены, то почему почти никто в России все еще не знает об этом маркетплейсе?</b> 🤔\n\nВсе очень просто! <b>Poizon создан исключительно для внутреннего рынка Китая</b>, то бишь ни в какой другой город или страну вне Китая — напрямую отправить вещь Вы не сможете. Чтобы заказать что-либо оттуда — Вам нужен <b>посредник</b>, который с помощью китайской карты оплатит вещь, отправит ее в транспортную компанию и оттуда она уже отправится в Россию. Это довольно сложная цепочка действий, особенно если учитывать то, что почти никакая транспортная в Китае штучно вещи не отправляет и нужно собирать вместе сразу 5-10 заказов и только потом их отправлять.',
                     parse_mode='html',reply_markup=markup)
    bot.send_photo(chat_id,photo=p14)
    sent_photos[chat_id]=p7
    sent_photos[chat_id]=p14
@bot.callback_query_handler(func=lambda call: call.data == 'what_of_delivery')
def handle_what_of_delivery(call):
    chat_id = call.message.chat.id
    # Здесь добавьте логику для инструкций по регистрации
    # Например, отправка инструкций по регистрации
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Почему нам можно доверять?', callback_data='why_of_us' )
    button2 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_question')
    markup.add(button1)
    markup.add(button2)
    p8 = open('painting/delivery1.jpg','rb')
    bot.send_photo(chat_id,photo=p8)
    bot.send_message(call.message.chat.id,'<b>У многих в голове все еще есть ассоциация с тем, что логистика с Китая в Россию занимает несколько месяцев...</b>\n\nНа самом же деле, это уже давно не так и сейчас уже все работает намного проще и быстрее.\n\n<b>🚚 Логистика из Китая делится на 4 этапа:</b>\n\n<b>1) Выкуп товара с Poizon</b>Данный процесс в среднем занимает <b>15 минут</b>, в зависимости от нашей загруженности.\n\n<b>2) Доставка с Poizon до склада в Китае</b>\n\nВ среднем, сроки доставки по Китаю занимают <b>от 2 до 4 дней</b>, если   выкупать товар по бирюзовой кнопке.\n\nЕсли же выкупаем по черной кнопке, либо с волнистыми линиями, то доставка в среднем занимает <b>от 4 до 6 дней</b>(Точный срок доставки написан на кнопках в приложении).\n\n<b>3) Доставка с Китая до России</b>\n\nВсе выкупленные позиции направляются из Китая напрямую в Уссурийск, где расположен наш склад.\n\nСредние сроки доставки со склада в Китае до России занимают <b>+-5 дней, если нет проблем с таможкой</b>\n\n<b>4) Доставка по России</b>\n\nПосле того, как товар приехал к нам на склад - мы должны его отправить нашим клиентам.\n\nДоставка из Уссурийска до вашего города зависит от данных почтовых служб: <b>Boxberry,Почта РФ</b>\n\n📎 <b>Итог:</b>\n\nВ среднем доставка до Мск используя Boxberry занимает <b>17 дней</b>, доставка до регионов <b>+-23 дня</b>\n\n',
                     parse_mode='html', reply_markup=markup)
    sent_photos[chat_id] = p8
@bot.callback_query_handler(func=lambda call: call.data == 'registration_instructions')
def handle_registration_instructions(call):
    chat_id = call.message.chat.id
    # Здесь добавьте логику для инструкций по регистрации
    # Например, отправка инструкций по регистрации
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_how_to_use')
    markup.add(button1)
    p1 = open('painting/registr11.png', 'rb')
    p2 = open('painting/registr21.png', 'rb')
    bot.send_photo(chat_id, photo=p1,
                   caption='<b>Регистрация на Poizon</b>\n\n📎 <b>Что она дает:</b>\n\n- Возможность просматривать цены за размер\n- Копировать ссылки на товар\n- Искать вещи по фото\n\nПодробная инструкция по регистрации на фото снизу ⤵️️\n\n📎 <b>Если не приходит код, то:</b>\n1) Посмотрите свой ватсап, возможно код пришел туда.\n2) Нажмите на кнопку «отправить код заново».\n3) Запрашивайте код с интервалом 10-20 минут.\n4) Попробуйте запросить его с выключенным ВПН.\n\nЕсли все же код не хочет приходить, то ничего страшного, ведь поиск вещей доступен всегда, а узнать цены и все посчитать — наш менеджер @Hastkalove всегда поможет 🤝',
                   parse_mode='html',reply_markup=markup)
    bot.send_photo(chat_id,photo=p2)
    sent_photos[chat_id] = p1
    sent_photos[chat_id] = p2
@bot.callback_query_handler(func=lambda call: call.data == 'how_pick_size')
def handle_how_pick_size(call):
    chat_id = call.message.chat.id
    # Здесь добавьте логику для инструкций по регистрации
    # Например, отправка инструкций по регистрации
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_how_to_use')
    markup.add(button1)
    p2 = open('painting/size1.jpg', 'rb')
    bot.send_photo(chat_id, photo=p2,
                   caption='️<b>Подбираем нужный размер</b>\n\nС размерами все не так очевидно, как может показаться, так как большинство моделей из наличия производятся под китайский рынок и могут маломерить.\n\nНа картинке показали, как выбрать размер, чтобы избежать дискомфорта ⤴️',
                   parse_mode='html',reply_markup=markup)
    sent_photos[chat_id] = p2



@bot.callback_query_handler(func=lambda call: call.data == 'meaning_of_the_buttons')
def handle_meaning_of_the_buttons(call):
    chat_id = call.message.chat.id
    # Здесь добавьте логику для инструкций по регистрации
    # Например, отправка инструкций по регистрации
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_how_to_use')
    markup.add(button1)
    p3 = open('painting/buttons1.jpg', 'rb')
    bot.send_photo(chat_id, photo=p3,
                   caption='<b>ОБОЗНАЧЕНИЯ КНОПОК С ЦЕНАМИ</b>\n\n▫️<b>Бирюзовая кнопка:</b>\n\n- Товар в наличии на складе Poizon, полностью проверенный на оригинальность и готовый к отправке.\n\n▫️<b>Черная кнопка:</b>\n\n- Товар на складе продавца, есть шанс что может не пройти проверку на подлинность и заказ будет отменен.\n\n▫️<b>Кнопка с «≈» перед ценой:</b>\n\n Товар находится в другой стране, в основном в Европе и Японии. Доставка оттуда не осуществляется\n\n▫️<b>Серая кнопка с числом «95»</b>\n\n- Б/У товар. В 90% случаев он в идеальном состоянии.\nТакже у этих товаров есть оценки новизны:\n\nSS - абсолютно новые вещи(товары)\nS - один дефект, очень часто коробки испорчены.\nА - небольшие дефекты (желтая подошва, коробка + мелкое что-то).\nB - нормально (убитые вещи)\n\n',
                   parse_mode='html',reply_markup=markup)
    sent_photos[chat_id] = p3

@bot.callback_query_handler(func=lambda call: call.data == 'qr_code')
def handle_qr_code(call):
    chat_id = call.message.chat.id
    # Здесь добавьте логику для инструкций по регистрации
    # Например, отправка инструкций по регистрации
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_how_to_use')
    markup.add(button1)
    p4 = open('painting/rolegit1.png', 'rb')
    p13 = open('painting/qr31.png','rb')
    bot.send_photo(chat_id,photo=p4,
                   caption='<b>Как определить копию при заказе с Poizon?🤔</b>\n\nДа, друзья, и такое бывает, но…\n\nТакое может произойти только при выборе не проверенного посредника.\n\n📎 <b>Как это работает:</b>\n\n1) Вы нашли посредника с курсом ниже или как на мосбирже (такой курс априори невозможен) и минимальной комиссией (либо вообще без).\n\n2) Отправили ему ссылку на товар.\n\n3) Оплатили.\n\n4) Он сказал, что товар выкуплен и скоро отправится в Россию.\n\nВроде как ничего подозрительного, НО… Человек, который выступает посредником — запросто может вместо оригинальной вещи отправить копию с фейковыми QR-кодами. Большинство из Вас наверняка видели такие в магазинах с копиями\n\nЧтобы проверить оригинальность сертификата и пломбы - нужно отсканировать его в приложении Poizon(пример сертификата ниже👇🏼)\n\n❗️Подделать QR и сделать так, чтобы он выглядел как настоящий — нереально, так как при первом сканировании QR, система активирует его и записывает дату и время скана.',
                   parse_mode='html', reply_markup=markup)
    bot.send_photo(chat_id,photo=p13)

    sent_photos[chat_id] = p4
    sent_photos[chat_id] = p13


@bot.callback_query_handler(func=lambda call: call.data == 'hight_cours')
def handle_hight_cours(call):
    # Здесь добавьте логику для инструкций по регистрации
    # Например, отправка инструкций по регистрации
    chat_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_cours')
    markup.add(button1)
    p5 = open('painting/course1.jpg','rb')
    bot.send_photo(chat_id,photo=p5,
                   caption='<b>Почему курс не как у ЦБ РФ? 📈</b>\n\nДело в том, что из-за нелёгкой геополитической ситуации в мире — <b>рубль весьма нестабилен.</b> И в связи с этим, банки страхуются благодаря продаже валюты по завышенному курсу. \n\nМы делаем все возможное, чтобы удешевить курс, работаем с эксклюзивными контрагентами, но все же, <b>сделать его биржевым, чисто физически — невозможно 😢</b>',
                   parse_mode='html', reply_markup=markup)
    sent_photos[chat_id] = p5
@bot.callback_query_handler(func=lambda call: call.data == 'why_of_us')
def handle_why_of_us(call):
    # Здесь добавьте логику для инструкций по регистрации
    # Например, отправка инструкций по регистрации
    chat_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_question')
    markup.add(button1)
    p9 = open('painting/why_of_us1.png','rb')
    bot.send_photo(chat_id,photo=p9,
                   caption='<b>Почему нам можно доверять?</b>\n\n<b>1. Мы успешно привезли уже несколько сотен товаров с китайского маркетплейса Poizon,</b> что подтверждает наш опыт и надежность.\n\n<b>2. Мы гордимся довольными отзывами наших клиентов</b>, которые доверили нам свои покупки и остались довольны качеством обслуживания.\n\n<b>3. Наши поставки осуществляются официально, с прохождением таможенных процедур, и все товары застрахованы,</b> обеспечивая вам дополнительную защиту.\n\n<b>4. Мы предлагаем доставку в любой город России,</b> что делает наш сервис доступным для клиентов по всей стране.\n\n<b>5. Мы активно занимаемся доставкой уже почти год</b>, накопив важный опыт и надежность в сфере международных покупок. Доверьтесь нам и убедитесь в нашей надежности и ответственности.\n\n<b>Благодарим вас за выбор нашей компании!</b>❤️',
                   parse_mode='html', reply_markup=markup)
    sent_photos[chat_id] = p9
@bot.callback_query_handler(func=lambda call: call.data == 'pay_upon_receipt')
def handle_pay_upon_receipt(call):
    chat_id = call.message.chat.id
    # Здесь добавьте логику для инструкций по регистрации
    # Например, отправка инструкций по регистрации
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_question')
    markup.add(button1)
    p10 = open('painting/pay_upon_receipt1.jpg','rb')
    bot.send_photo(chat_id,photo=p10,
                   caption='<b>Можно ли оплатить заказ при получении?</b>\n\nДрузья, первым делом — нужно понять, что мы не магазин. <b>Мы — сервис, который помогает выкупать ту или иную вещь с китайской платформы.</b>\n\nЕсли бы мы были магазином и продавали товар из наличия, то мы могли бы без каких-либо проблем отправлять его с оплатой при получении и в случае отказа — просто принять его обратно и выставить на продажу...\n\nНо, будучи сервисом — мы себе этого позволить не можем. <b>Кто нам гарантирует, что при выкупе товара за наш счёт — клиент его потом оплатит?</b> И если всё таки так получилось, что заказ был выкуплен нами, но не был оплачен клиентом, то <b>что нам дальше делать с выкупленной вещью?</b>\n\n<b>Именно из-за этого, заказа с оплатой при получении — у нас нет.</b> А если вы нам не доверяете и боитесь, что мы вас можем обмануть, то просто посмотрите на отзывы и убедитесь в нашей честности.',
                   parse_mode='html',reply_markup=markup)
    sent_photos[chat_id] = p10
@bot.callback_query_handler(func=lambda call: call.data == 'size_not_fit')
def handle_size_not_fit(call):
    chat_id = call.message.chat.id
    # Здесь добавьте логику для инструкций по регистрации
    # Например, отправка инструкций по регистрации
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_question')
    markup.add(button1)
    p2 = open('painting/size1.jpg','rb')
    bot.send_photo(chat_id,photo=p2,
                   caption='<b>Что делать если не подошёл размер?</b>\n\nПервым делом, нужно смотреть на корень проблемы...\n\nСтарайтесь, пожалуйста, при оформлении заказа с обувью — правильно измерять свою стопу.\n\n<b>Подробный пример по подбору размера указан на фото ☝️</b>\n\nА если же все-таки вещь или обувь уже приехала и она плохо сидит, то к, сожалению, поменять ее на новый — невозможно, так как <b>обмен на Poizon действует всего 7 дней.</b>\n\n<b>📎 Какие остаются варианты:</b>\n\n1) Предложить вещь знакомым и близким по себестоимости.\n\n2) Продать ее на авито. Если вещь популярная, то на ней можно будет даже заработать 20-30% без каких-либо заморочек.\n\n3) Отправить ее нам под реализацию. После того, как мы получим вещь — Вы обозначите цену продажи и мы выложим ее в наш канал.',
                   parse_mode='html',reply_markup=markup)
    sent_photos[chat_id] = p2

@bot.callback_query_handler(func=lambda call: call.data == 'many_things')
def handle_many_things(call):
    chat_id = call.message.chat.id
    # Здесь добавьте логику для инструкций по регистрации
    # Например, отправка инструкций по регистрации
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Назад↩️', callback_data='back_to_question')
    markup.add(button1)
    p12 = open('painting/many_things1.jpg', 'rb')
    bot.send_photo(call.message.chat.id,photo=p12,
                   caption='<b>Как рассчитать стоимость доставки?</b>\n\nНам часто задают этот вопрос, так как не все осведомлены о том, что <b>логистика с Китая работает не совсем как внутри России.</b>\n\n<b>При заказе чего-либо по России через тот же Boxberry - при получении</b> мы платим фиксированную стоимость за отправку. При этом, если в заказе будет несколько товаров — мы не будем оплачивать фиксированную стоимость еще раз. <b>Мы платим её один раз.</b> \n\nВ случае с Китаем — фиксированной оплаты за отправку нет, <b>есть только оплата за фактическое количество килограмм(каждый товар оплачивается по отдельности).</b>\n\n<b>1. Доставка со склада в Китае до Уссурийска - 630 рублей за 1 кг товара.</b>\n\n<b>2. Доставка с Уссурийска до вашего города почтовыми службами .</b>\n\nСредняя стоимость доставки по центральной России составляет <b>примерно 250-750 рублей на одну вещь</b>(цена может изменяться от веса и количества товаров)\n\n<b>3. Примерная общая стоимость доставки на 1 пару кроссовок составляет ~1500₽</b>',
                   parse_mode='html', reply_markup=markup)
    sent_photos[chat_id] = p12

bot.infinity_polling(timeout=10, long_polling_timeout = 5)
