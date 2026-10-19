<template>
  <div class="products-page">
    <div class="page-header">
      <h1 class="font-plaster fade-in-up">All Products</h1>
      <p class="fade-in-up tracking-wide">Explore our complete collection of premium intimate wellness products.</p>
    </div>

    <!-- Category Filter -->
    <div class="category-filter fade-in-up">
      <button
        v-for="cat in categories"
        :key="cat.id"
        class="cat-btn"
        :class="{ active: activeCategory === cat.id }"
        @click="setCategory(cat.id)"
      >
        {{ cat.name }}
      </button>
    </div>

    <!-- Sort -->
    <div class="sort-bar fade-in-up">
      <span class="result-count">{{ filteredProducts.length }} products</span>
      <select v-model="sortBy" class="sort-select">
        <option value="featured">Featured</option>
        <option value="price-low">Price: Low to High</option>
        <option value="price-high">Price: High to Low</option>
        <option value="name">Name A-Z</option>
      </select>
    </div>

    <!-- Product Grid -->
    <div class="product-grid">
      <div
        v-for="product in sortedProducts"
        :key="product.id"
        class="product-card fade-in-up"
      >
        <router-link :to="`/products/${product.id}`" class="product-link">
          <div class="product-image" :style="{ background: `radial-gradient(ellipse at 30% 30%, ${getProductColor(product)}50, ${getProductColor(product)}20 70%)` }">
            <div class="product-img-inner">
              <!-- Different shapes by category -->
              <svg v-if="product.category === 'wand'" viewBox="0 0 200 250" class="card-product-svg">
                <ellipse cx="100" cy="40" rx="40" ry="45" :fill="getProductColor(product)" opacity="0.6" />
                <path d="M75 78 Q72 115 78 170 Q100 185 122 170 Q128 115 125 78 Z"
                      :fill="getProductColor(product)" opacity="0.5" />
                <circle cx="100" cy="140" r="6" fill="rgba(255,255,255,0.4)" />
              </svg>
              <svg v-else-if="product.category === 'suction'" viewBox="0 0 200 250" class="card-product-svg">
                <ellipse cx="100" cy="130" rx="45" ry="80" :fill="getProductColor(product)" opacity="0.55" />
                <ellipse cx="100" cy="60" rx="30" ry="35" :fill="getProductColor(product)" opacity="0.4" />
                <ellipse cx="100" cy="60" rx="18" ry="22" fill="rgba(0,0,0,0.15)" />
                <circle cx="100" cy="135" r="10" fill="rgba(255,255,255,0.3)" />
              </svg>
              <svg v-else-if="product.category === 'rabbit'" viewBox="0 0 200 250" class="card-product-svg">
                <ellipse cx="65" cy="40" rx="12" ry="22" :fill="getProductColor(product)" opacity="0.6" transform="rotate(-15 65 40)" />
                <ellipse cx="135" cy="40" rx="12" ry="22" :fill="getProductColor(product)" opacity="0.6" transform="rotate(15 135 40)" />
                <path d="M65 75 Q62 120 68 180 Q100 215 132 180 Q138 120 135 75 Q118 90 100 90 Q82 90 65 75 Z"
                      :fill="getProductColor(product)" opacity="0.55" />
              </svg>
              <svg v-else-if="product.category === 'kegel'" viewBox="0 0 200 250" class="card-product-svg">
                <circle cx="100" cy="60" r="25" :fill="getProductColor(product)" opacity="0.6" />
                <circle cx="100" cy="120" r="30" :fill="getProductColor(product)" opacity="0.5" />
                <circle cx="100" cy="190" r="35" :fill="getProductColor(product)" opacity="0.45" />
              </svg>
              <svg v-else-if="product.category === 'couples'" viewBox="0 0 200 250" class="card-product-svg">
                <ellipse cx="100" cy="125" rx="60" ry="25" :fill="getProductColor(product)" opacity="0.6" />
                <ellipse cx="100" cy="125" rx="40" ry="15" fill="rgba(0,0,0,0.1)" />
                <circle cx="160" cy="125" r="12" :fill="getProductColor(product)" opacity="0.7" />
                <circle cx="40" cy="125" r="10" fill="rgba(255,255,255,0.3)" />
              </svg>
              <svg v-else-if="product.category === 'male'" viewBox="0 0 200 250" class="card-product-svg">
                <ellipse cx="100" cy="50" rx="40" ry="35" :fill="getProductColor(product)" opacity="0.5" />
                <path d="M70 75 Q65 110 70 160 Q75 220 100 230 Q125 220 130 160 Q135 110 130 75 Z"
                      :fill="getProductColor(product)" opacity="0.45" />
                <ellipse cx="100" cy="50" rx="25" ry="22" fill="rgba(0,0,0,0.1)" />
              </svg>
              <svg v-else-if="product.category === 'accessories'" viewBox="0 0 200 250" class="card-product-svg">
                <rect x="60" y="40" width="80" height="170" rx="20" :fill="getProductColor(product)" opacity="0.55" />
                <rect x="70" y="55" width="60" height="20" rx="5" fill="rgba(255,255,255,0.3)" />
                <circle cx="100" cy="160" r="15" fill="rgba(255,255,255,0.25)" />
              </svg>
              <svg v-else viewBox="0 0 200 250" class="card-product-svg">
                <ellipse cx="100" cy="50" rx="30" ry="35" :fill="getProductColor(product)" opacity="0.6" />
                <path d="M70 75 Q65 110 70 160 Q75 200 100 230 Q125 200 130 160 Q135 110 130 75 Z"
                      :fill="getProductColor(product)" opacity="0.5" />
              </svg>
            </div>
            <span v-if="product.badge" class="product-badge">{{ product.badge }}</span>
          </div>
          <div class="product-info">
            <h3 class="product-name">{{ product.name }}</h3>
            <p class="product-tagline">{{ product.tagline }}</p>
            <div class="product-price">
              <span class="price-current">${{ product.price }}</span>
              <span v-if="product.originalPrice" class="price-original">${{ product.originalPrice }}</span>
            </div>
          </div>
        </router-link>
        <button class="quick-add-btn" @click="handleAddToCart(product)">
          + Add
        </button>
      </div>
    </div>

    <div v-if="filteredProducts.length === 0" class="no-products">
      <p>No products found in this category.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, inject } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { products, categories } from '../data/products.js'

