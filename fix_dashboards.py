import os
import glob
import re

files = glob.glob('admin-*.html') + glob.glob('user-*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Add sidebar-overlay if missing
    if '<div class="sidebar-overlay"></div>' not in content:
        content = content.replace('<body>', '<body>\n    <div class="sidebar-overlay"></div>')
    
    # Wrap h1 with toggle button
    h1_match = re.search(r'<h1>(.*?)</h1>', content)
    if h1_match and '<button class="dash-toggle"' not in content:
        h1_inner = h1_match.group(1)
        new_header = f'''<div class="mobile-dash-header" style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <button class="dash-toggle" aria-label="Toggle Sidebar" style="background: none; border: none; outline: none;">
                        <i class="fas fa-bars"></i>
                    </button>
                    <h1 style="font-size: clamp(1.2rem, 5vw, 2.5rem); margin: 0;">{h1_inner}</h1>
                </div>'''
        content = content.replace(h1_match.group(0), new_header)
    
    # Add main.js if missing
    if '<script src="js/main.js"></script>' not in content:
        content = content.replace('</body>', '    <script src="js/main.js"></script>\n</body>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print(f'Processed {len(files)} files.')
