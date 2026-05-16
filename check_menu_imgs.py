import re
import requests
import os

with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all img URLs
urls = re.findall(r"img: '([^']+)'", content)

print(f"Checking {len(urls)} images...")

for url in urls:
    if url.startswith('http'):
        try:
            r = requests.head(url, timeout=5)
            if r.status_code >= 400:
                print(f"  [BROKEN] {url} - Status: {r.status_code}")
            else:
                pass # print(f"  [OK] {url}")
        except Exception as e:
            print(f"  [ERROR] {url} - {str(e)}")
    else:
        # Local file
        path = os.path.join(os.getcwd(), url.replace('/', os.sep))
        if not os.path.exists(path):
            print(f"  [BROKEN LOCAL] {url}")
        else:
            print(f"  [OK LOCAL] {url}")

print("Check complete.")
