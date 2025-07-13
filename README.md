# Wp Chat Analyzer

An interactive Streamlit app that analyzes WhatsApp chat exports and gives you deep insights into conversation patterns, top users, emojis, word usage, timelines, and more.

---

## Features

- Total messages, words, media, links
- Daily & monthly timeline of chat activity
- Busiest day of the week and month
- Hourly heatmap of activity
- Most active users in group chats
- WordCloud of most common words
- Top 20 most used words
- Emoji usage and distribution
- Works for both private and group chats

---

## Demo

[[Open Demo WebApp](https://wp-chat-analyzer-by-ronit.streamlit.app/)]

> Upload a `.txt` file exported from WhatsApp (Chat Backup > Export > Without Media)

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ronitsandooja/wp-chat-analyzer.git
cd wp-chat-analyzer
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

---

## File Structure

```
├── app.py                # Main Streamlit app
├── helper.py             # All feature logic
├── preprocessor.py       # Parses and structures chat text
└── requirements.txt      # Python dependencies
```

---

## How to Export WhatsApp Chat

1. Open the WhatsApp chat you want to analyze
2. [for Iphone]Tap on profile > Scroll down > Export chat
3. [for Android]Tap the 3-dot menu > More > Export Chat
4. Choose **"Without Media"**
5. Transfer the `.txt` file to your computer
6. Upload it in the app

---

## Supported Formats

* Supports only:

  * **24-hour** timestamps: `[04/01/24, 21:45:19]`

* Works with both:

  * **Private chats**
  * **Group chats** (even with long usernames or group names)

---

## Built With

* [Streamlit](https://streamlit.io)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [WordCloud](https://github.com/amueller/word_cloud)
* [emoji](https://pypi.org/project/emoji/)
* [URLExtract](https://github.com/lipoja/URLExtract)

---

## License

This project is open-source and free to use under the MIT License.

---

## Acknowledgments

Inspired by community WhatsApp analytics tools and the growing need for analyzing digital conversations in a fun, visual, and private way.

