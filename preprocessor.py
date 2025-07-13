import re
import pandas as pd

def preprocess(data):
    # Remove hidden characters like U+200E (LEFT-TO-RIGHT MARK)
    data = data.replace('\u200e', '')

    # Regex to extract datetime, user, and message
    pattern = r'\[(\d{2}/\d{2}/\d{2}), (\d{2}:\d{2}:\d{2})\] (.*?): (.*)'

    matches = re.findall(pattern, data)

    if not matches:
        return pd.DataFrame()  # Return empty DataFrame if nothing matched

    # Store structured data
    dates, users, messages = [], [], []
    for date, time, user, message in matches:
        full_datetime = f"{date}, {time}"
        dates.append(full_datetime)
        users.append(user.strip())
        messages.append(message.strip())

    # Create DataFrame
    df = pd.DataFrame({
        'date': pd.to_datetime(dates, format='%d/%m/%y, %H:%M:%S'),
        'user': users,
        'message': messages
    })

    # Enrich with time-based features
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # Period (e.g., 13-14)
    df['period'] = df['hour'].apply(lambda h: f"{h:02d}-{(h + 1) % 24:02d}")

    return df
