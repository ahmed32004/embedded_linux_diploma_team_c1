
#!/usr/bin/python3
import webbrowser

favourite_websites = {
    "google": "https://www.google.com/",
    "facebook": "https://www.facebook.com/",
    "youtube": "https://www.youtube.com/"
}


def firefox(url):
    webbrowser.get('firefox').open_new_tab(url)
