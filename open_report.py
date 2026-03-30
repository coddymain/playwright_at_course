#!/usr/bin/env python3
import webbrowser
import os
from pathlib import Path

report_path = Path.cwd() / "allure-report" / "index.html"

if report_path.exists():
    webbrowser.open(f"file://{report_path.absolute()}")
    print(f"✅ Отчёт открыт: {report_path}")
else:
    print("❌ Отчёт не найден. Сначала запусти:")
    print("   pytest tests/ --alluredir=./allure-results")
    print("   allure generate ./allure-results --clean -o ./allure-report")