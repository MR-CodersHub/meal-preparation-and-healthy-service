import re

with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the filter tabs to include data-filter
filter_tabs = '''<div class="filter-tabs">
                <button class="filter-btn active" data-filter="all">All Items</button>
                <button class="filter-btn" data-filter="breakfast">Breakfast</button>
                <button class="filter-btn" data-filter="lunch">Lunch Specials</button>
                <button class="filter-btn" data-filter="burgers">Gourmet Burgers</button>
                <button class="filter-btn" data-filter="pizza">Artisan Pizza</button>
                <button class="filter-btn" data-filter="bowls">Healthy Bowls</button>
                <button class="filter-btn" data-filter="desserts">Desserts</button>
                <button class="filter-btn" data-filter="beverages">Beverages</button>
            </div>'''
            
content = re.sub(r'<div class="filter-tabs">.*?</div>', filter_tabs, content, flags=re.DOTALL)

# Wrap existing categories in divs
content = content.replace('<!-- Category: Burgers -->', '<div class="menu-category" data-category="burgers">\n            <!-- Category: Burgers -->')
content = content.replace('<!-- Category: Rice Bowls -->', '</div>\n\n            <div class="menu-category" data-category="bowls">\n            <!-- Category: Rice Bowls -->')
content = content.replace('<!-- Category: Desserts -->', '</div>\n\n            <div class="menu-category" data-category="desserts">\n            <!-- Category: Desserts -->')
content = content.replace('<!-- App Banner -->', '</div>\n\n    <!-- App Banner -->')

# Generate new sections
breakfast_html = '''
            <div class="menu-category" data-category="breakfast" style="display: none;">
                <div class="menu-section-title" data-aos="fade-right">
                    <h2>Morning <span class="text-gradient">Classics</span></h2>
                </div>
                <div class="meal-grid">
                    <div class="meal-card">
                        <img src="https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=500&q=80" alt="Breakfast" class="meal-img">
                        <div class="meal-info">
                            <div style="display: flex; justify-content: space-between;">
                                <h3>Avocado Toast Deluxe</h3>
                                <span style="color: var(--primary); font-weight: 700;">$12.50</span>
                            </div>
                            <p style="color: var(--text-muted); font-size: 0.85rem; margin: 10px 0;">Sourdough, smashed avocado, poached eggs, microgreens, chili flakes.</p>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
                                <span style="font-size: 0.8rem; color: var(--text-muted);"><i class="fas fa-fire"></i> 450 kcal</span>
                                <button class="btn btn-primary" style="padding: 8px 15px; font-size: 0.8rem;" onclick="addToCart(11, 'Avocado Toast', 12.50, 'https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=500&q=80', 'Sourdough, smashed avocado, poached eggs, microgreens, chili flakes.')">Add to Cart</button>
                            </div>
                        </div>
                    </div>
                    <div class="meal-card">
                        <img src="https://images.unsplash.com/photo-1525648199074-cee30ba79a4a?auto=format&fit=crop&w=500&q=80" alt="Breakfast" class="meal-img">
                        <div class="meal-info">
                            <div style="display: flex; justify-content: space-between;">
                                <h3>Berry Protein Pancakes</h3>
                                <span style="color: var(--primary); font-weight: 700;">$14.00</span>
                            </div>
                            <p style="color: var(--text-muted); font-size: 0.85rem; margin: 10px 0;">Three fluffy oat pancakes, mixed berries, maple syrup, chia seeds.</p>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
                                <span style="font-size: 0.8rem; color: var(--text-muted);"><i class="fas fa-fire"></i> 520 kcal</span>
                                <button class="btn btn-primary" style="padding: 8px 15px; font-size: 0.8rem;" onclick="addToCart(12, 'Berry Protein Pancakes', 14.00, 'https://images.unsplash.com/photo-1525648199074-cee30ba79a4a?auto=format&fit=crop&w=500&q=80', 'Three fluffy oat pancakes, mixed berries, maple syrup, chia seeds.')">Add to Cart</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
'''

