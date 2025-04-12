from datetime import datetime, timedelta
import os
import events_data

event_list = events_data.event_list

def parse_date(date_str):
    """Aceita formatos DD/MM, DD/MM/YY ou DD/MM/YYYY"""
    current_year = datetime.now().year

    try:
        if len(date_str) == 5: # Formato: DD/MM
            full_date = f"{date_str}/{current_year}"
            return datetime.strptime(full_date, "%d/%m/%Y")
        elif len(date_str) == 8: # Formato: DD/MM/YY
            return datetime.strptime(date_str, "%d/%m/%y")
        elif len(date_str) == 10: # Formato: DD/MM/YYYY
            return datetime.strptime(date_str, "%d/%m/%Y")
        else:
            raise ValueError
    except ValueError:
        raise ValueError(f"Data '{date_str}' não é válida. Use DD/MM, DD/MM/YY ou DD/MM/YYYY.")

try:
    # Caminho da pasta onde o script está localizado
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Subpasta "ics_events" no mesmo nível do script
    output_folder = os.path.join(base_path, "ics_events")
    os.makedirs(output_folder, exist_ok=True)

    # Lista para armazenar os VEVENTs
    events_ics = []

    def format_ics_datetime(dt):
        return dt.strftime("%Y%m%dT%H%M%S")

    for event in event_list:
        # Obter dados do evento
        date_str = event['date']
        title = event['title']
        start_time_str = event['start_time']
        end_time_str = event['end_time']

        # Interpretar a data corretamente
        event_date = parse_date(date_str)

        # Criar datetime completo com hora
        start_dt = datetime.strptime(f"{event_date.strftime('%d/%m/%Y')} {start_time_str}", "%d/%m/%Y %H:%M")
        end_dt = datetime.strptime(f"{event_date.strftime('%d/%m/%Y')} {end_time_str}", "%d/%m/%Y %H:%M")

        vevent = f"""BEGIN:VEVENT
UID:{start_dt.strftime("%Y%m%d%H%M")}@yourevent.com
DTSTAMP:{format_ics_datetime(datetime.now())}
DTSTART:{format_ics_datetime(start_dt)}
DTEND:{format_ics_datetime(end_dt)}
SUMMARY:{title}
LOCATION:Online
DESCRIPTION:{title}
STATUS:CONFIRMED
END:VEVENT"""
        events_ics.append(vevent)

    # Montar o conteúdo final do .ics
    ics_full_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Your Name//Event Calendar//EN\n"
    ics_full_content += "\n".join(events_ics)
    ics_full_content += "\nEND:VCALENDAR"

    # Escrever arquivo
    final_ics_path = os.path.join(output_folder, "all_events.ics")
    with open(final_ics_path, "w", encoding="utf-8") as f:
        f.write(ics_full_content)

    print(f"Single .ics file generated at: {final_ics_path}")

except Exception as e:
    print(f"ERROR: {e}")

finally:
    input("Press Enter to quit...")
