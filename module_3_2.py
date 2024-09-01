def send_email(message, recipient, sender='university.help@gmail.com'):
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    elif ("@" and (".com" or ".ru" or ".net")) not in recipient and ("@" and (".com" or ".ru" or ".net")) not in sender:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)


send_email('Это сообщение для проверки связи', 'GadwetB@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')