from datetime import datetime, timedelta
import os
import events_data

event_list = events_data.event_list

def parse_date(date_str):
    """Função para interpretar e completar a data no formato DD/MM ou DD/MM/YY/DD/MM/YYYY"""
    current_year = datetime.now().year
    try:
        # Tentando interpretar a data com o ano atual caso seja DD/MM
        if len(date_str) == 5:  # Formato DD/MM
            full_date = f"{date_str}/{current_year}"
            return datetime.strptime(full_date, "%d/%m/%Y")
        
        # Tentando interpretar a data com ano de 2 ou 4 dígitos (DD/MM/YY ou DD/MM/YYYY)
        return datetime.strptime(date_str, "%d/%m/%Y")  # Formato DD/MM/YYYY ou DD/MM/YY
    
    except ValueError:
        raise ValueError(f"Data '{date_str}' não é válida.")

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
        # Obter a data, título e horários do evento
        date_str = event['date']
        title = event['title']
        start_time_str = event['start_time']
        end_time_str = event['end_time']
        
        # Interpretar a data, seja no formato DD/MM, DD/MM/YY ou DD/MM/YYYY
        event_date = parse_date(date_str)
        
        # Converter as strings de data e hora para datetime
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

    # Montar o conteúdo final do arquivo .ics
    ics_full_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Your Name//Event Calendar//EN\n"
    ics_full_content += "\n".join(events_ics)
    ics_full_content += "\nEND:VCALENDAR"

    # Caminho final do arquivo .ics
    final_ics_path = os.path.join(output_folder, "all_events.ics")
    with open(final_ics_path, "w", encoding="utf-8") as f:
        f.write(ics_full_content)

    print(f"Single .ics file generated at: {final_ics_path}")

except Exception as e:
    print(f"ERROR: {e}")

finally:
    input("Press Enter to quit...")
