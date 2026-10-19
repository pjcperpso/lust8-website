<template>
  <div v-if="product" class="product-detail">
    <!-- Breadcrumb -->
    <nav class="breadcrumb fade-in">
      <router-link to="/">{{ t.home }}</router-link>
      <span> / </span>
      <router-link to="/products">{{ t.products }}</router-link>
      <span> / </span>
      <span class="current">{{ product.name }}</span>
    </nav>

    <div class="product-layout">
      <!-- Image Gallery -->
      <div class="gallery-section fade-in-up">
        <div class="main-image" :style="{ background: `radial-gradient(ellipse at 30% 30%, ${productColor}50, ${productColor}20 70%)` }">
          <!-- Wand -->
          <svg v-if="isCategory('wand')" viewBox="0 0 200 300" class="main-product-svg">
            <defs>
              <radialGradient id="detailWandGrad" cx="30%" cy="30%" r="70%">
                <stop offset="0%" stop-color="rgba(255,255,255,0.5)" />
                <stop offset="100%" stop-color="rgba(255,255,255,0)" />
              </radialGradient>
            </defs>
            <ellipse cx="100" cy="45" rx="48" ry="52" :fill="productColor" opacity="0.6" />
            <path d="M72 88 Q68 130 74 190 Q100 210 126 190 Q132 130 128 88 Z"
                  :fill="productColor" opacity="0.55" />
            <ellipse cx="100" cy="45" rx="38" ry="42" fill="rgba(255,255,255,0.3)" />
            <circle cx="100" cy="170" r="10" fill="rgba(255,255,255,0.4)" />
            <circle cx="100" cy="200" r="10" fill="rgba(255,255,255,0.3)" />
            <ellipse cx="75" cy="55" rx="15" ry="35" fill="rgba(255,255,255,0.25)" transform="rotate(-15 75 55)" />
          </svg>

          <!-- Suction -->
          <svg v-else-if="isCategory('suction')" viewBox="0 0 200 300" class="main-product-svg">
            <defs>
              <radialGradient id="detailSuctionGrad" cx="30%" cy="30%" r="70%">
                <stop offset="0%" stop-color="rgba(255,255,255,0.5)" />
                <stop offset="100%" stop-color="rgba(255,255,255,0)" />
              </radialGradient>
            </defs>
            <ellipse cx="100" cy="160" rx="58" ry="105" :fill="productColor" opacity="0.55" />
            <ellipse cx="100" cy="65" rx="38" ry="45" :fill="productColor" opacity="0.45" />
            <ellipse cx="100" cy="65" rx="24" ry="30" fill="rgba(0,0,0,0.15)" />
            <ellipse cx="100" cy="42" rx="18" ry="12" fill="rgba(255,255,255,0.3)" />
            <circle cx="100" cy="165" r="14" fill="rgba(255,255,255,0.35)" />
            <circle cx="100" cy="165" r="7" fill="rgba(255,255,255,0.5)" />
            <rect x="88" y="250" width="24" height="12" rx="6" fill="rgba(0,0,0,0.2)" />
            <ellipse cx="72" cy="140" rx="15" ry="60" fill="rgba(255,255,255,0.2)" transform="rotate(-10 72 140)" />
          </svg>

          <!-- Rabbit -->
          <svg v-else-if="isCategory('rabbit')" viewBox="0 0 200 300" class="main-product-svg">
            <defs>
              <radialGradient id="detailRabbitGrad" cx="30%" cy="30%" r="70%">
                <stop offset="0%" stop-color="rgba(255,255,255,0.5)" />
                <stop offset="100%" stop-color="rgba(255,255,255,0)" />
              </radialGradient>
            </defs>
            <ellipse cx="65" cy="45" rx="17" ry="28" :fill="productColor" opacity="0.6" transform="rotate(-18 65 45)" />
            <ellipse cx="135" cy="45" rx="17" ry="28" :fill="productColor" opacity="0.6" transform="rotate(18 135 45)" />
            <path d="M62 80 Q58 130 65 200 Q100 240 135 200 Q142 130 138 80 Q120 100 100 100 Q80 100 62 80 Z"
                  :fill="productColor" opacity="0.55" />
            <ellipse cx="148" cy="130" rx="18" ry="25" :fill="productColor" opacity="0.5" transform="rotate(25 148 130)" />
            <circle cx="82" cy="200" r="9" fill="rgba(255,255,255,0.35)" />
            <circle cx="82" cy="225" r="9" fill="rgba(255,255,255,0.25)" />
            <ellipse cx="68" cy="150" rx="10" ry="50" fill="rgba(255,255,255,0.25)" />
          </svg>

          <!-- Kegel -->
          <svg v-else-if="isCategory('kegel')" viewBox="0 0 200 300" class="main-product-svg">
            <circle cx="100" cy="60" r="30" :fill="productColor" opacity="0.65" />
            <circle cx="100" cy="130" r="38" :fill="productColor" opacity="0.55" />
            <circle cx="100" cy="215" r="45" :fill="productColor" opacity="0.5" />
            <circle cx="90" cy="50" r="8" fill="rgba(255,255,255,0.4)" />
            <circle cx="88" cy="118" r="10" fill="rgba(255,255,255,0.35)" />
            <circle cx="85" cy="200" r="12" fill="rgba(255,255,255,0.3)" />
          </svg>

          <!-- Couples -->
          <svg v-else-if="isCategory('couples')" viewBox="0 0 200 300" class="main-product-svg">
            <ellipse cx="100" cy="150" rx="70" ry="30" :fill="productColor" opacity="0.6" />
            <ellipse cx="100" cy="150" rx="50" ry="20" fill="rgba(0,0,0,0.1)" />
            <circle cx="175" cy="150" r="15" :fill="productColor" opacity="0.7" />
            <circle cx="25" cy="150" r="12" fill="rgba(255,255,255,0.35)" />
            <circle cx="168" cy="142" r="4" fill="rgba(255,255,255,0.5)" />
          </svg>

          <!-- Default vibrator shape -->
          <svg v-else viewBox="0 0 200 300" class="main-product-svg">
            <defs>
              <radialGradient id="detailDefaultGrad" cx="30%" cy="30%" r="70%">
                <stop offset="0%" stop-color="rgba(255,255,255,0.5)" />
                <stop offset="100%" stop-color="rgba(255,255,255,0)" />
              </radialGradient>
            </defs>
            <ellipse cx="100" cy="50" rx="38" ry="42" :fill="productColor" opacity="0.6" />
            <path d="M70 82 Q65 125 70 185 Q75 240 100 265 Q125 240 130 185 Q135 125 130 82 Z"
                  :fill="productColor" opacity="0.55" />
            <ellipse cx="100" cy="50" rx="28" ry="32" fill="rgba(255,255,255,0.3)" />
            <ellipse cx="75" cy="150" rx="10" ry="45" fill="rgba(255,255,255,0.25)" />
          </svg>

          <span v-if="product.badge" class="product-badge">{{ product.badge }}</span>
        </div>
        <div class="thumbnail-row">
          <div
            v-for="(img, i) in 4"
            :key="i"
            class="thumbnail"
            :class="{ active: activeImage === i }"
            :style="{ background: `radial-gradient(ellipse at 30% 30%, ${productColor}50, ${productColor}20 70%)` }"
            @click="activeImage = i"
          >
            <svg viewBox="0 0 50 70" class="thumb-svg">
              <ellipse cx="25" cy="20" rx="10" ry="12" :fill="productColor" opacity="0.6" />
              <path d="M15 30 Q13 40 15 50 Q18 62 25 65 Q32 62 35 50 Q37 40 35 30 Z"
                    :fill="productColor" opacity="0.5" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Product Info -->
      <div class="info-section fade-in-up">
        <h1 class="product-title font-plaster">{{ product.name }}</h1>
        <p class="product-tagline">{{ product.tagline }}</p>

        <div class="price-row">
          <span class="price-current">${{ product.price }}</span>
          <span v-if="product.original_price" class="price-original">${{ product.original_price }}</span>
          <span v-if="product.original_price" class="discount-badge">
            {{ t.save }} {{ Math.round((1 - product.price / product.original_price) * 100) }}%
          </span>
        </div>

        <p class="product-desc">{{ product.description }}</p>

        <!-- Color Selection -->
        <div class="option-section">
          <span class="option-label">{{ t.color }}</span>
          <div class="color-options">
            <button
              v-for="(color, i) in product.colors"
              :key="i"
              class="color-btn"
              :class="{ active: selectedColor === i }"
              @click="selectedColor = i"
              :title="color"
            >
              {{ color.charAt(0) }}
            </button>
          </div>
          <span class="selected-color">{{ product.colors[selectedColor] }}</span>
        </div>

        <!-- Quantity -->
        <div class="option-section">
          <span class="option-label">{{ t.quantity }}</span>
          <div class="quantity-selector">
            <button class="qty-btn" @click="quantity = Math.max(1, quantity - 1)">−</button>
            <span class="qty-value">{{ quantity }}</span>
            <button class="qty-btn" @click="quantity++">+</button>
          </div>
        </div>

        <!-- Actions -->
        <div class="action-buttons">
          <button class="btn-primary add-to-cart-btn" @click="handleAddToCart" :disabled="addingToCart">
            <span>{{ addingToCart ? t.adding : t.addToCart }}</span>
            <svg viewBox="0 0 60 59" class="btn-arrow">
              <path d="M17.837,42.495c0,1.577-1.256,2.855-2.805,2.855s-2.805-1.278-2.805-2.855,1.256-2.855,2.805-2.855,2.805,1.278,2.805,2.855ZM41.718,39.641c-1.549,0-2.805,1.278-2.805,2.855s1.256,2.855,2.805,2.855,2.805-1.278,2.805-2.855-1.256-2.855-2.805-2.855ZM16.564,30.108h27.621l5.815-20.049h-4.473l-4.549,15.683h-24.94L10.333,5.35H0v4.366h7.094l5.18,18.514v9.694h32.247v-4.366h-27.958v-3.451Z"
                    fill="currentColor" />
            </svg>
          </button>
          <button class="btn-secondary buy-now-btn" @click="handleBuyNow">
            {{ t.buyNow }}
          </button>
        </div>

        <!-- Features List -->
        <div class="features-list">
          <h3>{{ t.features }}</h3>
          <ul>
            <li v-for="(feature, i) in product.features" :key="i">
              <span class="check-icon">✓</span>
              {{ feature }}
            </li>
          </ul>
        </div>

        <!-- Trust Badges -->
        <div class="trust-badges">
          <div class="trust-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
            </svg>
            <span>{{ t.bodySafe }}</span>
          </div>
          <div class="trust-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
              <circle cx="12" cy="10" r="3" />
            </svg>
            <span>{{ t.discreet }}</span>
          </div>
          <div class="trust-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="20 6 9 17 4 12" />
            </svg>
            <span>{{ t.returns }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Related Products -->
    <section v-if="relatedProducts.length > 0" class="related-products fade-in-up">
      <h2 class="section-title font-plaster text-center">{{ t.related }}</h2>
      <div class="product-grid">
        <div
          v-for="p in relatedProducts"
          :key="p.id"
          class="product-card"
        >
          <router-link :to="`/products/${p.slug}`" class="product-link">
            <div class="product-image" :style="{ background: `linear-gradient(135deg, ${getColor(p)}30, ${getColor(p)}60)` }">
              <div class="product-img-inner">
                <svg viewBox="0 0 200 250" class="card-product-svg">
                  <ellipse cx="100" cy="50" rx="30" ry="35" :fill="getColor(p)" opacity="0.6" />
                  <path d="M70 75 Q65 110 70 160 Q75 200 100 230 Q125 200 130 160 Q135 110 130 75 Z"
                        :fill="getColor(p)" opacity="0.5" />
                </svg>
              </div>
            </div>
            <div class="product-info">
              <h3 class="product-name">{{ p.name }}</h3>
              <div class="product-price">
                <span class="price-current">${{ p.price }}</span>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </section>
  </div>

  <!-- Loading -->
  <div v-else-if="loading" class="product-loading">
    <div class="spinner"></div>
    <p>{{ t.loading }}</p>
  </div>

  <!-- Not found -->
  <div v-else class="product-not-found">
    <h2>{{ t.notFound }}</h2>
    <router-link to="/products" class="btn-primary">{{ t.backToProducts }}</router-link>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, inject, watch } from 'vue'
