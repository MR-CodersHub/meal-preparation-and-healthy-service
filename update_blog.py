import re

with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update the blog filters
new_filters = '''<div class="blog-filters" data-aos="fade-up">
            <div class="blog-filter active" data-filter="all">All Stories</div>
            <div class="blog-filter" data-filter="chef-tips">Chef Tips</div>
            <div class="blog-filter" data-filter="healthy-eating">Healthy Eating</div>
            <div class="blog-filter" data-filter="cloud-tech">Cloud Kitchen Tech</div>
            <div class="blog-filter" data-filter="food-trends">Food Trends</div>
        </div>'''

content = re.sub(r'<div class="blog-filters".*?</div>\s*</div>', new_filters, content, flags=re.DOTALL)

# Replace the blog grid content completely
new_blog_grid = '''<!-- Blog Grid -->
        <div class="blog-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; margin-bottom: 100px;">
            <!-- Blog 1 -->
            <div class="blog-card" data-category="chef-tips" data-aos="fade-up">
                <img src="https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&w=600&q=80" class="blog-img">
                <div class="blog-content">
                    <div class="blog-meta">
                        <span><i class="fas fa-calendar"></i> May 15, 2026</span>
                        <span><i class="fas fa-user"></i> Chef Marcus</span>
                    </div>
                    <h4>The Art of Searing Wagyu: Tips from Our Executive Chef</h4>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 15px;">Discover the secrets to achieving the perfect crust and maintaining the buttery texture of premium wagyu beef.</p>
                    <a href="blog-details.html" style="color: var(--primary); display: inline-block; margin-top: 20px; font-weight: 600;">Read More <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
            <!-- Blog 2 -->
            <div class="blog-card" data-category="healthy-eating" data-aos="fade-up" data-aos-delay="100">
                <img src="https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=600&q=80" class="blog-img">
                <div class="blog-content">
                    <div class="blog-meta">
                        <span><i class="fas fa-calendar"></i> May 12, 2026</span>
                        <span><i class="fas fa-tag"></i> Healthy Eating</span>
                    </div>
                    <h4>Macro-Balancing: Why Your Lunch Choice Matters for Productivity</h4>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 15px;">How a balanced ratio of complex carbs and lean protein can prevent the dreaded afternoon slump.</p>
                    <a href="blog-details.html" style="color: var(--primary); display: inline-block; margin-top: 20px; font-weight: 600;">Read More <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
            <!-- Blog 3 -->
            <div class="blog-card" data-category="cloud-tech" data-aos="fade-up" data-aos-delay="200">
                <img src="https://images.unsplash.com/photo-1581299894007-aaa50297cf16?auto=format&fit=crop&w=600&q=80" class="blog-img">
                <div class="blog-content">
                    <div class="blog-meta">
                        <span><i class="fas fa-calendar"></i> May 10, 2026</span>
                        <span><i class="fas fa-microchip"></i> Future Food</span>
                    </div>
                    <h4>Inside the Cloud Kitchen: How AI is Optimizing Your Delivery</h4>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 15px;">A look behind the scenes at the technology that ensures your food arrives hot and fresh every single time.</p>
                    <a href="blog-details.html" style="color: var(--primary); display: inline-block; margin-top: 20px; font-weight: 600;">Read More <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
            <!-- Blog 4 -->
            <div class="blog-card" data-category="food-trends" data-aos="fade-up">
                <img src="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=600&q=80" class="blog-img">
                <div class="blog-content">
                    <div class="blog-meta">
                        <span><i class="fas fa-calendar"></i> May 08, 2026</span>
                        <span><i class="fas fa-chart-line"></i> Industry Insights</span>
                    </div>
                    <h4>The Rise of Plant-Based Ghost Kitchens</h4>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 15px;">Exploring the massive shift towards sustainability and how ghost kitchens are leading the vegan revolution.</p>
                    <a href="blog-details.html" style="color: var(--primary); display: inline-block; margin-top: 20px; font-weight: 600;">Read More <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
            <!-- Blog 5 -->
            <div class="blog-card" data-category="chef-tips" data-aos="fade-up" data-aos-delay="100">
                <img src="https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=600&q=80" class="blog-img">
                <div class="blog-content">
                    <div class="blog-meta">
                        <span><i class="fas fa-calendar"></i> May 05, 2026</span>
                        <span><i class="fas fa-user"></i> Chef Sarah</span>
                    </div>
                    <h4>5 Essential Knives Every Home Chef Needs</h4>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 15px;">Elevate your home cooking with these fundamental tools of the trade used by professional chefs.</p>
                    <a href="blog-details.html" style="color: var(--primary); display: inline-block; margin-top: 20px; font-weight: 600;">Read More <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
            <!-- Blog 6 -->
            <div class="blog-card" data-category="healthy-eating" data-aos="fade-up" data-aos-delay="200">
                <img src="https://images.unsplash.com/photo-1498837167922-41c53bbf0e41?auto=format&fit=crop&w=600&q=80" class="blog-img">
                <div class="blog-content">
                    <div class="blog-meta">
                        <span><i class="fas fa-calendar"></i> May 02, 2026</span>
                        <span><i class="fas fa-apple-alt"></i> Nutrition</span>
                    </div>
                    <h4>Superfoods of 2026: What's Next in Nutrition?</h4>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 15px;">From ancient grains to deep-sea kelp, discover the ingredients that are taking the wellness world by storm.</p>
                    <a href="blog-details.html" style="color: var(--primary); display: inline-block; margin-top: 20px; font-weight: 600;">Read More <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
        </div>'''

content = re.sub(r'<!-- Blog Grid -->.*?</div>\s*</div>', new_blog_grid, content, flags=re.DOTALL)

# Add the JS for filtering at the end of the body
filter_script = '''
    <script>
        // Smooth blog filtering logic
        document.addEventListener('DOMContentLoaded', () => {
            const filterBtns = document.querySelectorAll('.blog-filter');
            const blogCards = document.querySelectorAll('.blog-card');

            // Setup initial transition state
            blogCards.forEach(card => {
                card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
                card.style.opacity = '1';
                card.style.transform = 'scale(1)';
            });

            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    // Update active state
                    filterBtns.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');

                    const filter = btn.getAttribute('data-filter');

                    blogCards.forEach(card => {
                        // Start fade out
                        card.style.opacity = '0';
                        card.style.transform = 'scale(0.95)';

                        setTimeout(() => {
                            if (filter === 'all' || card.getAttribute('data-category') === filter) {
                                card.style.display = 'block';
                                // Slight delay to ensure display: block is registered before fading in
                                setTimeout(() => {
                                    card.style.opacity = '1';
                                    card.style.transform = 'scale(1)';
                                }, 50);
                            } else {
                                card.style.display = 'none';
                            }
                        }, 400); // Wait for transition to finish
                    });
                });
            });
        });
    </script>
</body>
</html>'''

content = re.sub(r'</body>\s*</html>', filter_script, content, flags=re.DOTALL)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Blog HTML successfully updated with filtering functionality.")
