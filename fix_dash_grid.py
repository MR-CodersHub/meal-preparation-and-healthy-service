import glob
import re

files = glob.glob('admin*.html') + glob.glob('dashboard.html') + glob.glob('user*.html')
files = list(set(files))

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace inline 2fr 1fr grid with class
    new_content = content.replace(
        '<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 30px;">',
        '<div class="dash-layout-grid">'
    )
    
    # Also fix potential table overflow in user dashboards
    # Ensure there is a wrapper for tables if there's any
    # (Actually .dash-table already has overflow-x handling in CSS, we'll check it later)
    
    # Also fix inline min-width in dashboard.html that forces wide layout
    new_content = new_content.replace('min-width: 150px;', 'min-width: 100px;')
    new_content = new_content.replace('min-width: 200px;', 'min-width: 150px;')

    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1

print(f'Updated {count} files.')
