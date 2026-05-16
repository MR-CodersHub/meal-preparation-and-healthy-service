with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.splitlines()

print("Total lines:", len(lines))

checks = [
    'menu-render-grid', 'renderFilter', 'MENU', 'data-filter',
    'filter-btn', 'addToCart', 'App Banner',
    'Truffle Mushroom Pizza', 'Molten Lava Cake', 'Artisan Matcha Latte',
    'Signature Truffle Burger', 'Vegan Buddha Bowl'
]
for c in checks:
    status = "OK" if c in content else "MISSING"
    print(f"  [{status}] {c}")