import { useRoute } from 'vue-router'
import { getProduct, getProducts } from '../api/products'
import { useCartStore } from '../stores/cart'
import { useScrollAnimation } from '../composables/useScrollAnimation'

const route = useRoute()
const cartStore = useCartStore()
const lang = inject('lang', ref('en'))
const { refreshObserver } = useScrollAnimation()

const product = ref(null)
const relatedProducts = ref([])
const loading = ref(true)
const quantity = ref(1)
const selectedColor = ref(0)
const activeImage = ref(0)
const addingToCart = ref(false)

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

const productColor = computed(() => {
  if (!product.value) return '#dd5da2'
  // We don't have category slug on product directly, map by category_id isn't reliable
  // Fallback to a default color scheme based on product
  return '#dd5da2'
})

const t = computed(() => ({
  home: lang.value === 'en' ? 'Home' : '首页',
  products: lang.value === 'en' ? 'Products' : '产品',
  save: lang.value === 'en' ? 'Save' : '节省',
  color: lang.value === 'en' ? 'Color' : '颜色',
  quantity: lang.value === 'en' ? 'Quantity' : '数量',
  addToCart: lang.value === 'en' ? 'Add to Cart' : '加入购物车',
  adding: lang.value === 'en' ? 'Adding...' : '添加中...',
  buyNow: lang.value === 'en' ? 'Buy Now' : '立即购买',
  features: lang.value === 'en' ? 'Features' : '产品特性',
  bodySafe: lang.value === 'en' ? 'Body Safe' : '身体安全',
  discreet: lang.value === 'en' ? 'Discreet Shipping' : '隐私配送',
  returns: lang.value === 'en' ? '30-Day Returns' : '30天退换',
  related: lang.value === 'en' ? 'You May Also Like' : '你可能还喜欢',
  loading: lang.value === 'en' ? 'Loading...' : '加载中...',
  notFound: lang.value === 'en' ? 'Product not found' : '产品未找到',
  backToProducts: lang.value === 'en' ? 'Back to Products' : '返回产品列表',
  added: lang.value === 'en' ? 'Added to cart!' : '已加入购物车！',
  addFailed: lang.value === 'en' ? 'Failed to add to cart' : '添加购物车失败',
}))