const route = useRoute()
const router = useRouter()
const addToCart = inject('addToCart')

const activeCategory = ref(route.query.category || 'all')
const sortBy = ref('featured')

const filteredProducts = computed(() => {
  if (activeCategory.value === 'all') return products
  return products.filter(p => p.category === activeCategory.value)
})

const sortedProducts = computed(() => {
  const list = [...filteredProducts.value]
  switch (sortBy.value) {
    case 'price-low':
      return list.sort((a, b) => a.price - b.price)
    case 'price-high':
      return list.sort((a, b) => b.price - a.price)
    case 'name':
      return list.sort((a, b) => a.name.localeCompare(b.name))
    default:
      return list
  }
})

const setCategory = (catId) => {
  activeCategory.value = catId
  router.push({ query: catId === 'all' ? {} : { category: catId } })
}

const getProductColor = (product) => {
  const colorMap = {
    wand: '#e5c000',
    kegel: '#8b5cf6',
    couples: '#f29520',
    gspot: '#ec4899',
    suction: '#dd5da2',
    rabbit: '#f97316',
    accessories: '#10b981',
    male: '#06b6d4',
    dildo: '#a855f7',
    anal: '#64748b',
    bondage: '#dc2626',
  }
  return colorMap[product.category] || '#dd5da2'
}

const handleAddToCart = (product) => {
  addToCart && addToCart(product)
}

onMounted(() => {
  setTimeout(() => {
    document.querySelectorAll('.fade-in-up, .fade-in').forEach((el, i) => {
      setTimeout(() => el.classList.add('visible'), i * 50)
    })
  }, 300)
})
</script>

<style scoped>
.products-page {
  padding: 100px 1.5rem 4rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.page-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.page-header h1 {
  font-size: clamp(2.5rem, 5vw, 4rem);
  margin-bottom: 0.75rem;
}

.page-header p {
  font-size: 1.125rem;
  color: var(--color-text-light);
}

.category-filter {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.75rem;
  margin-bottom: 2rem;
}

.cat-btn {
  padding: 0.5rem 1.25rem;
  border: 2px solid var(--color-text);
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--color-text);
  background: transparent;
  transition: all var(--transition-fast);
  cursor: pointer;
}

.cat-btn:hover {
  background: var(--color-text);
  color: var(--color-bg);
}

.cat-btn.active {
  background: var(--color-flavor);
  border-color: var(--color-flavor);
  color: white;
}

.sort-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(35, 31, 32, 0.1);
}

.result-count {
  font-size: 0.9rem;
  color: var(--color-text-light);
}

.sort-select {
  padding: 0.5rem 1rem;
  border: 1px solid rgba(35, 31, 32, 0.2);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.5);
  font-family: inherit;
  font-size: 0.9rem;
  color: var(--color-text);
  cursor: pointer;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 2rem;
}

.product-card {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(10px);
  transition: all var(--transition-base);
}

.product-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
}

.product-link {
  display: block;
  color: inherit;
}

.product-image {
  aspect-ratio: 4/5;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.product-img-inner {
  width: 70%;
  height: 80%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform var(--transition-base);
}

.product-card:hover .product-img-inner {
  transform: scale(1.08);
}

.card-product-svg {
  width: 100%;
  height: 100%;
}

.product-badge {
  position: absolute;
  top: 1rem;
  left: 1rem;
  background: var(--color-flavor);
  color: white;
  padding: 0.375rem 0.875rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.product-info {
  padding: 1.25rem;
}

.product-name {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.product-tagline {
  font-size: 0.875rem;
  color: var(--color-text-light);
  margin-bottom: 0.75rem;
}

.product-price {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.price-current {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--color-flavor);
}

.price-original {
  font-size: 0.9rem;
  color: var(--color-text-light);
  text-decoration: line-through;
}

.quick-add-btn {
  position: absolute;
  bottom: 1rem;
  right: 1rem;
  background: var(--color-text);
  color: var(--color-bg);
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 500;
  opacity: 0;
  transform: translateY(10px);
  transition: all var(--transition-base);
}

.product-card:hover .quick-add-btn {
  opacity: 1;
  transform: translateY(0);
}

.quick-add-btn:hover {
  background: var(--color-flavor);
}

.no-products {
  text-align: center;
  padding: 4rem 0;
  color: var(--color-text-light);
}

@media (max-width: 768px) {
  .products-page {
    padding: 80px 1rem 3rem;
  }

  .product-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }

  .category-filter {
    gap: 0.5rem;
  }

  .cat-btn {
    padding: 0.4rem 0.9rem;
    font-size: 0.8rem;
  }

  .sort-bar {
    flex-direction: column;
    gap: 0.75rem;
    align-items: flex-start;
  }
}
</style>
