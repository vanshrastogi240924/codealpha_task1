<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ShopEasy - Online Shopping</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        .cart-badge {
            position: absolute;
            top: -8px;
            right: -8px;
        }
        .search-bar:focus {
            outline: none;
            box-shadow: 0 0 0 2px #f59e0b;
        }
    </style>
</head>
<body class="bg-gray-50 font-sans">
    <!-- Navigation Bar -->
    <nav class="bg-orange-500 text-white shadow-md sticky top-0 z-50">
        <div class="container mx-auto px-4 py-3 flex items-center justify-between">
            <div class="flex items-center space-x-1">
                <img src="https://placehold.co/40x40" alt="ShopEasy logo with orange and white colors and shopping cart icon" 
                     class="h-10 w-10 rounded-full border-2 border-white">
                <span class="text-2xl font-bold">ShopEasy</span>
            </div>
            
            <div class="flex-1 max-w-2xl mx-4">
                <div class="relative">
                    <input type="text" placeholder="Search for products..." 
                           class="w-full py-2 px-4 rounded-lg text-gray-800 focus:ring-2 focus:ring-orange-300">
                    <button class="absolute right-0 top-0 h-full px-4 bg-orange-600 rounded-r-lg hover:bg-orange-700">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                        </svg>
                    </button>
                </div>
            </div>
            
            <div class="flex items-center space-x-6">
                <a href="#" class="hover:text-orange-200 flex flex-col items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                    </svg>
                    <span class="text-xs">Profile</span>
                </a>
                <a href="#" class="hover:text-orange-200 flex flex-col items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                    </svg>
                    <span class="text-xs">Wishlist</span>
                </a>
                <div class="relative">
                    <a href="#" class="hover:text-orange-200 flex flex-col items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                        </svg>
                        <span class="text-xs">Cart</span>
                    </a>
                    <span class="cart-badge bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">0</span>
                </div>
            </div>
        </div>
    </nav>

    <!-- Categories Bar -->
    <div class="bg-white shadow-sm">
        <div class="container mx-auto px-4 py-2 overflow-x-auto">
            <div class="flex space-x-8">
                <a href="#" class="whitespace-nowrap hover:text-orange-500">Electronics</a>
                <a href="#" class="whitespace-nowrap hover:text-orange-500">Fashion</a>
                <a href="#" class="whitespace-nowrap hover:text-orange-500">Home & Kitchen</a>
                <a href="#" class="whitespace-nowrap hover:text-orange-500">Beauty</a>
                <a href="#" class="whitespace-nowrap hover:text-orange-500">Toys</a>
                <a href="#" class="whitespace-nowrap hover:text-orange-500">Sports</a>
                <a href="#" class="whitespace-nowrap hover:text-orange-500">Grocery</a>
                <a href="#" class="whitespace-nowrap hover:text-orange-500">Accessories</a>
            </div>
        </div>
    </div>

    <!-- Main Content -->
    <main class="container mx-auto px-4 py-8">
        <!-- Hero Banner -->
        <div class="mb-8 rounded-xl overflow-hidden">
            <img src="/projectimg6.jpeg" alt="E-commerce sale banner showing various product deals with discount percentages" 
                 class="w-full h-auto object-cover">
        </div>

        <h2 class="text-2xl font-bold mb-6">Trending Products</h2>
        
        <!-- Products Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <!-- Product 1 -->
            <div class="product-card bg-white rounded-lg overflow-hidden shadow-md transition-transform duration-300">
                <div class="h-48 bg-gray-100 relative">
                    <img src="projectimg4.avif" alt="Latest smartphone model with AMOLED display and triple camera setup" 
                         class="w-full h-full object-contain p-4">
                    <span class="absolute top-2 left-2 bg-red-500 text-white text-xs px-2 py-1 rounded">20% OFF</span>
                </div>
                <div class="p-4">
                    <h3 class="font-semibold text-lg mb-1">Smartphone X Pro</h3>
                    <p class="text-gray-600 text-sm mb-2">6.7" AMOLED, 256GB Storage</p>
                    <div class="flex items-center mb-2">
                        <div class="flex text-yellow-400">
                            ★★★★☆
                        </div>
                        <span class="text-gray-500 text-xs ml-1">(1,234)</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-lg font-bold text-gray-900">₹34,999</p>
                            <p class="text-sm text-gray-500 line-through">₹42,999</p>
                        </div>
                        <button class="add-to-cart bg-orange-500 text-white px-3 py-1 rounded-full text-sm hover:bg-orange-600">
                            Add to Cart
                        </button>
                    </div>
                </div>
            </div>

            <!-- Product 2 -->
            <div class="product-card bg-white rounded-lg overflow-hidden shadow-md transition-transform duration-300">
                <div class="h-48 bg-gray-100 relative">
                    <img src="projectimg3.jpeg" alt="Wireless noise-cancelling headphones in black with silver accents" 
                         class="w-full h-full object-contain p-4">
                </div>
                <div class="p-4">
                    <h3 class="font-semibold text-lg mb-1">Wireless Headphones</h3>
                    <p class="text-gray-600 text-sm mb-2">Noise Cancelling, 30hr Battery</p>
                    <div class="flex items-center mb-2">
                        <div class="flex text-yellow-400">
                            ★★★★★
                        </div>
                        <span class="text-gray-500 text-xs ml-1">(876)</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-lg font-bold text-gray-900">₹9,499</p>
                            <p class="text-sm text-gray-500 line-through">₹10,499</p>
                        </div>
                        <button class="add-to-cart bg-orange-500 text-white px-3 py-1 rounded-full text-sm hover:bg-orange-600">
                            Add to Cart
                        </button>
                    </div>
                </div>
            </div>

            <!-- Product 3 -->
            <div class="product-card bg-white rounded-lg overflow-hidden shadow-md transition-transform duration-300">
                <div class="h-48 bg-gray-100 relative">
                    <img src="projectimg.2.jpeg" alt="Modern smartwatch with fitness tracking and touchscreen display" 
                         class="w-full h-full object-contain p-4">
                    <span class="absolute top-2 left-2 bg-green-500 text-white text-xs px-2 py-1 rounded">NEW</span>
                </div>
                <div class="p-4">
                    <h3 class="font-semibold text-lg mb-1">Smart Watch Pro</h3>
                    <p class="text-gray-600 text-sm mb-2">1.4" AMOLED, Heart Rate Monitor</p>
                    <div class="flex items-center mb-2">
                        <div class="flex text-yellow-400">
                            ★★★★☆
                        </div>
                        <span class="text-gray-500 text-xs ml-1">(567)</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-lg font-bold text-gray-900">₹16,999</p>
                            <p class="text-sm text-gray-500 line-through">₹28,499</p>
                        </div>
                        <button class="add-to-cart bg-orange-500 text-white px-3 py-1 rounded-full text-sm hover:bg-orange-600">
                            Add to Cart
                        </button>
                    </div>
                </div>
            </div>

            <!-- Product 4 -->
            <div class="product-card bg-white rounded-lg overflow-hidden shadow-md transition-transform duration-300">
                <div class="h-48 bg-gray-100 relative">
                    <img src="projectimg.jpeg" alt="Bluetooth speaker with premium design and long battery life" 
                         class="w-full h-full object-contain p-4">
                </div>
                <div class="p-4">
                    <h3 class="font-semibold text-lg mb-1">Bluetooth Speaker</h3>
                    <p class="text-gray-600 text-sm mb-2">20W Stereo Sound, IPX7 Waterproof</p>
                    <div class="flex items-center mb-2">
                        <div class="flex text-yellow-400">
                            ★★★★☆
                        </div>
                        <span class="text-gray-500 text-xs ml-1">(432)</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-lg font-bold text-gray-900">₹5,499</p>
                            <p class="text-sm text-gray-500 line-through">₹8,499</p>
                        </div>
                        <button class="add-to-cart bg-orange-500 text-white px-3 py-1 rounded-full text-sm hover:bg-orange-600">
                            Add to Cart
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->  
    <footer class="bg-gray-800 text-white py-8">
        <div class="container mx-auto px-4">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
                <div>
                    <h3 class="text-lg font-semibold mb-4">ShopEasy</h3>
                    <p class="text-gray-400 text-sm">Your one-stop shop for all your needs with great deals and fast delivery.</p>
                </div>
                <div>
                    <h3 class="text-lg font-semibold mb-4">Quick Links</h3>
                    <ul class="space-y-2 text-sm text-gray-400">
                        <li><a href="#" class="hover:text-white">Home</a></li>
                        <li><a href="#" class="hover:text-white">About Us</a></li>
                        <li><a href="#" class="hover:text-white">Categories</a></li>
                        <li><a href="#" class="hover:text-white">Contact</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-semibold mb-4">Customer Service</h3>
                    <ul class="space-y-2 text-sm text-gray-400">
                        <li><a href="#" class="hover:text-white">My Account</a></li>
                        <li><a href="#" class="hover:text-white">Order Tracking</a></li>
                        <li><a href="#" class="hover:text-white">Returns Policy</a></li>
                        <li><a href="#" class="hover:text-white">FAQs</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-semibold mb-4">Newsletter</h3>
                    <p class="text-gray-400 text-sm mb-2">Subscribe for the latest deals and updates.</p>
                    <div class="flex">
                        <input type="email" placeholder="Your email" 
                               class="bg-gray-700 text-white px-3 py-2 rounded-l-lg text-sm w-full">
                        <button class="bg-orange-500 text-white px-4 py-2 rounded-r-lg text-sm hover:bg-orange-600">
                            Subscribe
                        </button>
                    </div>
                </div>
            </div>
            <div class="border-t border-gray-700 mt-8 pt-6 text-center text-gray-400 text-sm">
                <p>© 2023 ShopEasy. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        // Shopping cart functionality
        let cartCount = 0;
        const cartBadge = document.querySelector('.cart-badge');
        const addToCartButtons = document.querySelectorAll('.add-to-cart');
        
        addToCartButtons.forEach(button => {
            button.addEventListener('click', () => {
                cartCount++;
                cartBadge.textContent = cartCount;
                
                // Add animation
                cartBadge.classList.add('animate-bounce');
                setTimeout(() => {
                    cartBadge.classList.remove('animate-bounce');
                }, 800);
                
                // Show added to cart message
                const productName = button.closest('.product-card').querySelector('h3').textContent;
                alert('${productName} added to cart!');
            });
        });

        // Search functionality
        const searchInput = document.querySelector('input[type="text"]');
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                const searchTerm = searchInput.value.trim();
                if (searchTerm) {
                    alert('Searching for: ${searchTerm}');
                    // In a real app, you would redirect or filter products
                }
            }
        });
    </script>
</body>
</html>