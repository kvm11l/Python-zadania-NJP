"""
Zadanie 2 - Kalkulator stref czasowych
"""

from datetime import datetime
from pytz import timezone
import pytz

# Wyświetlenie wszystkich stref czasowych
print('Timezones')
for timeZone in pytz.all_timezones:           
   print(timeZone)


def convert_timezone(source_time, source_tz, target_tz):
    # Tworzenie obiektu datetime dla wprowadzonej godziny
    source_datetime = datetime.strptime(source_time, "%H:%M")

    # Ustalanie strefy czasowej zrodlowej i docelowej
    source_timezone = timezone(source_tz)
    target_timezone = timezone(target_tz)

    # Konwersja strefy czasowej
    source_datetime = source_timezone.localize(source_datetime)
    target_datetime = source_datetime.astimezone(target_timezone)

    # Formatowanie i zwracanie wyniku
    target_time = target_datetime.strftime("%H:%M")
    return target_time

if __name__ == "__main__":
    # Przykładowe działanie
    source_time = input("Podaj godzinę (HH:MM): ")
    source_tz = input("Podaj źródłową strefę czasową: ")
    target_tz = input("Podaj docelową strefę czasową: ")

    converted_time = convert_timezone(source_time, source_tz, target_tz)
    print(f"Przekonwertowana godzina: {converted_time}")

    # Przykład użycia funkcji bez inputu 
    converted_time = convert_timezone("12:20", "UTC", "Europe/Warsaw")
    print(f"Przekonwertowana godzina (dla 12:20 UTC Europe/Warsaw): {converted_time}")