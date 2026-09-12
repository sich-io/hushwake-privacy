#!/usr/bin/env python3
"""Собирает юридические страницы Hushwake на шести языках.

Английский лежит в корне, остальные — в подпапках по коду языка:
App Store Connect принимает свой Privacy Policy URL на каждую локаль.

Правится ТОЛЬКО `content.py`, потом `python3 build.py`. HTML руками
не трогать — он перезапишется.
"""
import os
from content import LANGUAGES, PAGES, UI

ROOT = os.path.dirname(os.path.abspath(__file__))
UPDATED = "12 September 2026"

# Знак приложения: купол и расходящийся от него звук — то же, что на иконке.
MARK = """  <div class="mark" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4"
         stroke-linecap="round" stroke-linejoin="round">
      <path d="M2.5 13.4c1.6 0 2.6 1.6 4.2 1.6s2.4-3 4.1-3 2.6 5.4 4.3 5.4S17.6 5 21.5 5"/>
    </svg>
  </div>"""

def switcher(current):
    """Переключатель языков. Из корня ссылки вниз, из подпапки — вбок через `../`."""
    items = []
    for code, meta in LANGUAGES.items():
        if code == "en":
            href = "../" if current != "en" else "./"
        else:
            href = ("" if current == "en" else "../") + code + "/"
        cls = ' class="current"' if code == current else ""
        items.append(f'<a href="{href}" hreflang="{code}"{cls}>{meta["name"]}</a>')
    return '<div class="langs">' + "\n  ".join(items) + "</div>"


def page(lang, name):
    css = "style.css" if lang == "en" else "../style.css"
    title = UI[lang]["titles"][name]
    nav = "\n  ".join(
        f'<a href="{href}">{UI[lang]["nav"][key]}</a>'
        for key, href in (("privacy", "./"), ("terms", "terms.html"), ("support", "support.html"))
    )
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Hushwake</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<div class="wrap">
<header>
{MARK}
  <h1>{title}</h1>
  <p class="updated">Hushwake · {UI[lang]['updated']} {UPDATED}</p>
</header>
{PAGES[lang][name].strip()}
<nav>
  {nav}
</nav>
{switcher(lang)}
<footer>
  {UI[lang]['footer']} <a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a>
</footer>
</div>
</body>
</html>
"""


def main():
    missing = [code for code in LANGUAGES if code not in PAGES]
    if missing:
        print("нет текстов для:", ", ".join(missing))

    written = 0
    for lang in PAGES:
        directory = ROOT if lang == "en" else os.path.join(ROOT, lang)
        os.makedirs(directory, exist_ok=True)
        for name in ("index", "terms", "support"):
            path = os.path.join(directory, f"{name}.html")
            with open(path, "w", encoding="utf-8") as f:
                f.write(page(lang, name))
            written += 1
    print(f"собрано страниц: {written}")


if __name__ == "__main__":
    main()
