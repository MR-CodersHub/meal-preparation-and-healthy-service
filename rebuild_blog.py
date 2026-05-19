import re

with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define 6 unique blog posts for each of the 4 categories
categories = [
    {
        'id': 'chef-tips',
        'posts': [
            {'img': 'https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&w=600&q=80', 'date': 'May 15, 2026', 'author': 'Chef Marcus', 'title': 'The Art of Searing Wagyu: Tips from Our Executive Chef', 'desc': 'Discover the secrets to achieving the perfect crust and maintaining the buttery texture of premium wagyu beef.'},
            {'img': 'https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=600&q=80', 'date': 'May 05, 2026', 'author': 'Chef Sarah', 'title': '5 Essential Knives Every Home Chef Needs', 'desc': 'Elevate your home cooking with these fundamental tools of the trade used by professional chefs.'},
            {'img': 'https://images.unsplash.com/photo-1581349485608-9469926a8e5e?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 28, 2026', 'author': 'Chef David', 'title': 'Mastering the French Mother Sauces', 'desc': 'A comprehensive guide to the five base sauces that form the foundation of classical cuisine.'},
            {'img': 'https://images.unsplash.com/photo-1600565193348-f74bd3c7ccdf?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 20, 2026', 'author': 'Chef Marcus', 'title': 'Plating Like a Pro: Visual Composition', 'desc': 'Learn how to transform a simple dish into a Michelin-worthy visual masterpiece using simple techniques.'},
            {'img': 'https://images.unsplash.com/photo-1507048331197-7d4ac70811cf?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 12, 2026', 'author': 'Chef Sarah', 'title': 'The Secret to Perfectly Caramelized Onions', 'desc': 'Patience is key. We break down the science and methodology behind deep, rich caramelization.'},
            {'img': 'https://images.unsplash.com/photo-1628294895950-9805252327bc?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 05, 2026', 'author': 'Chef David', 'title': 'Sous Vide for Beginners', 'desc': 'Everything you need to know to start cooking with clinical precision in your own kitchen.'}
        ]
    },
    {
        'id': 'healthy-eating',
        'posts': [
            {'img': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=600&q=80', 'date': 'May 12, 2026', 'tag': 'Healthy Eating', 'title': 'Macro-Balancing: Why Your Lunch Choice Matters', 'desc': 'How a balanced ratio of complex carbs and lean protein can prevent the dreaded afternoon slump.'},
            {'img': 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?auto=format&fit=crop&w=600&q=80', 'date': 'May 02, 2026', 'tag': 'Nutrition', 'title': "Superfoods of 2026: What's Next in Nutrition?", 'desc': 'From ancient grains to deep-sea kelp, discover the ingredients that are taking the wellness world by storm.'},
            {'img': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 25, 2026', 'tag': 'Wellness', 'title': 'The Gut-Brain Connection in Modern Diets', 'desc': 'Understanding how your daily food choices directly impact your mood and cognitive function.'},
            {'img': 'https://images.unsplash.com/photo-1494390248081-4e521a5940db?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 18, 2026', 'tag': 'Meal Prep', 'title': 'High-Protein Plant-Based Alternatives', 'desc': 'A breakdown of the most bioavailable plant proteins to fuel your workouts and recovery.'},
            {'img': 'https://images.unsplash.com/photo-1478144592103-25e218a04891?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 10, 2026', 'tag': 'Dietary Science', 'title': 'Intermittent Fasting: Myths vs Reality', 'desc': 'We dive into the latest clinical research on time-restricted eating and its metabolic benefits.'},
            {'img': 'https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 01, 2026', 'tag': 'Healthy Habits', 'title': 'Hydration Beyond Water', 'desc': 'Exploring electrolyte balance and water-rich foods that keep you hydrated more efficiently than just drinking water.'}
        ]
    },
    {
        'id': 'cloud-tech',
        'posts': [
            {'img': 'https://images.unsplash.com/photo-1581299894007-aaa50297cf16?auto=format&fit=crop&w=600&q=80', 'date': 'May 10, 2026', 'tag': 'Future Food', 'title': 'Inside the Cloud Kitchen: How AI Optimizes Delivery', 'desc': 'A look behind the scenes at the predictive algorithms that ensure your food arrives hot and fresh.'},
            {'img': 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=80', 'date': 'May 01, 2026', 'tag': 'Automation', 'title': 'The Role of Robotics in Prep Stations', 'desc': 'How collaborative robots are assisting our chefs with repetitive tasks, ensuring perfect consistency.'},
            {'img': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 22, 2026', 'tag': 'Data Science', 'title': 'Predicting Food Trends with Machine Learning', 'desc': 'How we analyze millions of data points to develop new menu items before they even become popular.'},
            {'img': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 15, 2026', 'tag': 'Logistics', 'title': 'Thermal Packaging 2.0: The End of Cold Fries', 'desc': 'Our proprietary packaging technology uses phase-change materials to maintain exact temperatures.'},
            {'img': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 08, 2026', 'tag': 'Smart Infrastructure', 'title': 'Building the Dark Kitchen of Tomorrow', 'desc': 'The architectural innovations required to handle 500+ gourmet orders an hour seamlessly.'},
            {'img': 'https://images.unsplash.com/photo-1526628953301-3e589a6a8b74?auto=format&fit=crop&w=600&q=80', 'date': 'Mar 28, 2026', 'tag': 'Analytics', 'title': 'Real-time Quality Control Monitoring', 'desc': 'Implementing IoT sensors across all cooking stations to guarantee clinical food safety standards.'}
        ]
    },
    {
        'id': 'food-trends',
        'posts': [
            {'img': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=600&q=80', 'date': 'May 08, 2026', 'tag': 'Industry Insights', 'title': 'The Rise of Plant-Based Ghost Kitchens', 'desc': 'Exploring the massive shift towards sustainability and how ghost kitchens are leading the vegan revolution.'},
            {'img': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 29, 2026', 'tag': 'Global Cuisine', 'title': 'Hyper-Regional Asian Street Food', 'desc': 'Why consumers are moving past generic labels and seeking highly specific, authentic regional dishes.'},
            {'img': 'https://images.unsplash.com/photo-1543352634-99a5d50ae78e?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 21, 2026', 'tag': 'Dining Habits', 'title': 'The Micro-Dining Experience at Home', 'desc': 'How the definition of a "restaurant quality meal" has evolved in the era of ultra-premium delivery.'},
            {'img': 'https://images.unsplash.com/photo-1482049016688-2d3e1b311543?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 14, 2026', 'tag': 'Flavor Profiles', 'title': 'Swicy: The Sweet & Spicy Flavor Taking Over', 'desc': 'Analyzing the explosive popularity of hot honey, chili crisp, and complex sweet-heat combinations.'},
            {'img': 'https://images.unsplash.com/photo-1514326640560-7d063ef2aed5?auto=format&fit=crop&w=600&q=80', 'date': 'Apr 06, 2026', 'tag': 'Consumer Data', 'title': 'Nostalgia as an Ingredient', 'desc': 'Why modernized comfort foods from the 90s are driving record sales across delivery platforms.'},
            {'img': 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?auto=format&fit=crop&w=600&q=80', 'date': 'Mar 30, 2026', 'tag': 'Sustainability', 'title': 'Upcycled Ingredients in High-End Dining', 'desc': 'How chefs are transforming food waste into premium, highly sought-after culinary experiences.'}
        ]
    }
]

generated_html = '''<!-- Blog Grid -->
        <div class="blog-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; margin-bottom: 100px;">'''

for cat in categories:
    for idx, post in enumerate(cat['posts']):
        icon_html = f'<span><i class="fas fa-user"></i> {post["author"]}</span>' if 'author' in post else f'<span><i class="fas fa-tag"></i> {post["tag"]}</span>'
        
        generated_html += f'''
            <div class="blog-card" data-category="{cat['id']}" data-aos="fade-up" data-aos-delay="{(idx%3) * 100}">
                <img src="{post['img']}" class="blog-img">
                <div class="blog-content">
                    <div class="blog-meta">
                        <span><i class="fas fa-calendar"></i> {post['date']}</span>
                        {icon_html}
                    </div>
                    <h4>{post['title']}</h4>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 15px;">{post['desc']}</p>
                    <a href="blog-details.html?id={cat['id']}-{idx}" style="color: var(--primary); display: inline-block; margin-top: 20px; font-weight: 600;">Read More <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>'''

generated_html += '''
        </div>'''

# Replace the grid in blog.html
content = re.sub(r'<!-- Blog Grid -->.*?</div>\s*</div>\s*(?=<!-- Featured Post -->)', generated_html + '\n    </div>\n\n    ', content, flags=re.DOTALL)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Blog HTML successfully updated with 6 cards per category.")
