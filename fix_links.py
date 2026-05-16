import re, os

# Files to patch href="#" social links and Download App buttons
files = [
    'index.html', 'home2.html', 'about.html', 'menu.html',
    'blog.html', 'contact.html', 'services.html', 'dashboard.html',
    'cart.html', 'login.html', 'admin.html', 'admin-orders.html',
    'admin-users.html', 'admin-content.html', 'admin-notifications.html',
    'admin-revenue.html', 'admin-settings.html', 'admin-tracking.html',
    'user-orders.html', 'user-favorites.html', 'user-messages.html',
    'user-settings.html', 'user-tracking.html'
]

social_map = {
    'fa-facebook-f': 'https://www.facebook.com',
    'fa-instagram':  'https://www.instagram.com',
    'fa-twitter':    'https://twitter.com',
    'fa-linkedin-in': 'https://www.linkedin.com',
    'fa-youtube':    'https://www.youtube.com',
}

def fix_social_links(content):
    """Replace href="#" on social icon anchors with real URLs"""
    for icon_class, url in social_map.items():
        # Match: <a href="#"><i class="fab fa-ICON"></i></a>
        pattern = rf'(<a\s+href=")#("\s*>(?:\s*<i[^>]+{re.escape(icon_class)}[^>]*>\s*</i>\s*)</a>)'
        replacement = rf'\g<1>{url}" target="_blank"\2'
        content = re.sub(pattern, replacement, content)
    return content

def fix_download_app(content):
    """Point 'Download App' buttons to coming-soon.html"""
    content = re.sub(
        r'(<a\s[^>]*?)href="#"([^>]*>(?:Download App|Get App|Download|App Store|Google Play)[^<]*</a>)',
        r'\1href="coming-soon.html"\2',
        content,
        flags=re.IGNORECASE
    )
    return content

total_changed = 0
for fname in files:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        original = f.read()
    
    updated = fix_social_links(original)
    updated = fix_download_app(updated)
    
    if updated != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"  Fixed: {fname}")
        total_changed += 1
    else:
        print(f"  OK (no changes): {fname}")

print(f"\nTotal files patched: {total_changed}")
