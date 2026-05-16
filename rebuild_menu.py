import re

with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract everything before Menu Content
pre_match = re.search(r'(.*?<!-- Menu Content -->\s*<section class=\"section-padding\" style=\"padding-top: 0;\">\s*<div class=\"container\">\s*)', content, flags=re.DOTALL)
pre_content = pre_match.group(1) if pre_match else content.split('<!-- Menu Content -->')[0] + '<!-- Menu Content -->\n    <section class=\"section-padding\" style=\"padding-top: 0;\">\n        <div class=\"container\">\n'

# Extract everything from App Banner onwards
post_match = re.search(r'(</section>\s*<!-- App Banner -->.*)', content, flags=re.DOTALL)
post_content = post_match.group(1) if post_match else '\n        </div>\n    </section>\n\n    <!-- App Banner -->' + content.split('<!-- App Banner -->')[1]

# Define 6 distinct items per category
categories = [
    {
        'id': 'breakfast',
        'title': 'Morning <span class=\"text-gradient\">Classics</span>',
        'items': [
            {'img': 'https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=500&q=80', 'name': 'Avocado Toast Deluxe', 'price': 12.50, 'desc': 'Sourdough, smashed avocado, poached eggs, microgreens, chili flakes.', 'cal': 450},
            {'img': 'https://images.unsplash.com/photo-1525648199074-cee30ba79a4a?auto=format&fit=crop&w=500&q=80', 'name': 'Berry Protein Pancakes', 'price': 14.00, 'desc': 'Three fluffy oat pancakes, mixed berries, maple syrup, chia seeds.', 'cal': 520},
            {'img': 'https://images.unsplash.com/photo-1494859802809-d069c3b71a8a?auto=format&fit=crop&w=500&q=80', 'name': 'Classic Eggs Benedict', 'price': 16.50, 'desc': 'English muffin, Canadian bacon, poached eggs, hollandaise sauce.', 'cal': 610},
            {'img': 'https://images.unsplash.com/photo-1550507992-eb63ffee0224?auto=format&fit=crop&w=500&q=80', 'name': 'Acai Super Bowl', 'price': 11.00, 'desc': 'Organic acai, house granola, banana, strawberries, coconut flakes.', 'cal': 380},
            {'img': 'https://images.unsplash.com/photo-1514326640560-7d063ef2aed5?auto=format&fit=crop&w=500&q=80', 'name': 'Smoked Salmon Bagel', 'price': 13.50, 'desc': 'Toasted everything bagel, cream cheese, capers, red onion, dill.', 'cal': 540},
            {'img': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=500&q=80', 'name': 'Spicy Shakshuka', 'price': 15.00, 'desc': 'Poached eggs in a hearty, spiced tomato and bell pepper sauce with pita.', 'cal': 490}
        ]
    },
    {
        'id': 'lunch',
        'title': 'Lunch <span class=\"text-gradient\">Specials</span>',
        'items': [
            {'img': 'https://images.unsplash.com/photo-1512152272829-e3139592d56f?auto=format&fit=crop&w=500&q=80', 'name': 'Grilled Chicken Wrap', 'price': 11.50, 'desc': 'Whole wheat wrap, grilled chicken, romaine, Caesar dressing.', 'cal': 480, 'badge': 'POPULAR'},
            {'img': 'https://images.unsplash.com/photo-1564834724105-918b73d1b9e0?auto=format&fit=crop&w=500&q=80', 'name': 'Quinoa & Roasted Veg', 'price': 13.00, 'desc': 'Mixed greens, roasted butternut squash, quinoa, balsamic vinaigrette.', 'cal': 350},
            {'img': 'https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=500&q=80', 'name': 'Turkey Club Sandwich', 'price': 14.50, 'desc': 'Roasted turkey, bacon, lettuce, tomato, mayo on artisan bread.', 'cal': 620},
            {'img': 'https://images.unsplash.com/photo-1546069901-d5bfd2cbfb1f?auto=format&fit=crop&w=500&q=80', 'name': 'Mediterranean Salad', 'price': 12.00, 'desc': 'Cucumbers, tomatoes, feta cheese, kalamata olives, lemon oregano dressing.', 'cal': 320},
            {'img': 'https://images.unsplash.com/photo-1554998171-7e599bc96cca?auto=format&fit=crop&w=500&q=80', 'name': 'Spicy Tuna Poke', 'price': 16.00, 'desc': 'Sushi-grade tuna, spicy mayo, edamame, seaweed salad over rice.', 'cal': 510},
            {'img': 'https://images.unsplash.com/photo-1529042410759-befb1204b468?auto=format&fit=crop&w=500&q=80', 'name': 'Beef Brisket Tacos', 'price': 15.50, 'desc': 'Three corn tortillas, slow-cooked brisket, cilantro, onions, salsa verde.', 'cal': 580}
        ]
    },
    {
        'id': 'burgers',
        'title': 'Gourmet <span class=\"text-gradient\">Burgers</span>',
        'items': [
            {'img': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=500&q=80', 'name': 'Signature Truffle Burger', 'price': 18.50, 'desc': 'Double wagyu patty, black truffle aioli, swiss cheese, caramelized onions.', 'cal': 820, 'badge': 'BEST SELLER', 'badge_color': 'var(--primary)', 'text_color': '#000'},
            {'img': 'https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=500&q=80', 'name': "Blazin' BBQ Burger", 'price': 16.00, 'desc': 'Spicy beef patty, smoked bacon, jalapeños, hickory BBQ sauce.', 'cal': 950},
            {'img': 'https://images.unsplash.com/photo-1525059696034-4967a8e1dca2?auto=format&fit=crop&w=500&q=80', 'name': 'Crispy Zest Chicken', 'price': 14.50, 'desc': 'Buttermilk fried chicken, citrus slaw, spicy mayo, toasted brioche.', 'cal': 710},
            {'img': 'https://images.unsplash.com/photo-1586190848861-99aa4a171e90?auto=format&fit=crop&w=500&q=80', 'name': 'Classic Cheeseburger', 'price': 13.00, 'desc': 'Single beef patty, american cheese, lettuce, tomato, house pickles.', 'cal': 650},
            {'img': 'https://images.unsplash.com/photo-1594212691516-b258525b42d5?auto=format&fit=crop&w=500&q=80', 'name': 'Mushroom Swiss Burger', 'price': 15.50, 'desc': 'Angus beef, sautéed wild mushrooms, aged swiss cheese, garlic mayo.', 'cal': 780},
            {'img': 'https://images.unsplash.com/photo-1551782450-a2132b4ba21d?auto=format&fit=crop&w=500&q=80', 'name': 'The Vegan Beast', 'price': 17.00, 'desc': 'Beyond meat patty, vegan cheddar, avocado, caramelized onions, vegan bun.', 'cal': 620}
        ]
    },
    {
        'id': 'pizza',
        'title': 'Artisan <span class=\"text-gradient\">Pizza</span>',
        'items': [
            {'img': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=500&q=80', 'name': 'Margherita Classico', 'price': 16.00, 'desc': 'San Marzano tomatoes, fresh mozzarella, basil, extra virgin olive oil.', 'cal': 850, 'badge': "CHEF'S CHOICE", 'badge_color': '#ff4d4d', 'text_color': '#fff'},
            {'img': 'https://images.unsplash.com/photo-1590947132387-155cc02f3212?auto=format&fit=crop&w=500&q=80', 'name': 'Truffle Mushroom Pizza', 'price': 19.50, 'desc': 'Wild mushrooms, truffle cream, thyme, fontina cheese.', 'cal': 920},
            {'img': 'https://images.unsplash.com/photo-1628840042765-356cda07504e?auto=format&fit=crop&w=500&q=80', 'name': 'Pepperoni Inferno', 'price': 18.00, 'desc': 'Spicy pepperoni, jalapeños, hot honey drizzle, mozzarella.', 'cal': 980},
            {'img': 'https://images.unsplash.com/photo-1573821663912-569905455b1c?auto=format&fit=crop&w=500&q=80', 'name': 'Quattro Formaggi', 'price': 17.50, 'desc': 'Mozzarella, gorgonzola, parmesan, ricotta, garlic confit.', 'cal': 950},
            {'img': 'https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=500&q=80', 'name': 'Vegetariana', 'price': 16.50, 'desc': 'Roasted bell peppers, red onions, mushrooms, black olives, spinach.', 'cal': 780},
            {'img': 'https://images.unsplash.com/photo-1574071318508-1cdbab80d002?auto=format&fit=crop&w=500&q=80', 'name': 'BBQ Chicken Pizza', 'price': 18.50, 'desc': 'Smoked gouda, grilled chicken, red onions, cilantro, BBQ sauce.', 'cal': 910}
        ]
    },
    {
        'id': 'bowls',
        'title': 'Healthy <span class=\"text-gradient\">Bowls</span>',
        'items': [
            {'img': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=500&q=80', 'name': 'Teriyaki Salmon Bowl', 'price': 21.00, 'desc': 'Grilled Atlantic salmon, jasmine rice, edamame, pickled ginger, sesame glaze.', 'cal': 540},
            {'img': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=500&q=80', 'name': 'Korean Beef Bibimbap', 'price': 19.00, 'desc': 'Marinated ribeye, sautéed vegetables, fried egg, gochujang sauce.', 'cal': 680},
            {'img': 'https://images.unsplash.com/photo-1543339308-43e59d6b73a6?auto=format&fit=crop&w=500&q=80', 'name': 'Vegan Buddha Bowl', 'price': 15.50, 'desc': 'Quinoa, roasted chickpeas, avocado, kale, tahini dressing.', 'cal': 420},
            {'img': 'https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=500&q=80', 'name': 'Chicken Fiesta Bowl', 'price': 16.50, 'desc': 'Grilled chicken, brown rice, black beans, corn salsa, guacamole.', 'cal': 590},
            {'img': 'https://images.unsplash.com/photo-1548943487-a2e4e43b4859?auto=format&fit=crop&w=500&q=80', 'name': 'Falafel Hummus Bowl', 'price': 14.50, 'desc': 'Crispy falafel, creamy hummus, tabbouleh, mixed greens, tahini.', 'cal': 520},
            {'img': 'https://images.unsplash.com/photo-1559058789-672da06263d8?auto=format&fit=crop&w=500&q=80', 'name': 'Ahi Tuna Poke Bowl', 'price': 22.00, 'desc': 'Fresh ahi tuna, sushi rice, seaweed salad, cucumber, ponzu dressing.', 'cal': 480}
        ]
    },
    {
        'id': 'desserts',
        'title': 'Sweet <span class=\"text-gradient\">Endings</span>',
        'items': [
            {'img': 'https://images.unsplash.com/photo-1551024506-0bccd828d307?auto=format&fit=crop&w=500&q=80', 'name': 'Molten Lava Cake', 'price': 9.00, 'desc': 'Warm dark chocolate cake with a gooey center, served with vanilla bean gelato.', 'cal': 850},
            {'img': 'https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=500&q=80', 'name': 'Classic New York Cheesecake', 'price': 8.50, 'desc': 'Rich and creamy cheesecake with a graham cracker crust and fresh strawberry compote.', 'cal': 720},
            {'img': 'https://images.unsplash.com/photo-1563805042-7684c8a9e9ce?auto=format&fit=crop&w=500&q=80', 'name': 'Artisan Macarons', 'price': 12.00, 'desc': 'Assortment of 6 hand-crafted macarons in seasonal flavors.', 'cal': 450},
            {'img': 'https://images.unsplash.com/photo-1509482560494-4126f8225994?auto=format&fit=crop&w=500&q=80', 'name': 'Tiramisu Classico', 'price': 10.00, 'desc': 'Espresso-soaked ladyfingers, mascarpone cream, dusted with premium cocoa.', 'cal': 680},
            {'img': 'https://images.unsplash.com/photo-1495147466023-ac5c588e2e94?auto=format&fit=crop&w=500&q=80', 'name': 'Lemon Meringue Tart', 'price': 9.50, 'desc': 'Tangy lemon curd in a butter crust topped with toasted Italian meringue.', 'cal': 510},
            {'img': 'https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?auto=format&fit=crop&w=500&q=80', 'name': 'Decadent Brownie Sundae', 'price': 11.00, 'desc': 'Fudge brownie, two scoops of vanilla ice cream, hot fudge, whipped cream.', 'cal': 950}
        ]
    },
    {
        'id': 'beverages',
        'title': 'Refreshing <span class=\"text-gradient\">Beverages</span>',
        'items': [
            {'img': 'https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?auto=format&fit=crop&w=500&q=80', 'name': 'Artisan Matcha Latte', 'price': 6.50, 'desc': 'Ceremonial grade matcha, oat milk, touch of agave.', 'cal': 180},
            {'img': 'https://images.unsplash.com/photo-1556881286-fc6915169721?auto=format&fit=crop&w=500&q=80', 'name': 'Cold Brew Iced Coffee', 'price': 5.00, 'desc': '18-hour steeped single origin coffee over ice.', 'cal': 10},
            {'img': 'https://images.unsplash.com/photo-1544145945-f90425340c7e?auto=format&fit=crop&w=500&q=80', 'name': 'Fresh Squeezed Lemonade', 'price': 4.50, 'desc': 'Classic lemonade made with organic lemons and cane sugar.', 'cal': 150},
            {'img': 'https://images.unsplash.com/photo-1497534446932-c925b458314e?auto=format&fit=crop&w=500&q=80', 'name': 'Tropical Mango Smoothie', 'price': 7.50, 'desc': 'Mango, pineapple, coconut water, and a hint of mint blended to perfection.', 'cal': 220},
            {'img': 'https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&w=500&q=80', 'name': 'Sparkling Berry Fizz', 'price': 5.50, 'desc': 'Mixed berry puree topped with sparkling water and fresh lime.', 'cal': 80},
            {'img': 'https://images.unsplash.com/photo-1541167760496-1628856ab772?auto=format&fit=crop&w=500&q=80', 'name': 'Classic Cappuccino', 'price': 5.50, 'desc': 'Rich espresso topped with a deep layer of foamed milk.', 'cal': 120}
        ]
    }
]

generated_html = ""
item_counter = 1

for cat in categories:
    generated_html += f'''
            <div class=\"menu-category\" data-category=\"{cat['id']}\">
                <div class=\"menu-section-title\" data-aos=\"fade-right\">
                    <h2>{cat['title']}</h2>
                </div>
                <div class=\"meal-grid\">'''
    
    for idx, item in enumerate(cat['items']):
        badge_html = ''
        if 'badge' in item:
            badge_color = item.get("badge_color", "var(--primary)")
            text_color = item.get("text_color", "#000")
            badge_html = f'<div class=\"offer-badge\" style=\"background: {badge_color}; color: {text_color};\">{item["badge"]}</div>'
            
        name_escaped = item['name'].replace("'", "\\'")
        desc_escaped = item['desc'].replace("'", "\\'")
        generated_html += f'''
                    <div class=\"meal-card\" data-aos=\"fade-up\" data-aos-delay=\"{(idx%3) * 100}\">
                        {badge_html}
                        <img src=\"{item['img']}\" alt=\"{item['name']}\" class=\"meal-img\">
                        <div class=\"meal-info\">
                            <div style=\"display: flex; justify-content: space-between;\">
                                <h3>{item['name']}</h3>
                                <span style=\"color: var(--primary); font-weight: 700;\">${item['price']:.2f}</span>
                            </div>
                            <p style=\"color: var(--text-muted); font-size: 0.85rem; margin: 10px 0;\">{item['desc']}</p>
                            <div style=\"display: flex; justify-content: space-between; align-items: center; margin-top: 15px;\">
                                <span style=\"font-size: 0.8rem; color: var(--text-muted);\"><i class=\"fas fa-fire\"></i> {item['cal']} kcal</span>
                                <button class=\"btn btn-primary\" style=\"padding: 8px 15px; font-size: 0.8rem;\" onclick=\"addToCart({item_counter}, '{name_escaped}', {item['price']}, '{item['img']}', '{desc_escaped}')\">Add to Cart</button>
                            </div>
                        </div>
                    </div>'''
        item_counter += 1
        
    generated_html += '''
                </div>
            </div>'''

# Replace the specific section
final_content = pre_content + generated_html + post_content

# We want the script at the bottom to remain clean
new_script = '''<script>
        // Smooth filter logic implementation
        const filterBtns = document.querySelectorAll('.filter-btn');
        const categories = document.querySelectorAll('.menu-category');

        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class from all buttons
                filterBtns.forEach(b => b.classList.remove('active'));
                
                // Add active class to clicked button
                btn.classList.add('active');
                
                const filter = btn.getAttribute('data-filter');
                
                categories.forEach(category => {
                    // Start fade out
                    category.style.opacity = '0';
                    category.style.transform = 'scale(0.98)';
                    
                    setTimeout(() => {
                        if (filter === 'all' || category.getAttribute('data-category') === filter) {
                            category.style.display = 'block';
                            // Short delay before fade in to ensure layout triggers
                            setTimeout(() => {
                                category.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
                                category.style.opacity = '1';
                                category.style.transform = 'scale(1)';
                            }, 50);
                        } else {
                            category.style.display = 'none';
                        }
                    }, 300); // Wait for fade out to complete
                });
            });
        });
        
        // Initial setup for transitions
        categories.forEach(category => {
            category.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            category.style.opacity = '1';
            category.style.transform = 'scale(1)';
        });
    </script>'''

# Replace whatever script is there with the updated one
final_content = re.sub(r'<script>\s*// Smooth filter.*?</div>\s*</div>', '', final_content, flags=re.DOTALL) # cleanup old bad script if it exists
final_content = re.sub(r'<script>\s*// Simple filter logic.*?</script>', '', final_content, flags=re.DOTALL)
final_content = re.sub(r'<script>\s*// Smooth filter logic implementation.*?</script>', new_script, final_content, flags=re.DOTALL)

with open('menu.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Menu HTML successfully rebuilt with exactly 6 items per category!")
