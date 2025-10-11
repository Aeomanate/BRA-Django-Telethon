@echo off
REM Активуємо venv (якщо потрібно - зміни шлях)
call .venv\Scripts\activate

REM Встановлюємо всі залежності
pip install -r requirements.txt

REM Запускаємо скрипт, який створює py.typed у telethon
python types_tabs_fix.py

echo.
echo Done!