lunch_html = '''
            <div class="menu-category" data-category="lunch" style="display: none;">
                <div class="menu-section-title" data-aos="fade-right">
                    <h2>Lunch <span class="text-gradient">Specials</span></h2>
                </div>
                <div class="meal-grid">
                    <div class="meal-card">
                        <div class="offer-badge" style="background: var(--primary); color: #000;">POPULAR</div>
                        <img src="https://images.unsplash.com/photo-1512152272829-e3139592d56f?auto=format&fit=crop&w=500&q=80" alt="Lunch" class="meal-img">
                        <div class="meal-info">
                            <div style="display: flex; justify-content: space-between;">
                                <h3>Grilled Chicken Wrap</h3>
                                <span style="color: var(--primary); font-weight: 700;">$11.50</span>
                            </div>
                            <p style="color: var(--text-muted); font-size: 0.85rem; margin: 10px 0;">Whole wheat wrap, grilled chicken, romaine, Caesar dressing.</p>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
                                <span style="font-size: 0.8rem; color: var(--text-muted);"><i class="fas fa-fire"></i> 480 kcal</span>
                                <button class="btn btn-primary" style="padding: 8px 15px; font-size: 0.8rem;" onclick="addToCart(13, 'Grilled Chicken Wrap', 11.50, 'https://images.unsplash.com/photo-1512152272829-e3139592d56f?auto=format&fit=crop&w=500&q=80', 'Whole wheat wrap, grilled chicken, romaine, Caesar dressing.')">Add to Cart</button>
                            </div>
                        </div>
                    </div>
                    <div class="meal-card">
                        <img src="https://images.unsplash.com/photo-1564834724105-918b73d1b9e0?auto=format&fit=crop&w=500&q=80" alt="Lunch" class="meal-img">
                        <div class="meal-info">
                            <div style="display: flex; justify-content: space-between;">
                                <h3>Quinoa & Roasted Veg Salad</h3>
                                <span style="color: var(--primary); font-weight: 700;">$13.00</span>
                            </div>
                            <p style="color: var(--text-muted); font-size: 0.85rem; margin: 10px 0;">Mixed greens, roasted butternut squash, quinoa, balsamic vinaigrette.</p>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
                                <span style="font-size: 0.8rem; color: var(--text-muted);"><i class="fas fa-fire"></i> 350 kcal</span>
                                <button class="btn btn-primary" style="padding: 8px 15px; font-size: 0.8rem;" onclick="addToCart(14, 'Quinoa Veg Salad', 13.00, 'https://images.unsplash.com/photo-1564834724105-918b73d1b9e0?auto=format&fit=crop&w=500&q=80', 'Mixed greens, roasted butternut squash, quinoa, balsamic vinaigrette.')">Add to Cart</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
'''

pizza_html = '''
            <div class="menu-category" data-category="pizza" style="display: none;">
                <div class="menu-section-title" data-aos="fade-right">
                    <h2>Artisan <span class="text-gradient">Pizza</span></h2>
                </div>
                <div class="meal-grid">
                    <div class="meal-card">
                        <div class="offer-badge" style="background: #ff4d4d; color: #fff;">CHEF'S CHOICE</div>
                        <img src="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=500&q=80" alt="Pizza" class="meal-img">
                        <div class="meal-info">
                            <div style="display: flex; justify-content: space-between;">
                                <h3>Margherita Classico</h3>
                                <span style="color: var(--primary); font-weight: 700;">$16.00</span>
                            </div>
                            <p style="color: var(--text-muted); font-size: 0.85rem; margin: 10px 0;">San Marzano tomatoes, fresh mozzarella, basil, extra virgin olive oil.</p>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
                                <span style="font-size: 0.8rem; color: var(--text-muted);"><i class="fas fa-fire"></i> 850 kcal</span>
                                <button class="btn btn-primary" style="padding: 8px 15px; font-size: 0.8rem;" onclick="addToCart(15, 'Margherita Classico', 16.00, 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=500&q=80', 'San Marzano tomatoes, fresh mozzarella, basil, extra virgin olive oil.')">Add to Cart</button>
                            </div>
                        </div>
                    </div>
                    <div class="meal-card">
                        <img src="https://images.unsplash.com/photo-1590947132387-155cc02f3212?auto=format&fit=crop&w=500&q=80" alt="Pizza" class="meal-img">
                        <div class="meal-info">
                            <div style="display: flex; justify-content: space-between;">
                                <h3>Truffle Mushroom Pizza</h3>
                                <span style="color: var(--primary); font-weight: 700;">$19.50</span>
                            </div>
                            <p style="color: var(--text-muted); font-size: 0.85rem; margin: 10px 0;">Wild mushrooms, truffle cream, thyme, fontina cheese.</p>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
                                <span style="font-size: 0.8rem; color: var(--text-muted);"><i class="fas fa-fire"></i> 920 kcal</span>
                                <button class="btn btn-primary" style="padding: 8px 15px; font-size: 0.8rem;" onclick="addToCart(16, 'Truffle Mushroom Pizza', 19.50, 'https://images.unsplash.com/photo-1590947132387-155cc02f3212?auto=format&fit=crop&w=500&q=80', 'Wild mushrooms, truffle cream, thyme, fontina cheese.')">Add to Cart</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
'''

