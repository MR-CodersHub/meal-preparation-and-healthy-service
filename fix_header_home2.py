import os
import glob
import re

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Remove hardcoded theme-controls
    # We look for <div class="theme-controls">...</div> inside <div class="nav-btns">
    # Note: main.js injects it, so we shouldn't hardcode it anywhere.
    theme_pattern = re.compile(r'<div class="theme-controls">\s*<button id="theme-btn"[^>]*>.*?</button>\s*</div>', re.DOTALL)
    if theme_pattern.search(content):
        content = theme_pattern.sub('', content)

    # 2. Add Home2 to nav-links if missing
    # Find <ul class="nav-links"> and the first <li> which should be Home.
    # We will insert Home2 right after the first <li> containing "Home"
    if 'href="home2.html"' not in content and 'Home2' not in content:
        # Search for the Home li
        home_li_pattern = re.compile(r'(<li[^>]*><a[^>]*href="index\.html"[^>]*>.*?Home.*?</a></li>)', re.IGNORECASE)
        match = home_li_pattern.search(content)
        if match:
            home2_li = '\n                    <li role="none"><a href="home2.html" role="menuitem">Home2</a></li>'
            content = content[:match.end()] + home2_li + content[match.end():]

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f'Processed {len(html_files)} files.')
