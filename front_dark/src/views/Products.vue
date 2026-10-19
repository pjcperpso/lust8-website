<template>
  <div class="products-page">
    <div class="page-header">
      <h1 class="font-plaster fade-in-up">{{ t.title }}</h1>
      <p class="fade-in-up tracking-wide">{{ t.subtitle }}</p>
    </div>

    <!-- Category Filter -->
    <div class="category-filter fade-in-up">
      <button
        v-for="cat in allCategories"
        :key="cat.id || cat.slug"
        class="cat-btn"
        :class="{ active: activeCategory === (cat.slug || 'all') }"
        @click="setCategory(cat.slug || 'all')"
      >
        {{ cat.name }}
      </button>
    </div>

    <!-- Sort -->
    <div class="sort-bar fade-in-up">
      <span class="result-count">{{ totalProducts }} {{ t.products }}</span>
      <select v-model="sortBy" class="sort-select" @change="handleSortChange">
        <option value="featured">{{ t.sortFeatured }}</option>
        <option value="price-low">{{ t.sortPriceLow }}</option>
        <option value="price-high">{{ t.sortPriceHigh }}</option>
        <option value="name">{{ t.sortName }}</option>
      </select>
    </div>

    <!-- Loading -->
    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
      <p>{{ t.loading }}</p>
    </div>

    <!-- Product Grid -->
    <div v-else class="product-grid">
      <div
        v-for="product in products"
        :key="product.id"
        class="product-card fade-in-up"
      >
        <router-link :to="`/products/${product.slug}`" class="product-link">
          <div class="product-image" :style="{ background: `radial-gradient(ellipse at 30% 30%, ${getProductColor(product)}50, ${getProductColor(product)}20 70%)` }">
            <div class="product-img-inner">
              <!-- Different shapes by category -->
              <svg v-if="product.category_id === getCategoryId('wand')" viewBox="0 0 200 250" class="card-product-svg">
                <ellipse cx="100" cy="40" rx="40" ry="45" :fill="getProductColor(product)" opacity="0.6" />
                <path d="M75 78 Q72 115 78 170 Q100 185 122 170 Q128 115 125 78 Z"
                      :fill="getProductColor(product)" opacity="0.5" />
                <circle cx="100" cy="140" r="6" fill="rgba(255,255,255,0.4)" />
              </svg>
              <svg v-else-if="product.category_id === getCategoryId('suction')" viewBox="0 0 200 250" class="card-product-svg">
                <ellipse cx="100" cy="130" rx="45" ry="80" :fill="getProductColor(product)" opacity="0.55" />
                <ellipse cx="100" cy="60" rx="30" ry="35" :fill="getProductColor(product)" opacity="0.4" />
                <ellipse cx="100" cy="60" rx="18" ry="22" fill="rgba(0,0,0,0.15)" />
                <circle cx="100" cy="135" r="10" fill="rgba(255,255,255,0.3)" />
              </svg>
              <svg v-else-if="product.category_id === getCategoryId('rabbit')" viewBox="0 0 200 250" class="card-product-svg">
                <ellipse cx="65" cy="40" rx="12" ry="22" :fill="getProductColor(product)" opacity="0.6" transform="rotate(-15 65 40)" />
                <ellipse cx="135" cy="40" rx="12" ry="22" :fill="getProductColor(product)" opacity="0.6" transform="rotate(15 135 40)" />
                <path d="M65 75 Q62 120 68 180 Q100 215 132 180 Q138 120 135 75 Q118 90 100 90 Q82 90 65 75 Z"
                      :fill="getProductColor(product)" opacity="0.55" />
              </svg>
              <svg v-else-if="product.category_id === getCategoryId('kegel')" viewBox="0 0 200 250" class="card-product-svg">
                <circle cx="100" cy="60" r="25" :fill="getProductColor(product)" opacity="0.6" />
                <circle cx="100" cy="120" r="30" :fill="getProductColor(product)" opacity="0.5" />
                <circle cx="100" cy="190" r="35" :fill="getProductColor(product)" opacity="0.45" />
              </svg>
              <svg v-else-if="product.category_id === getCategoryId('couples')" viewBox="0 0 200 250" class="card-product-svg">
                <ellipse cx="100" cy="125" rx="60" ry="25" :fill="getProductColor(product)" opacity="0.6" />
                <ellipse cx="100" cy="125" rx="40" ry="15" fill="rgba(0,0,0,0.1)" />
                <circle cx="160" cy="125" r="12" :fill="getProductColor(product)" opacity="0.7" />
                <circle cx="40" cy="125" r="10" fill="rgba(255,255,255,0.3)" />
              </svg>
              <svg v-else-if="product.category_id === getCategoryId('male')" viewBox="0 0 200 250" class="card-product-svg">
                <ellipse cx="100" cy="50" rx="40" ry="35" :fill="getProductColor(product)" opacity="0.5" />
                <path d="M70 75 Q65 110 70 160 Q75 220 100 230 Q125 220 130 160 Q135 110 130 75 Z"
                      :fill="getProductColor(product)" opacity="0.45" />
                <ellipse cx="100" cy="50" rx="25" ry="22" fill="rgba(0,0,0,0.1)" />
              </svg>
              <svg v-else-if="product.category_id === getCategoryId('accessories')" viewBox="0 0 200 250" class="card-product-svg">
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
              <span v-if="product.original_price" class="price-original">${{ product.original_price }}</span>
            </div>
          </div>
        </router-link>
        <button class="quick-add-btn" @click="handleAddToCart(product)">
          + {{ t.add }}
        </button>
      </div>
    </div>

    <!-- Pagination -->
    <div v-if="!loading && totalPages > 1" class="pagination">
      <button
        class="page-btn"
        :disabled="page <= 1"
        @click="goToPage(page - 1)"
      >
        ← {{ t.prev }}
      </button>
      <span class="page-info">{{ page }} / {{ totalPages }}</span>
      <button
        class="page-btn"
        :disabled="page >= totalPages"
        @click="goToPage(page + 1)"
      >
        {{ t.next }} →
      </button>
    </div>

    <div v-if="!loading && products.length === 0" class="no-products">
      <p>{{ t.noProducts }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, inject, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getProducts, getCategories } from '../api/products'
