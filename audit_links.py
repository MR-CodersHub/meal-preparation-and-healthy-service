import os, re
from pathlib import Path

# All HTML files in project
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
file_sizes = {f: os.path.getsize(f) for f in html_files}

# Pages that exist
existing_pages = set(html_files)

print("=== FILE SIZE AUDIT (files under 6KB are likely stubs) ===")
for f, size in sorted(file_sizes.items(), key=lambda x: x[1]):
    flag = " <-- STUB?" if size < 5000 else ""
    print(f"  {size:>8} bytes  {f}{flag}")

print("\n=== BROKEN HREF LINKS ===")
all_issues = []
for fname in html_files:
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    hrefs = re.findall(r'href="([^"#][^"]*)"', content)
    for href in hrefs:
        # Only local .html files
        if href.endswith('.html') and not href.startswith('http'):
            base = href.split('?')[0].split('#')[0]
            if base not in existing_pages:
                all_issues.append(f"  [{fname}] --> MISSING: {href}")

if all_issues:
    for issue in all_issues:
        print(issue)
else:
    print("  All local .html links resolve to existing files!")

print("\n=== PLACEHOLDER # LINKS ===")
for fname in html_files:
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    count = content.count('href="#"')
    if count > 0:
        print(f"  {fname}: {count} placeholder '#' links")