beverages_html = '''
            <div class="menu-category" data-category="beverages" style="display: none;">
                <div class="menu-section-title" data-aos="fade-right">
                    <h2>Refreshing <span class="text-gradient">Beverages</span></h2>
                </div>
                <div class="meal-grid">
                    <div class="meal-card">
                        <img src="https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?auto=format&fit=crop&w=500&q=80" alt="Beverage" class="meal-img">
                        <div class="meal-info">
                            <div style="display: flex; justify-content: space-between;">
                                <h3>Artisan Matcha Latte</h3>
                                <span style="color: var(--primary); font-weight: 700;">$6.50</span>
                            </div>
                            <p style="color: var(--text-muted); font-size: 0.85rem; margin: 10px 0;">Ceremonial grade matcha, oat milk, touch of agave.</p>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
                                <span style="font-size: 0.8rem; color: var(--text-muted);"><i class="fas fa-fire"></i> 180 kcal</span>
                                <button class="btn btn-primary" style="padding: 8px 15px; font-size: 0.8rem;" onclick="addToCart(17, 'Artisan Matcha Latte', 6.50, 'https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?auto=format&fit=crop&w=500&q=80', 'Ceremonial grade matcha, oat milk, touch of agave.')">Add to Cart</button>
                            </div>
                        </div>
                    </div>
                    <div class="meal-card">
                        <img src="https://images.unsplash.com/photo-1556881286-fc6915169721?auto=format&fit=crop&w=500&q=80" alt="Beverage" class="meal-img">
                        <div class="meal-info">
                            <div style="display: flex; justify-content: space-between;">
                                <h3>Cold Brew Iced Coffee</h3>
                                <span style="color: var(--primary); font-weight: 700;">$5.00</span>
                            </div>
                            <p style="color: var(--text-muted); font-size: 0.85rem; margin: 10px 0;">18-hour steeped single origin coffee over ice.</p>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
                                <span style="font-size: 0.8rem; color: var(--text-muted);"><i class="fas fa-fire"></i> 10 kcal</span>
                                <button class="btn btn-primary" style="padding: 8px 15px; font-size: 0.8rem;" onclick="addToCart(18, 'Cold Brew Iced Coffee', 5.00, 'https://images.unsplash.com/photo-1556881286-fc6915169721?auto=format&fit=crop&w=500&q=80', '18-hour steeped single origin coffee over ice.')">Add to Cart</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
'''

content = content.replace('<div class="menu-category" data-category="burgers">', breakfast_html + lunch_html + '<div class="menu-category" data-category="burgers">')
content = content.replace('<div class="menu-category" data-category="bowls">', pizza_html + '<div class="menu-category" data-category="bowls">')
content = content.replace('<div class="menu-category" data-category="desserts">', '<div class="menu-category" data-category="desserts">')
content = content.replace('</div>\n\n    <!-- App Banner -->', beverages_html + '</div>\n\n    <!-- App Banner -->')

# Update script to perform the filtering with fade transitions
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
                    
                    setTimeout(() => {
                        if (filter === 'all' || category.getAttribute('data-category') === filter) {
                            category.style.display = 'block';
                            // Short delay before fade in to ensure layout triggers
                            setTimeout(() => {
                                category.style.transition = 'opacity 0.4s ease';
                                category.style.opacity = '1';
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
            category.style.transition = 'opacity 0.4s ease';
            category.style.opacity = '1';
        });
    </script>'''

content = re.sub(r'<script>\s*// Simple filter logic simulation.*?</script>', new_script, content, flags=re.DOTALL)

with open('menu.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Menu HTML successfully updated.")