function isCategory(slug) {
  // We'll determine by checking product features and name patterns
  if (!product.value) return false
  const name = product.value.name.toLowerCase()
  const tagline = product.value.tagline.toLowerCase()
  if (slug === 'wand') return name.includes('wand') || tagline.includes('massager')
  if (slug === 'suction') return name.includes('halo') || tagline.includes('air pulse') || tagline.includes('stimulator')
  if (slug === 'rabbit') return name.includes('rabbit') || tagline.includes('dual action') || tagline.includes('dual-action')
  if (slug === 'kegel') return name.includes('beads') || tagline.includes('kegel')
  if (slug === 'couples') return name.includes('eclipse') || tagline.includes('couples') || tagline.includes('ring')
  return false
}

function getColor(p) {
  // Heuristic color based on product name
  const name = p.name.toLowerCase()
  if (name.includes('wand')) return colorMap.wand
  if (name.includes('rabbit')) return colorMap.rabbit
  if (name.includes('halo') || name.includes('clitoral')) return colorMap.suction
  if (name.includes('luna') || name.includes('beads')) return colorMap.kegel
  if (name.includes('eclipse') || name.includes('couples')) return colorMap.couples
  if (name.includes('titan') || name.includes('male')) return colorMap.male
  if (name.includes('velvet') || name.includes('curve')) return colorMap.gspot
  if (name.includes('bondage')) return colorMap.bondage
  if (name.includes('dildo') || name.includes('density')) return colorMap.dildo
  if (name.includes('anal') || name.includes('trainer')) return colorMap.anal
  if (name.includes('sensual') || name.includes('silk') || name.includes('glide')) return colorMap.accessories
  return '#dd5da2'
}

