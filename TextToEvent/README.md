# Text To Event

Script to convert a list of text-based events into a `.ics` calendar file, compatible with Google Calendar, Outlook, Apple Calendar, and others.

## 📦 Features

- Generate `.ics` files from a list of events.
- Supports flexible date formats: `DD/MM`, `DD/MM/YY`, and `DD/MM/YYYY`.
- Custom start and end times for each event.
- Keeps sensitive data out of the repository with a template system.

---

## 🛠 How to Use

1. **Create the file `events_data.py`**

   Create a file named `events_data.py` inside of this project/folder (TextToEvent)

   This file should contain your personal event data using the same structure shown in `events_data_example.py`.

   Example content:

   ```python
   event_list = [
       {
           'date': '09/04',
           'title': 'Work',
           'start_time': '08:00',
           'end_time': '16:00'
       },
       {
           'date': '13/04/24',
           'title': 'Work',
           'start_time': '15:00',
           'end_time': '20:00'
       },
   ]

2. **Run the script**

   Execute the `text_to_event.py` file. A folder named `ics_events` will be automatically created (if it doesn't already exist), and the generated `.ics` file will be saved inside it with the name.


3. **Import the `.ics` file into your calendar**

The generated `.ics` file can be imported into various calendar applications, including:

- **Microsoft Outlook**
- **Google Calendar**
- **Apple Calendar (iCloud or native macOS/iOS app)**
- **Any other app that supports `.ics` files**

4. **Keeping your data private**

- The `events_data.py` file should only contain **your personal information**.
- **Do not upload this file to GitHub.**
- To do this:
  - Create `events_data.py` locally with your real data.
  - Use the `events_data_example.py` file as a public example to keep in the repository.
  - Add `events_data.py` to your `.gitignore` file to make sure it's not included in commits:

    ```
    TextToEvent/events_data.py
    ```

This ensures you can work with your private information locally without exposing it in the repository.