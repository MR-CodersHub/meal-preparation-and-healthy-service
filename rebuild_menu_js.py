import re

with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── New menu content: a single render container + all data + renderer JS ────
new_menu_section = '''    <!-- Menu Content -->
    <section class="section-padding" style="padding-top: 0;">
        <div class="container">
            <!-- Category title -->
            <div id="menu-cat-title" class="menu-section-title" data-aos="fade-right" style="margin-bottom: 10px;">
                <h2 id="cat-heading">All <span class="text-gradient">Items</span></h2>
            </div>
            <!-- Cards grid rendered by JS -->
            <div id="menu-render-grid" class="meal-grid"></div>
        </div>
    </section>

    <style>
        @keyframes cardIn {
            from { opacity: 0; transform: translateY(22px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .menu-card-anim {
            animation: cardIn 0.38s ease forwards;
        }
    </style>

    <script>
    (function () {
        /* ═══════════════════════ MENU DATA ═══════════════════════ */
        var MENU = {
            breakfast: {
                label: 'Morning <span class="text-gradient">Classics</span>',
                items: [
                    { id: 1,  name: 'Avocado Toast Deluxe',     price: 12.50, cal: 450,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=500&q=80', desc: 'Sourdough, smashed avocado, poached eggs, microgreens, chili flakes.' },
                    { id: 2,  name: 'Berry Protein Pancakes',    price: 14.00, cal: 520,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1525648199074-cee30ba79a4a?auto=format&fit=crop&w=500&q=80', desc: 'Three fluffy oat pancakes, mixed berries, maple syrup, chia seeds.' },
                    { id: 3,  name: 'Classic Eggs Benedict',     price: 16.50, cal: 610,  badge: 'CHEF\'S PICK', badgeColor: '#ff4d4d',badgeText: '#fff',  img: 'https://images.unsplash.com/photo-1494859802809-d069c3b71a8a?auto=format&fit=crop&w=500&q=80', desc: 'English muffin, Canadian bacon, poached eggs, hollandaise sauce.' },
                    { id: 4,  name: 'Acai Super Bowl',           price: 11.00, cal: 380,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1590301157890-4810ed352733?auto=format&fit=crop&w=500&q=80', desc: 'Organic acai, house granola, banana, strawberries, coconut flakes.' },
                    { id: 5,  name: 'Smoked Salmon Bagel',       price: 13.50, cal: 540,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1519984388953-d2406bc725e1?auto=format&fit=crop&w=500&q=80', desc: 'Toasted everything bagel, cream cheese, capers, red onion, dill.' },
                    { id: 6,  name: 'Spicy Shakshuka',           price: 15.00, cal: 490,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=500&q=80', desc: 'Poached eggs in spiced tomato and bell pepper sauce with warm pita.' }
                ]
            },
            lunch: {
                label: 'Lunch <span class="text-gradient">Specials</span>',
                items: [
                    { id: 7,  name: 'Grilled Chicken Wrap',      price: 11.50, cal: 480,  badge: 'POPULAR',     badgeColor: 'var(--primary)', badgeText: '#000', img: 'https://images.unsplash.com/photo-1512152272829-e3139592d56f?auto=format&fit=crop&w=500&q=80', desc: 'Whole wheat wrap, grilled chicken, romaine, Caesar dressing.' },
                    { id: 8,  name: 'Quinoa & Roasted Veg',      price: 13.00, cal: 350,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1564834724105-918b73d1b9e0?auto=format&fit=crop&w=500&q=80', desc: 'Mixed greens, roasted butternut squash, quinoa, balsamic vinaigrette.' },
                    { id: 9,  name: 'Turkey Club Sandwich',      price: 14.50, cal: 620,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=500&q=80', desc: 'Roasted turkey, bacon, lettuce, tomato, mayo on artisan sourdough.' },
                    { id: 10, name: 'Mediterranean Salad',       price: 12.00, cal: 320,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1565299507177-b0ac66763828?auto=format&fit=crop&w=500&q=80', desc: 'Cucumbers, tomatoes, feta, kalamata olives, lemon oregano dressing.' },
                    { id: 11, name: 'Spicy Tuna Poke',           price: 16.00, cal: 510,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=500&q=80', desc: 'Sushi-grade tuna, spicy mayo, edamame, seaweed salad over rice.' },
                    { id: 12, name: 'Beef Brisket Tacos',        price: 15.50, cal: 580,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1640719028782-8230f1bdc341?auto=format&fit=crop&w=500&q=80', desc: 'Three corn tortillas, slow-cooked brisket, cilantro, salsa verde.' }
                ]
            },
            burgers: {
                label: 'Gourmet <span class="text-gradient">Burgers</span>',
                items: [
                    { id: 13, name: 'Signature Truffle Burger',  price: 18.50, cal: 820,  badge: 'BEST SELLER', badgeColor: 'var(--primary)', badgeText: '#000', img: 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=500&q=80', desc: 'Double wagyu patty, black truffle aioli, swiss cheese, caramelized onions.' },
                    { id: 14, name: "Blazin' BBQ Burger",        price: 16.00, cal: 950,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=500&q=80', desc: 'Spicy beef patty, smoked bacon, jalapeños, hickory BBQ sauce.' },
                    { id: 15, name: 'Crispy Zest Chicken',       price: 14.50, cal: 710,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1525059696034-4967a8e1dca2?auto=format&fit=crop&w=500&q=80', desc: 'Buttermilk fried chicken, citrus slaw, spicy mayo, toasted brioche.' },
                    { id: 16, name: 'Classic Cheeseburger',      price: 13.00, cal: 650,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1586190848861-99aa4a171e90?auto=format&fit=crop&w=500&q=80', desc: 'Single beef patty, american cheese, lettuce, tomato, house pickles.' },
                    { id: 17, name: 'Mushroom Swiss Burger',     price: 15.50, cal: 780,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1594212691516-b258525b42d5?auto=format&fit=crop&w=500&q=80', desc: 'Angus beef, sautéed wild mushrooms, aged swiss cheese, garlic mayo.' },
                    { id: 18, name: 'The Vegan Beast',           price: 17.00, cal: 620,  badge: 'VEGAN',       badgeColor: '#4caf50', badgeText: '#fff', img: 'https://images.unsplash.com/photo-1551782450-a2132b4ba21d?auto=format&fit=crop&w=500&q=80', desc: 'Beyond meat patty, vegan cheddar, avocado, caramelized onions, vegan bun.' }
                ]
            },
            pizza: {
                label: 'Artisan <span class="text-gradient">Pizza</span>',
                items: [
                    { id: 19, name: 'Margherita Classico',       price: 16.00, cal: 850,  badge: "CHEF'S CHOICE", badgeColor: '#ff4d4d', badgeText: '#fff', img: 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=500&q=80', desc: 'San Marzano tomatoes, fresh mozzarella, basil, extra virgin olive oil.' },
                    { id: 20, name: 'Truffle Mushroom Pizza',    price: 19.50, cal: 920,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1590947132387-155cc02f3212?auto=format&fit=crop&w=500&q=80', desc: 'Wild mushrooms, truffle cream, thyme, fontina cheese on thin crust.' },
                    { id: 21, name: 'Pepperoni Inferno',         price: 18.00, cal: 980,  badge: 'SPICY',       badgeColor: '#ff4d4d', badgeText: '#fff', img: 'https://images.unsplash.com/photo-1628840042765-356cda07504e?auto=format&fit=crop&w=500&q=80', desc: 'Spicy pepperoni, jalapeños, hot honey drizzle, mozzarella blend.' },
                    { id: 22, name: 'Quattro Formaggi',          price: 17.50, cal: 950,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1573821663912-569905455b1c?auto=format&fit=crop&w=500&q=80', desc: 'Mozzarella, gorgonzola, parmesan, ricotta on garlic-rubbed crust.' },
                    { id: 23, name: 'Vegetariana',               price: 16.50, cal: 780,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=500&q=80', desc: 'Roasted bell peppers, red onions, mushrooms, black olives, spinach.' },
                    { id: 24, name: 'BBQ Chicken Pizza',         price: 18.50, cal: 910,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1574071318508-1cdbab80d002?auto=format&fit=crop&w=500&q=80', desc: 'Smoked gouda, grilled chicken, red onions, cilantro, BBQ sauce base.' }
                ]
            },
            bowls: {
                label: 'Healthy <span class="text-gradient">Bowls</span>',
                items: [
                    { id: 25, name: 'Teriyaki Salmon Bowl',      price: 21.00, cal: 540,  badge: "CHEF'S CHOICE", badgeColor: '#ff4d4d', badgeText: '#fff', img: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=500&q=80', desc: 'Grilled Atlantic salmon, jasmine rice, edamame, pickled ginger, sesame glaze.' },
                    { id: 26, name: 'Korean Beef Bibimbap',      price: 19.00, cal: 680,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=500&q=80', desc: 'Marinated ribeye, sautéed vegetables, fried egg, gochujang sauce.' },
                    { id: 27, name: 'Vegan Buddha Bowl',         price: 15.50, cal: 420,  badge: 'VEGAN',       badgeColor: '#4caf50', badgeText: '#fff', img: 'https://images.unsplash.com/photo-1543339308-43e59d6b73a6?auto=format&fit=crop&w=500&q=80', desc: 'Quinoa, roasted chickpeas, avocado, kale, tahini lemon dressing.' },
                    { id: 28, name: 'Chicken Fiesta Bowl',       price: 16.50, cal: 590,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=500&q=80', desc: 'Grilled chicken, brown rice, black beans, corn salsa, guacamole.' },
                    { id: 29, name: 'Falafel Hummus Bowl',       price: 14.50, cal: 520,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1585325701165-f7de94762e15?auto=format&fit=crop&w=500&q=80', desc: 'Crispy falafel, creamy hummus, tabbouleh, mixed greens, tahini.' },
                    { id: 30, name: 'Ahi Tuna Poke Bowl',        price: 22.00, cal: 480,  badge: 'PREMIUM',     badgeColor: 'var(--primary)', badgeText: '#000', img: 'https://images.unsplash.com/photo-1559058789-672da06263d8?auto=format&fit=crop&w=500&q=80', desc: 'Fresh ahi tuna, sushi rice, seaweed salad, cucumber, ponzu dressing.' }
                ]
            },
            desserts: {
                label: 'Sweet <span class="text-gradient">Endings</span>',
                items: [
                    { id: 31, name: 'Molten Lava Cake',          price: 9.00,  cal: 850,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1551024506-0bccd828d307?auto=format&fit=crop&w=500&q=80', desc: 'Warm dark chocolate cake with a gooey center, vanilla bean gelato.' },
                    { id: 32, name: 'NY Cheesecake',             price: 8.50,  cal: 720,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=500&q=80', desc: 'Rich creamy cheesecake, graham cracker crust, fresh strawberry compote.' },
                    { id: 33, name: 'Artisan Macarons (6pc)',    price: 12.00, cal: 450,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1563805042-7684c8a9e9ce?auto=format&fit=crop&w=500&q=80', desc: 'Assortment of six hand-crafted macarons in seasonal flavors.' },
                    { id: 34, name: 'Tiramisu Classico',         price: 10.00, cal: 680,  badge: "CHEF'S PICK", badgeColor: '#ff4d4d', badgeText: '#fff', img: 'https://images.unsplash.com/photo-1509482560494-4126f8225994?auto=format&fit=crop&w=500&q=80', desc: 'Espresso-soaked ladyfingers, mascarpone cream, dusted with premium cocoa.' },
                    { id: 35, name: 'Lemon Meringue Tart',       price: 9.50,  cal: 510,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1495147466023-ac5c588e2e94?auto=format&fit=crop&w=500&q=80', desc: 'Tangy lemon curd in a butter crust topped with toasted Italian meringue.' },
                    { id: 36, name: 'Brownie Sundae',            price: 11.00, cal: 950,  badge: 'INDULGENT',   badgeColor: '#7c3aed', badgeText: '#fff', img: 'https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?auto=format&fit=crop&w=500&q=80', desc: 'Fudge brownie, two scoops vanilla ice cream, hot fudge, whipped cream.' }
                ]
            },
            beverages: {
                label: 'Refreshing <span class="text-gradient">Beverages</span>',
                items: [
                    { id: 37, name: 'Artisan Matcha Latte',      price: 6.50,  cal: 180,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?auto=format&fit=crop&w=500&q=80', desc: 'Ceremonial grade matcha, oat milk, touch of agave nectar.' },
                    { id: 38, name: 'Cold Brew Iced Coffee',     price: 5.00,  cal: 10,   badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1556881286-fc6915169721?auto=format&fit=crop&w=500&q=80', desc: '18-hour steeped single-origin coffee served over ice.' },
                    { id: 39, name: 'Fresh Lemonade',            price: 4.50,  cal: 150,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1544145945-f90425340c7e?auto=format&fit=crop&w=500&q=80', desc: 'Classic lemonade made with organic lemons and raw cane sugar.' },
                    { id: 40, name: 'Tropical Mango Smoothie',   price: 7.50,  cal: 220,  badge: 'POPULAR',     badgeColor: 'var(--primary)', badgeText: '#000', img: 'https://images.unsplash.com/photo-1497534446932-c925b458314e?auto=format&fit=crop&w=500&q=80', desc: 'Mango, pineapple, coconut water, and a hint of fresh mint.' },
                    { id: 41, name: 'Sparkling Berry Fizz',      price: 5.50,  cal: 80,   badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&w=500&q=80', desc: 'Mixed berry puree topped with sparkling water and fresh lime.' },
                    { id: 42, name: 'Classic Cappuccino',        price: 5.50,  cal: 120,  badge: null,          badgeColor: null,     badgeText: null,    img: 'https://images.unsplash.com/photo-1541167760496-1628856ab772?auto=format&fit=crop&w=500&q=80', desc: 'Rich espresso topped with a deep layer of perfectly foamed milk.' }
                ]
            }
        };

        var CAT_ORDER = ['breakfast','lunch','burgers','pizza','bowls','desserts','beverages'];

        /* ═══════════════════════ RENDERER ═══════════════════════ */
        var grid    = document.getElementById('menu-render-grid');
        var heading = document.getElementById('cat-heading');

        function buildCard(item, delay) {
            var badge = item.badge
                ? '<div class="offer-badge" style="background:' + item.badgeColor + ';color:' + item.badgeText + ';">' + item.badge + '</div>'
                : '';
            return '<div class="meal-card menu-card-anim" style="animation-delay:' + (delay * 0.07) + 's;">'
                + badge
                + '<img src="' + item.img + '" alt="' + item.name + '" class="meal-img" loading="lazy">'
                + '<div class="meal-info">'
                +   '<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:8px;">'
                +     '<h3 style="font-size:1rem;line-height:1.3;">' + item.name + '</h3>'
                +     '<span style="color:var(--primary);font-weight:700;white-space:nowrap;">$' + item.price.toFixed(2) + '</span>'
                +   '</div>'
                +   '<p style="color:var(--text-muted);font-size:0.85rem;margin:10px 0 0;">' + item.desc + '</p>'
                +   '<div style="display:flex;justify-content:space-between;align-items:center;margin-top:15px;">'
                +     '<span style="font-size:0.8rem;color:var(--text-muted);"><i class="fas fa-fire"></i> ' + item.cal + ' kcal</span>'
                +     '<button class="btn btn-primary" style="padding:8px 15px;font-size:0.8rem;" onclick="addToCart(' + item.id + ',\'' + item.name.replace(/'/g,"\\'") + '\',' + item.price + ',\'' + item.img + '\',\'' + item.desc.replace(/'/g,"\\'") + '\')">Add to Cart</button>'
                +   '</div>'
                + '</div>'
                + '</div>';
        }

        function renderFilter(filter) {
            var html = '';
            var itemList = [];

            if (filter === 'all') {
                heading.innerHTML = 'All <span class="text-gradient">Items</span>';
                CAT_ORDER.forEach(function(key) {
                    var cat = MENU[key];
                    html += '<div style="grid-column:1/-1;margin-top:40px;" class="menu-section-title"><h2>' + cat.label + '</h2></div>';
                    cat.items.forEach(function(item, i) {
                        html += buildCard(item, i);
                    });
                });
            } else {
                var cat = MENU[filter];
                if (!cat) return;
                heading.innerHTML = cat.label;
                cat.items.forEach(function(item, i) {
                    html += buildCard(item, i);
                });
            }

            // Wipe grid and inject
            grid.innerHTML = html;
        }

        /* ═══════════════════════ FILTER BUTTONS ═══════════════════════ */
        var filterBtns = document.querySelectorAll('.filter-btn');
        filterBtns.forEach(function(btn) {
            btn.addEventListener('click', function() {
                filterBtns.forEach(function(b) { b.classList.remove('active'); });
                btn.classList.add('active');
                renderFilter(btn.getAttribute('data-filter'));
                // Scroll to grid smoothly
                grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
            });
        });

        // Initial render — show all items
        renderFilter('all');
    })();
    </script>

'''

# Replace everything between <!-- Menu Content --> and <!-- App Banner -->
pattern = r'    <!-- Menu Content -->.*?(?=    <!-- App Banner -->)'
replacement = new_menu_section

updated = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Remove old broken filter scripts at the bottom (the style+script block we added before)
updated = re.sub(r'\s*<style>\s*@keyframes menuFadeIn.*?</style>\s*<script>\s*\(function \(\).*?</script>\s*</body>', '\n</body>', updated, flags=re.DOTALL)

with open('menu.html', 'w', encoding='utf-8') as f:
    f.write(updated)

print("Done! Menu rebuilt with JS data-driven renderer.")
