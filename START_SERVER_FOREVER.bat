@echo off
echo ========================================
echo Starting Prairies Africa Backend Forever
echo ========================================
echo.

:loop
echo [%date% %time%] Starting Django server...
cd /d "C:\Users\sean\Desktop\my website\backend"
python manage.py runserver 0.0.0.0:8000

echo [%date% %time%] Server crashed or stopped. Restarting in 5 seconds...
timeout /t 5 /nobreak > nul
goto loop