async function loadProduct() {
  const id = route.params.id
  loading.value = true
  try {
    const data = await getProduct(id, lang.value)
    product.value = data
    quantity.value = 1
    selectedColor.value = 0
    activeImage.value = 0

    // Load related products
    await loadRelatedProducts(data.category_id, data.id)
  } catch (err) {
    console.error('Failed to load product:', err.message)
    product.value = null
  } finally {
    loading.value = false
    setTimeout(() => refreshObserver(), 100)
  }
}

async function loadRelatedProducts(categoryId, excludeId) {
  try {
    const data = await getProducts({
      page: 1,
      page_size: 6,
      lang: lang.value,
      sort: 'featured',
    })
    relatedProducts.value = data.items
      .filter((p) => p.id !== excludeId)
      .slice(0, 4)
  } catch (err) {
    console.error('Failed to load related products:', err.message)
    relatedProducts.value = []
  }
}

async function handleAddToCart() {
  if (!product.value) return
  addingToCart.value = true
  try {
    const color = product.value.colors[selectedColor.value] || ''
    await cartStore.addProductToCart(product.value.id, quantity.value, color, lang.value)
    // Simple feedback
    console.log(t.value.added)
  } catch (err) {
    alert(t.value.addFailed)
  } finally {
    addingToCart.value = false
  }
}

