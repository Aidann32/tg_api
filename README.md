# Как работает API

## 1. auth/users/
![изображение](https://github.com/Aidann32/tg_api/assets/46024391/7494bb2c-86c1-475f-8150-b28154079f4f)
Необходимо зарегистрироваться
В JSON body необходимо указать логин, имя и пароль

## 2. auth/token/login
![изображение](https://github.com/Aidann32/tg_api/assets/46024391/70985b2e-6177-4985-8654-146bbbb129e6)
Необходимо аутентифицироваться
В этой ручке аутентификации через form-data необходимо указать логин и пароль
В ответе сервер отдас auth_token, его нужно отправить в ТГ бота(https://t.me/TestTelgramAPIbot)

## 3. bot/send_message
![изображение](https://github.com/Aidann32/tg_api/assets/46024391/385935d5-9deb-4169-ae67-fdda2c08a3f8)
В Headers указать ключ Authorization и значение Token {auth_token}, как показано на скрине
В теле запроса необходимо JSON'ом указать сообщение которое вы хотите отправить
![изображение](https://github.com/Aidann32/tg_api/assets/46024391/c4770475-baa4-4af3-98bd-3ec0b0b26ed2)

## 4. bot/messages
![изображение](https://github.com/Aidann32/tg_api/assets/46024391/8f1fd6cc-c12b-42f0-9a20-be34e5fa5317)
Получение всех сообщений отправленных вами(не забудьте Authorization)



