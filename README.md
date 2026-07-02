# Бэкенд для сайта «Корявый Бас»

Небольшой Flask-сервер, который принимает данные из форм на сайте и
пересылает их вам на email и в Telegram одновременно.

---

## Шаг 1. Создать Telegram-бота и узнать chat_id

1. В Telegram напишите **@BotFather** → `/newbot` → следуйте инструкциям.
   В конце вы получите **токен бота** (строка вида `123456:ABC-DEF...`).
2. Напишите своему новому боту любое сообщение (например «привет»), чтобы
   он "увидел" ваш чат.
3. Откройте в браузере (подставив свой токен):
   ```
   https://api.telegram.org/bot<ВАШ_ТОКЕН>/getUpdates
   ```
4. В ответе найдите `"chat":{"id": 123456789, ...}` — это и есть ваш
   **TELEGRAM_CHAT_ID**.

## Шаг 2. Настроить email (Gmail, пример)

1. Включите двухфакторную аутентификацию в аккаунте Google.
2. Создайте **App Password**: https://myaccount.google.com/apppasswords
   (обычный пароль от почты для SMTP не подойдёт).
3. Запишите:
   - `SMTP_USER` — ваш email (например `station.korba@gmail.com`)
   - `SMTP_PASSWORD` — сгенерированный App Password
   - `EMAIL_TO` — куда присылать заявки (можно тот же адрес)

Если у вас другой почтовый провайдер (Яндекс, Mail.ru и т.д.) — просто
поменяйте `SMTP_HOST`/`SMTP_PORT` на его данные, у каждого провайдера
свои App Password настраиваются похожим образом.

## Шаг 3. Задеплоить бэкенд на Render.com (бесплатно)

1. Зарегистрируйтесь на https://render.com (можно через GitHub).
2. Создайте новый **приватный** репозиторий на GitHub и залейте туда
   папку `backend/` (файлы `app.py`, `requirements.txt`, `Procfile`).
3. В Render: **New → Web Service** → подключите этот репозиторий.
4. Настройки сервиса:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Во вкладке **Environment** добавьте переменные:
   - `SMTP_USER`
   - `SMTP_PASSWORD`
   - `EMAIL_TO`
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
6. Нажмите **Create Web Service** — Render соберёт и запустит проект.
   После деплоя вы получите адрес вида
   `https://koraviy-bas-backend.onrender.com`.

> Бесплатный тариф Render «засыпает» после ~15 минут без запросов и
> первый запрос после этого выполняется на 20-30 секунд дольше —
> для формы заявок это некритично.

## Шаг 4. Подключить адрес бэкенда к сайту

В файле `index.html` найдите строку:

```js
const BACKEND_URL = 'https://ВАШ-БЭКЕНД.onrender.com';
```

и замените на реальный адрес, который выдал Render.

## Шаг 5. Проверить

Откройте сайт, заполните любую из форм и отправьте — сообщение должно
прийти вам в Telegram и на почту одновременно. Логи можно посмотреть
во вкладке **Logs** в Render.

---

### Локальный запуск (для теста перед деплоем)

```bash
cd backend
pip install -r requirements.txt
export SMTP_USER="..."
export SMTP_PASSWORD="..."
export EMAIL_TO="..."
export TELEGRAM_BOT_TOKEN="..."
export TELEGRAM_CHAT_ID="..."
python app.py
```

Сервер запустится на `http://localhost:5000`. Для локального теста
временно укажите в `index.html`:
```js
const BACKEND_URL = 'http://localhost:5000';
```
