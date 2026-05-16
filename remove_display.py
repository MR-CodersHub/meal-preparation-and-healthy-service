with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('style="display: none;"', '')

with open('menu.html', 'w', encoding='utf-8') as f:
    f.write(content)