function handleBuyNow() {
  handleAddToCart().then(() => {
    // In a full implementation, redirect to checkout
    alert(lang.value === 'en' ? 'Proceeding to checkout...' : '前往结算...')
  })
}

watch(
  () => route.params.id,
  () => {
    loadProduct()
    window.scrollTo(0, 0)
  }
)

watch(lang, () => {
  if (route.params.id) loadProduct()
})

onMounted(() => {
  loadProduct()
  window.scrollTo(0, 0)
})
</script>

<style scoped>
.product-detail {
  padding: 100px 1.5rem 4rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.product-loading,
.product-not-found {
  padding: 200px 1rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
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

.product-not-found h2 {
  font-size: 1.5rem;
  color: var(--color-text-light);
}

.breadcrumb {
  font-size: 0.875rem;
  color: var(--color-text-light);
  margin-bottom: 2rem;
}

.breadcrumb a {
  color: var(--color-text-light);
}

.breadcrumb a:hover {
  color: var(--color-flavor);
}

.breadcrumb .current {
  color: var(--color-text);
  font-weight: 500;
}

.product-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  margin-bottom: 5rem;
}

.gallery-section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.main-image {
  aspect-ratio: 4/5;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.main-product-svg {
  width: 65%;
  height: auto;
  filter: drop-shadow(0 20px 40px rgba(0,0,0,0.15));
}

.product-badge {
  position: absolute;
  top: 1.5rem;
  left: 1.5rem;
  background: var(--color-flavor);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.thumbnail-row {
  display: flex;
  gap: 0.75rem;
}

.thumbnail {
  flex: 1;
  aspect-ratio: 1;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border: 2px solid transparent;
  transition: all var(--transition-fast);
}

.thumbnail:hover {
  border-color: var(--color-flavor);
}

.thumbnail.active {
  border-color: var(--color-flavor);
}

.thumb-svg {
  width: 60%;
  height: auto;
}

/* Info Section */
.info-section {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.product-title {
  font-size: clamp(2rem, 4vw, 3rem);
  margin-bottom: 0.25rem;
}

.product-tagline {
  font-size: 1.25rem;
  color: var(--color-text-light);
}

.price-row {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid rgba(35, 31, 32, 0.1);
}

.price-current {
  font-size: 2rem;
  font-weight: 700;
  color: var(--color-flavor);
}

.price-original {
  font-size: 1.25rem;
  color: var(--color-text-light);
  text-decoration: line-through;
}

.discount-badge {
  background: var(--color-flavor);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.8rem;
  font-weight: 600;
}

.product-desc {
  font-size: 1rem;
  line-height: 1.7;
  color: var(--color-text-light);
}

.option-section {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.option-label {
  font-size: 0.9rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.color-options {
  display: flex;
  gap: 0.75rem;
}

.color-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 2px solid rgba(35, 31, 32, 0.2);
  background: rgba(255, 255, 255, 0.5);
  font-weight: 600;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.color-btn:hover {
  border-color: var(--color-text);
}

.color-btn.active {
  border-color: var(--color-flavor);
  background: var(--color-flavor);
  color: white;
}

.selected-color {
  font-size: 0.9rem;
  color: var(--color-text-light);
}

.quantity-selector {
  display: inline-flex;
  align-items: center;
  border: 2px solid var(--color-text);
  border-radius: 9999px;
  width: fit-content;
}

.qty-btn {
  width: 44px;
  height: 44px;
  font-size: 1.25rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  cursor: pointer;
  transition: background var(--transition-fast);
  border: none;
  color: var(--color-text);
}

.qty-btn:hover {
  background: var(--color-text);
  color: var(--color-bg);
}

.qty-value {
  width: 50px;
  text-align: center;
  font-weight: 600;
  font-size: 1.1rem;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  padding: 0.5rem 0;
}

.add-to-cart-btn {
  width: 100%;
  justify-content: center;
  padding: 1rem 2rem;
  font-size: 1rem;
}

.btn-arrow {
  width: 22px;
}

.btn-secondary {
  width: 100%;
  padding: 1rem 2rem;
  border: 2px solid var(--color-text);
  border-radius: 9999px;
  background: transparent;
  font-size: 1rem;
  font-weight: 500;
  color: var(--color-text);
  cursor: pointer;
  transition: all var(--transition-base);
  font-family: inherit;
}

.btn-secondary:hover {
  background: var(--color-text);
  color: var(--color-bg);
}

.features-list h3 {
  font-size: 1.125rem;
  margin-bottom: 0.75rem;
}

.features-list ul {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
  list-style: none;
  padding: 0;
}

.features-list li {
  font-size: 0.9rem;
  color: var(--color-text-light);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.check-icon {
  color: var(--color-flavor);
  font-weight: 700;
}

.trust-badges {
  display: flex;
  gap: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(35, 31, 32, 0.1);
}

.trust-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  color: var(--color-text-light);
  font-size: 0.8rem;
  text-align: center;
}

.trust-item svg {
  width: 24px;
  height: 24px;
}

/* Related Products */
.related-products {
  padding: 3rem 0;
  border-top: 1px solid rgba(35, 31, 32, 0.1);
}

.section-title {
  font-size: clamp(1.75rem, 3vw, 2.5rem);
  margin-bottom: 2rem;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1.5rem;
}

.product-card {
  border-radius: 12px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.3);
  transition: all var(--transition-base);
}

.product-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
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

.product-info {
  padding: 1rem;
}

.product-name {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.product-price .price-current {
  font-size: 1.1rem;
}

@media (max-width: 768px) {
  .product-detail {
    padding: 80px 1rem 3rem;
  }

  .product-layout {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .features-list ul {
    grid-template-columns: 1fr;
  }

  .trust-badges {
    gap: 1rem;
  }

  .product-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
}
</style>