import { useCartStore } from '../stores/cart'
import { useScrollAnimation } from '../composables/useScrollAnimation'

const route = useRoute()
const router = useRouter()
const cartStore = useCartStore()
const lang = inject('lang', ref('en'))
const { refreshObserver } = useScrollAnimation()

// State
const products = ref([])
const categories = ref([])
const loading = ref(false)
const totalProducts = ref(0)
const page = ref(1)
const pageSize = ref(12)
const activeCategory = ref(route.query.category || 'all')
const sortBy = ref('featured')

// Computed
const totalPages = computed(() => Math.ceil(totalProducts.value / pageSize.value))

const allCategories = computed(() => {
  const allCat = {
    slug: 'all',
    name: lang.value === 'en' ? 'All Products' : '全部产品',
    icon: 'sparkle',
  }
  return [allCat, ...categories.value]
})

const t = computed(() => ({
  title: lang.value === 'en' ? 'All Products' : '全部产品',
  subtitle: lang.value === 'en'
    ? 'Explore our complete collection of premium intimate wellness products.'
    : '探索我们的优质情趣健康产品系列。',
  products: lang.value === 'en' ? 'products' : '个产品',
  sortFeatured: lang.value === 'en' ? 'Featured' : '推荐',
  sortPriceLow: lang.value === 'en' ? 'Price: Low to High' : '价格：从低到高',
  sortPriceHigh: lang.value === 'en' ? 'Price: High to Low' : '价格：从高到低',
  sortName: lang.value === 'en' ? 'Name A-Z' : '名称 A-Z',
  add: lang.value === 'en' ? 'Add' : '加入',
  loading: lang.value === 'en' ? 'Loading...' : '加载中...',
  prev: lang.value === 'en' ? 'Prev' : '上一页',
  next: lang.value === 'en' ? 'Next' : '下一页',
  noProducts: lang.value === 'en' ? 'No products found in this category.' : '该分类暂无产品。',
}))

// Helpers
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

function getCategoryId(slug) {
  const cat = categories.value.find((c) => c.slug === slug)
  return cat ? cat.id : -1
}

function getProductColor(product) {
  const cat = categories.value.find((c) => c.id === product.category_id)
  if (cat && colorMap[cat.slug]) return colorMap[cat.slug]
  return '#dd5da2'
}

// Data fetching
async function loadProducts() {
  loading.value = true
  try {
    const params = {
      page: page.value,
      page_size: pageSize.value,
      lang: lang.value,
      sort: sortParam.value,
    }
    if (activeCategory.value !== 'all') {
      params.category = activeCategory.value
    }
    const data = await getProducts(params)
    products.value = data.items
    totalProducts.value = data.total
  } catch (err) {
    console.error('Failed to load products:', err.message)
    products.value = []
    totalProducts.value = 0
  } finally {
    loading.value = false
    // Refresh scroll animations after data loads
    setTimeout(() => refreshObserver(), 100)
  }
}

async function loadCategories() {
  try {
    const data = await getCategories(lang.value)
    categories.value = data
  } catch (err) {
    console.error('Failed to load categories:', err.message)
  }
}

const sortParam = computed(() => {
  switch (sortBy.value) {
    case 'price-low': return 'price-asc'
    case 'price-high': return 'price-desc'
    case 'name': return 'name'
    default: return 'featured'
  }
})

// Actions
function setCategory(catId) {
  activeCategory.value = catId
  page.value = 1
  router.push({ query: catId === 'all' ? {} : { category: catId } })
}

function handleSortChange() {
  page.value = 1
  loadProducts()
}

function goToPage(p) {
  page.value = p
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

async function handleAddToCart(product) {
  try {
    const color = product.colors && product.colors[0] ? product.colors[0] : ''
    await cartStore.addProductToCart(product.id, 1, color, lang.value)
  } catch (err) {
    alert(lang.value === 'en' ? 'Failed to add to cart' : '添加购物车失败')
  }
}

// Watchers
watch(activeCategory, () => {
  page.value = 1
  loadProducts()
})

watch(page, () => {
  loadProducts()
})

watch(lang, () => {
  loadCategories()
  loadProducts()
})

onMounted(() => {
  loadCategories()
  loadProducts()
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

.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 0;
  gap: 1rem;
  color: var(--color-text-light);
}

.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(255, 255, 255, 0.2);
  border-top-color: var(--color-flavor);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
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
  border: none;
  cursor: pointer;
}

.product-card:hover .quick-add-btn {
  opacity: 1;
  transform: translateY(0);
}

.quick-add-btn:hover {
  background: var(--color-flavor);
}

.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  margin-top: 3rem;
}

.page-btn {
  padding: 0.6rem 1.25rem;
  border: 2px solid var(--color-text);
  border-radius: 9999px;
  background: transparent;
  color: var(--color-text);
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.page-btn:hover:not(:disabled) {
  background: var(--color-text);
  color: var(--color-bg);
}

.page-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.page-info {
  font-family: var(--font-mono);
  font-size: 0.9rem;
  color: var(--color-text-light);
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
