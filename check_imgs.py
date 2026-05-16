import re

with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

imgs = re.findall(r'src="(https://images\.unsplash\.com[^"]+)"', content)
print('All image URLs found:')
for i, url in enumerate(imgs, 1):
    print(f'{i}: {url}')
