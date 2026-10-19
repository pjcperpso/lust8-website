<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero-section">
      <h1 class="hero-subtitle tracking-widest fade-in">
        Premium Adult Pleasure
      </h1>

      <!-- Product Carousel -->
      <div class="carousel-container">
        <hr class="carousel-line" />
        <nav class="carousel">
          <button class="carousel-btn prev" @click="prevProduct" aria-label="Previous">
            <svg viewBox="0 0 75 85" class="arrow-icon">
              <path d="M0,42.5l75,42.5v-42.5S75,0,75,0L0,42.5ZM4.547,42.5L74.738.513,13.85,42.5l60.888,41.987L4.547,42.5ZM72.394,42.5l2.344,40.481-8.807-40.481L74.738,2.019l-2.344,40.481Z" />
            </svg>
          </button>

          <ul class="fruit-list">
            <li
              v-for="(product, index) in heroProducts"
              :key="index"
              class="fruit-item"
              :class="{
                active: index === activeHeroIndex,
                blur: index !== activeHeroIndex
              }"
              :style="{
                transform: index === activeHeroIndex ? 'scale(1)' : 'scale(0.8)',
                opacity: index === activeHeroIndex ? 1 : 0.5
              }"
              @click="setActiveHero(index)"
            >
              <div class="fruit-icon" :style="{ color: product.color }">
                <svg viewBox="0 0 70 100" v-html="product.iconSvg"></svg>
              </div>
            </li>
          </ul>

          <button class="carousel-btn next" @click="nextProduct" aria-label="Next">
            <svg viewBox="0 0 75 85" class="arrow-icon">
              <path d="M0,42.5l75,42.5v-42.5S75,0,75,0L0,42.5ZM4.547,42.5L74.738.513,13.85,42.5l60.888,41.987L4.547,42.5ZM72.394,42.5l2.344,40.481-8.807-40.481L74.738,2.019l-2.344,40.481Z" />
            </svg>
          </button>
        </nav>
      </div>

      <!-- Product Spin Animation -->
      <div class="spin-section">
        <div class="spin-container">
          <div class="product-display">
            <div
              class="product-sprite"
              :style="{ transform: `translateX(-${spriteOffset}px)` }"
            >
              <!-- Product placeholder gradient -->
              <div class="product-placeholder">
                <div class="product-shape" :style="{ background: `radial-gradient(ellipse at 30% 30%, ${heroProducts[activeHeroIndex].color}60, ${heroProducts[activeHeroIndex].color}20 70%)` }">
                  <!-- Suction Stimulator (Halo) -->
                  <svg v-if="activeHeroIndex === 0" viewBox="0 0 200 300" class="product-svg">
                    <defs>
                      <radialGradient id="haloGrad" cx="30%" cy="30%" r="70%">
                        <stop offset="0%" stop-color="rgba(255,255,255,0.5)" />
                        <stop offset="50%" stop-color="rgba(255,255,255,0.2)" />
                        <stop offset="100%" stop-color="rgba(255,255,255,0)" />
                      </radialGradient>
                    </defs>
                    <!-- Body -->
                    <ellipse cx="100" cy="160" rx="55" ry="100" fill="url(#haloGrad)" />
                    <!-- Top opening -->
                    <ellipse cx="100" cy="70" rx="35" ry="40" fill="rgba(255,255,255,0.3)" />
                    <ellipse cx="100" cy="70" rx="22" ry="28" fill="rgba(0,0,0,0.1)" />
                    <!-- Control panel -->
                    <circle cx="100" cy="160" r="12" fill="rgba(255,255,255,0.4)" />
                    <circle cx="100" cy="160" r="6" fill="rgba(255,255,255,0.6)" />
                    <!-- Bottom charging port -->
                    <rect x="88" y="250" width="24" height="10" rx="5" fill="rgba(0,0,0,0.2)" />
                    <!-- Highlight -->
                    <ellipse cx="75" cy="140" rx="15" ry="50" fill="rgba(255,255,255,0.25)" transform="rotate(-15 75 140)" />
                  </svg>

                  <!-- Wand Massager (Aura) -->
                  <svg v-else-if="activeHeroIndex === 1" viewBox="0 0 200 300" class="product-svg">
                    <defs>
                      <radialGradient id="wandGrad" cx="30%" cy="30%" r="70%">
                        <stop offset="0%" stop-color="rgba(255,255,255,0.5)" />
                        <stop offset="100%" stop-color="rgba(255,255,255,0)" />
                      </radialGradient>
                    </defs>
                    <!-- Head -->
                    <ellipse cx="100" cy="45" rx="45" ry="50" fill="url(#wandGrad)" />
                    <ellipse cx="100" cy="45" rx="35" ry="40" fill="rgba(255,255,255,0.3)" />
                    <!-- Neck -->
                    <path d="M80 85 Q78 110 82 140 Q100 148 118 140 Q122 110 120 85 Z" fill="url(#wandGrad)" />
                    <!-- Handle -->
                    <path d="M75 140 Q70 200 75 255 Q100 265 125 255 Q130 200 125 140 Z"
                          fill="url(#wandGrad)" />
                    <!-- Control buttons -->
                    <circle cx="100" cy="180" r="8" fill="rgba(255,255,255,0.4)" />
                    <circle cx="100" cy="205" r="8" fill="rgba(255,255,255,0.3)" />
                    <!-- Highlight -->
                    <ellipse cx="70" cy="50" rx="12" ry="30" fill="rgba(255,255,255,0.3)" transform="rotate(-20 70 50)" />
                    <ellipse cx="68" cy="190" rx="8" ry="40" fill="rgba(255,255,255,0.2)" />
                  </svg>

                  <!-- Rabbit Vibrator (Nocturne) -->
                  <svg v-else viewBox="0 0 200 300" class="product-svg">
                    <defs>
                      <radialGradient id="rabbitGrad" cx="30%" cy="30%" r="70%">
                        <stop offset="0%" stop-color="rgba(255,255,255,0.5)" />
                        <stop offset="100%" stop-color="rgba(255,255,255,0)" />
                      </radialGradient>
                    </defs>
                    <!-- Rabbit ears -->
                    <ellipse cx="70" cy="45" rx="15" ry="25" fill="url(#rabbitGrad)" transform="rotate(-20 70 45)" />
                    <ellipse cx="130" cy="45" rx="15" ry="25" fill="url(#rabbitGrad)" transform="rotate(20 130 45)" />
                    <!-- Main body -->
                    <path d="M65 80 Q60 120 65 180 Q70 240 100 265 Q130 240 135 180 Q140 120 135 80 Q118 95 100 95 Q82 95 65 80 Z"
                          fill="url(#rabbitGrad)" />
                    <!-- G-spot curve nub -->
                    <ellipse cx="140" cy="120" rx="15" ry="20" fill="url(#rabbitGrad)" transform="rotate(30 140 120)" />
                    <!-- Control pad -->
                    <circle cx="85" cy="190" r="7" fill="rgba(255,255,255,0.4)" />
                    <circle cx="85" cy="215" r="7" fill="rgba(255,255,255,0.3)" />
                    <!-- Highlight -->
                    <ellipse cx="70" cy="140" rx="10" ry="50" fill="rgba(255,255,255,0.25)" />
                  </svg>
                </div>
              </div>
            </div>
          </div>

          <!-- Scrubber -->
          <div class="scrubber">
            <div class="scrubber-track" ref="scrubberTrack" @mousedown="startDrag" @touchstart="startDrag">
              <div
                class="scrubber-drag"
                :style="{ transform: `translateX(${dragPosition}px)` }"
                ref="scrubberDrag"
              >
                <svg viewBox="0 0 60 60">
                  <circle cx="30" cy="30" r="30" :fill="heroProducts[activeHeroIndex].color" />
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>

      <h1 class="hero-title font-plaster fade-in-up">
        {{ heroProducts[activeHeroIndex].name }}
        <span>{{ heroProducts[activeHeroIndex].tagline }}</span>
      </h1>

      <router-link
        :to="`/products/${heroProducts[activeHeroIndex].id}`"
        class="buy-button uppercase fade-in-up"
      >
        <span>Shop Now</span>
        <svg viewBox="0 0 60 59">
          <path d="M20.018,29.5h-8.663V3.5l43.645,26L11.355,55.5H0"
                fill="none" :stroke="heroProducts[activeHeroIndex].color" stroke-miterlimit="10" />
          <polygon points="36.999 29.5 20.018 19.384 20.018 39.616 36.999 29.5"
                   fill="none" :stroke="heroProducts[activeHeroIndex].color" stroke-miterlimit="10" />
        </svg>
      </router-link>

      <!-- ACTV8-style Feature Bar -->
      <section class="feature-bar">
        <svg viewBox="0 0 400 42" class="feature-svg">
          <defs>
            <clipPath id="featureClip">
              <rect x="0" y="0" width="400" height="42" />
            </clipPath>
          </defs>
          <g clip-path="url(#featureClip)">
            <rect x="49.5" y="0" width="301" height="42" rx="21"
                  :fill="heroProducts[activeHeroIndex].color"
                  class="feature-bg" />
            <text x="200" y="28" text-anchor="middle"
                  class="feature-text"
                  fill="#231f20"
                  font-family="'Outfit', sans-serif"
                  font-size="14"
                  font-weight="600"
                  letter-spacing="2">
              FEATURED COLLECTION
            </text>
          </g>
          <circle cx="16.687" cy="21" r="13.687" fill="none"
                  :stroke="heroProducts[activeHeroIndex].color"
                  stroke-miterlimit="10" stroke-width="6" />
          <circle cx="383.313" cy="21" r="13.687" fill="none"
                  :stroke="heroProducts[activeHeroIndex].color"
                  stroke-miterlimit="10" stroke-width="6" />
        </svg>
      </section>
    </section>

    <!-- Ingredients / Features Visualization -->
    <section class="ingredients-section">
      <div class="ingredients-geo">
        <svg viewBox="0 0 1050 900" class="geo-svg">
          <!-- Outer rings -->
          <circle cx="525" cy="450" r="308" fill="none"
                  :stroke="heroProducts[activeHeroIndex].color"
                  stroke-dasharray="4 8 8 8" opacity="0.5" />
          <circle cx="525" cy="450" r="238" fill="none"
                  :stroke="heroProducts[activeHeroIndex].color"
                  stroke-width="2" opacity="0.5" />
          <circle cx="525" cy="450" r="177" fill="none"
                  :stroke="heroProducts[activeHeroIndex].color"
                  stroke-width="2" />

          <!-- Triangle shape -->
          <polygon points="525,272 371,538 679,538"
                   fill="none"
                   :stroke="heroProducts[activeHeroIndex].color"
                   stroke-width="2"
                   stroke-linejoin="bevel" />

          <!-- Inner triangle -->
          <polygon points="525,538 601,405 449,405"
                   fill="none"
                   :stroke="heroProducts[activeHeroIndex].color"
                   stroke-width="2"
                   stroke-linejoin="bevel" />

          <!-- Feature dots on hex points -->
          <g v-for="(ing, index) in displayIngredients" :key="ing.id">
            <circle :cx="ingredientPositions[index].x"
                    :cy="ingredientPositions[index].y"
                    r="4"
                    :fill="heroProducts[activeHeroIndex].color"
                    class="feature-dot" />
          </g>

          <!-- Dashed lines connecting -->
          <line v-for="(line, i) in connectLines" :key="i"
                :x1="line.x1" :y1="line.y1" :x2="line.x2" :y2="line.y2"
                :stroke="heroProducts[activeHeroIndex].color"
                stroke-dasharray="4 8 8 8" opacity="0.5" />
        </svg>

        <div class="ingredient-content">
          <h2 class="font-plaster ingredient-title">
            {{ currentIngredient.name }}
            <span>{{ currentIngredient.fullName }}</span>
          </h2>
          <p class="ingredient-desc">{{ currentIngredient.description }}</p>
        </div>
      </div>
    </section>

    <!-- Featured Products -->
    <section class="featured-products">
      <h2 class="section-title font-plaster text-center fade-in-up">
        Best Sellers
      </h2>
      <p class="section-subtitle text-center fade-in-up tracking-wide">
        Our most popular adult pleasure products, loved by thousands worldwide
      </p>

      <div class="product-grid">
        <div
          v-for="product in featuredProducts"
          :key="product.id"
          class="product-card fade-in-up"
        >
          <router-link :to="`/products/${product.id}`" class="product-link">
            <div class="product-image" :style="{ background: `radial-gradient(ellipse at 30% 30%, ${getProductColor(product)}50, ${getProductColor(product)}20 70%)` }">
              <div class="product-img-inner">
                <!-- Wand -->
                <svg v-if="product.category === 'wand'" viewBox="0 0 200 250" class="card-product-svg">
                  <ellipse cx="100" cy="40" rx="38" ry="42" :fill="getProductColor(product)" opacity="0.6" />
                  <path d="M74 75 Q70 110 76 155 Q100 170 124 155 Q128 110 126 75 Z"
                        :fill="getProductColor(product)" opacity="0.5" />
                  <circle cx="100" cy="125" r="6" fill="rgba(255,255,255,0.4)" />
                </svg>
                <!-- Suction -->
                <svg v-else-if="product.category === 'suction'" viewBox="0 0 200 250" class="card-product-svg">
                  <ellipse cx="100" cy="130" rx="42" ry="75" :fill="getProductColor(product)" opacity="0.55" />
                  <ellipse cx="100" cy="60" rx="28" ry="32" :fill="getProductColor(product)" opacity="0.45" />
                  <ellipse cx="100" cy="60" rx="16" ry="20" fill="rgba(0,0,0,0.15)" />
                  <circle cx="100" cy="135" r="9" fill="rgba(255,255,255,0.35)" />
                </svg>
                <!-- Rabbit -->
                <svg v-else-if="product.category === 'rabbit'" viewBox="0 0 200 250" class="card-product-svg">
                  <ellipse cx="62" cy="38" rx="13" ry="22" :fill="getProductColor(product)" opacity="0.6" transform="rotate(-15 62 38)" />
                  <ellipse cx="138" cy="38" rx="13" ry="22" :fill="getProductColor(product)" opacity="0.6" transform="rotate(15 138 38)" />
                  <path d="M62 75 Q58 115 65 170 Q100 200 135 170 Q142 115 138 75 Q120 88 100 88 Q80 88 62 75 Z"
                        :fill="getProductColor(product)" opacity="0.55" />
                </svg>
                <!-- Kegel -->
                <svg v-else-if="product.category === 'kegel'" viewBox="0 0 200 250" class="card-product-svg">
                  <circle cx="100" cy="60" r="28" :fill="getProductColor(product)" opacity="0.65" />
                  <circle cx="100" cy="130" r="35" :fill="getProductColor(product)" opacity="0.55" />
                  <circle cx="100" cy="200" r="32" :fill="getProductColor(product)" opacity="0.5" />
                </svg>
                <!-- Couples -->
                <svg v-else-if="product.category === 'couples'" viewBox="0 0 200 250" class="card-product-svg">
                  <ellipse cx="100" cy="125" rx="60" ry="25" :fill="getProductColor(product)" opacity="0.6" />
                  <ellipse cx="100" cy="125" rx="42" ry="16" fill="rgba(0,0,0,0.1)" />
                  <circle cx="165" cy="125" r="12" :fill="getProductColor(product)" opacity="0.7" />
                  <circle cx="35" cy="125" r="10" fill="rgba(255,255,255,0.3)" />
                </svg>
                <!-- Default -->
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
          <button class="quick-add-btn" @click="$emit('add-to-cart', product)">
            + Add
          </button>
        </div>
      </div>

      <div class="text-center mt-12 fade-in-up">
        <router-link to="/products" class="btn-primary">
          <span>View All Products</span>
          <svg viewBox="0 0 60 59" class="btn-arrow">
            <path d="M20.018,29.5h-8.663V3.5l43.645,26L11.355,55.5H0" fill="none" stroke="currentColor" stroke-miterlimit="10" />
          </svg>
        </router-link>
      </div>
    </section>

    <!-- Brand Values Icons -->
    <section class="values-section">
      <ul class="values-list">
        <li v-for="(brand, index) in brandValues" :key="index" class="value-item fade-in-up">
          <svg viewBox="0 0 45 45" class="value-icon" :style="{ fill: heroProducts[activeHeroIndex].color }">
            <path :d="brand.icon" />
          </svg>
          <span>{{ brand.name }}</span>
        </li>
      </ul>

      <ul class="info-list">
        <li class="fade-in"><h2>• Discreet Packaging & Shipping •</h2></li>
        <li class="fade-in"><h2>• Body-Safe Premium Materials •</h2></li>
        <li class="fade-in"><h2>• 30-Day Satisfaction Guarantee •</h2></li>
        <li class="fade-in"><h2>• 2 Year Warranty Included •</h2></li>
      </ul>
    </section>

    <!-- B2B Wholesale Banner -->
    <section class="wholesale-banner fade-in-up">
      <div class="wholesale-content">
        <h2 class="font-plaster wholesale-title">B2B Wholesale</h2>
        <p class="wholesale-desc">
          Partner with LUST8 for premium adult pleasure products. Competitive wholesale pricing, white-label OEM options, and discreet global shipping for retailers, distributors, and e-commerce brands worldwide.
        </p>
        <router-link to="/wholesale" class="btn-primary wholesale-btn">
          <span>Learn More</span>
          <svg viewBox="0 0 60 59" class="btn-arrow">
            <path d="M20.018,29.5h-8.663V3.5l43.645,26L11.355,55.5H0" fill="none" stroke="currentColor" stroke-miterlimit="10" />
          </svg>
        </router-link>
      </div>
    </section>

    <!-- Newsletter -->
    <section class="newsletter-signup">
      <div class="newsletter-texture"></div>
      <h2 class="font-plaster newsletter-title">Join the LUST8 community</h2>
      <p class="newsletter-desc tracking-widest text-center">
        Subscribe for exclusive deals, new arrivals, and 15% off your first order. Discreetly delivered to your inbox.
      </p>
      <form class="newsletter-form" @submit.prevent="handleNewsletter">
        <input type="email" placeholder="Enter Your Email" v-model="newsletterEmail" />
        <button type="submit">
          <svg viewBox="0 0 110 110">
            <path class="triangle" d="M19.654,77.903v-45.805l36.803,22.903-36.803,22.903v-45.805l36.803,22.903-36.803,22.903Z"
                  fill="none" :stroke="heroProducts[activeHeroIndex].color" stroke-miterlimit="10" stroke-width="3" />
            <path class="line" d="M19.654,5l80.346,50L19.654,105"
                  fill="none" :stroke="heroProducts[activeHeroIndex].color" stroke-miterlimit="10" stroke-width="3" />
            <path class="arrow" d="M100,55H0"
                  fill="none" :stroke="heroProducts[activeHeroIndex].color" stroke-miterlimit="10" stroke-width="3" />
          </svg>
        </button>
      </form>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { products, ingredients } from '../data/products.js'

// Hero product carousel - 3 signature products
const heroProducts = [
  {
    id: 8,
    name: 'Halo',
    tagline: 'Air Pulse Stimulator',
    color: '#dd5da2',
    // Suction stimulator icon
    iconSvg: `<ellipse cx="35" cy="55" rx="22" ry="28" />
             <ellipse cx="35" cy="35" rx="14" ry="16" fill="rgba(255,255,255,0.3)" />
             <circle cx="35" cy="25" r="6" fill="rgba(255,255,255,0.5)" />
             <path d="M18 55 Q35 65 52 55" fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="2" />`
  },
  {
    id: 1,
    name: 'Aura',
    tagline: 'Luxury Wand Massager',
    color: '#e5c000',
    // Wand massager icon
    iconSvg: `<ellipse cx="35" cy="20" rx="20" ry="18" />
             <path d="M20 35 Q18 60 22 80 Q35 88 48 80 Q52 60 50 35 Z" />
             <ellipse cx="35" cy="20" rx="14" ry="12" fill="rgba(255,255,255,0.3)" />
             <circle cx="35" cy="65" r="3" fill="rgba(255,255,255,0.5)" />`
  },
  {
    id: 6,
    name: 'Nocturne',
    tagline: 'Dual Rabbit Vibe',
    color: '#f29520',
    // Rabbit vibrator icon
    iconSvg: `<ellipse cx="35" cy="30" rx="16" ry="20" />
             <path d="M22 45 Q20 70 25 85 Q35 92 45 85 Q50 70 48 45 Z" />
             <ellipse cx="22" cy="25" rx="7" ry="10" />
             <ellipse cx="48" cy="25" rx="7" ry="10" />
             <path d="M26 55 Q35 62 44 55" fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="2" />`
  }
]

const activeHeroIndex = ref(1)
const spriteOffset = ref(0)
const dragPosition = ref(0)
const isDragging = ref(false)
const scrubberTrack = ref(null)
const scrubberDrag = ref(null)
const newsletterEmail = ref('')
const currentIngredientIndex = ref(0)

const featuredProducts = computed(() => products.slice(0, 6))

const displayIngredients = computed(() => ingredients.slice(0, 6))

const ingredientPositions = [
  { x: 525, y: 272 },   // top
  { x: 679, y: 405 },   // right-top
  { x: 760, y: 538 },   // right-mid
  { x: 679, y: 625 },   // right-btm
  { x: 371, y: 625 },   // left-btm
  { x: 290, y: 538 },   // left-mid
  { x: 371, y: 405 },   // left-top
  { x: 525, y: 625 },   // bottom
]

const connectLines = [
  { x1: 525, y1: 272, x2: 804, y2: 163 },
  { x1: 760, y1: 538, x2: 928, y2: 450 },
  { x1: 679, y1: 625, x2: 804, y2: 737 },
  { x1: 525, y1: 625, x2: 525, y2: 828 },
  { x1: 371, y1: 625, x2: 246, y2: 737 },
  { x1: 290, y1: 538, x2: 122, y2: 450 },
  { x1: 371, y1: 405, x2: 246, y2: 163 },
]

const currentIngredient = computed(() => ingredients[currentIngredientIndex.value])

const brandValues = computed(() => [
  { name: 'Body Safe', icon: 'M22.5 5 C15 5 10 12 10 20 C10 30 15 38 22.5 45 C30 38 35 30 35 20 C35 12 30 5 22.5 5 Z M22.5 25 C19 25 16 22 16 18 C16 14 19 11 22.5 11 C26 11 29 14 29 18 C29 22 26 25 22.5 25 Z' },
  { name: 'Medical Grade', icon: 'M18 10 L27 10 L27 18 L35 18 L35 27 L27 27 L27 35 L18 35 L18 27 L10 27 L10 18 L18 18 Z' },
  { name: 'Waterproof', icon: 'M22.5 5 C15 15 10 22 10 30 C10 37 15 42 22.5 42 C30 42 35 37 35 30 C35 22 30 15 22.5 5 Z M17 28 Q22.5 22 28 28 Q22.5 34 17 28 Z' },
  { name: 'Rechargeable', icon: 'M20 5 L15 25 L25 25 L20 45 L35 22 L25 22 L30 5 Z' },
  { name: 'Discreet Ship', icon: 'M5 15 L40 15 L40 38 L5 38 Z M5 15 L22.5 32 L40 15 M15 22 L20 22 M25 22 L30 22' },
  { name: '30-Day Return', icon: 'M22.5 5 C35 5 45 15 45 27.5 C45 40 35 45 22.5 45 C10 45 5 40 5 27.5 M15 22 L22.5 30 L30 22 M22.5 12 L22.5 30' },
  { name: '2Y Warranty', icon: 'M22.5 5 L22.5 15 M22.5 35 L22.5 45 M5 22.5 L15 22.5 M30 22.5 L40 22.5 M12 12 L19 19 M26 26 L33 33 M33 12 L26 19 M19 26 L12 33' },
  { name: '24/7 Support', icon: 'M22.5 5 C32 5 40 13 40 22.5 C40 32 32 40 22.5 40 C13 40 5 32 5 22.5 C5 13 13 5 22.5 5 Z M22.5 15 L22.5 25 L30 30' },
])

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

const getProductColor = (product) => {
  return colorMap[product.category] || '#dd5da2'
}

const nextProduct = () => {
  activeHeroIndex.value = (activeHeroIndex.value + 1) % heroProducts.length
  spriteOffset.value = 0
  dragPosition.value = 0
  currentIngredientIndex.value = (currentIngredientIndex.value + 1) % ingredients.length
}

const prevProduct = () => {
  activeHeroIndex.value = (activeHeroIndex.value - 1 + heroProducts.length) % heroProducts.length
  spriteOffset.value = 0
  dragPosition.value = 0
}

const setActiveHero = (index) => {
  activeHeroIndex.value = index
  spriteOffset.value = 0
  dragPosition.value = 0
  currentIngredientIndex.value = index % ingredients.length
}

// Scrubber drag
const startDrag = (e) => {
  isDragging.value = true
  updateDragPosition(e)
  window.addEventListener('mousemove', updateDragPosition)
  window.addEventListener('mouseup', stopDrag)
  window.addEventListener('touchmove', updateDragPosition)
  window.addEventListener('touchend', stopDrag)
}

const updateDragPosition = (e) => {
  if (!isDragging.value || !scrubberTrack.value) return
  const rect = scrubberTrack.value.getBoundingClientRect()
  const clientX = e.touches ? e.touches[0].clientX : e.clientX
  let x = clientX - rect.left - 30
  const maxX = rect.width - 60
  x = Math.max(0, Math.min(x, maxX))
  dragPosition.value = x
  spriteOffset.value = (x / maxX) * 500
}

const stopDrag = () => {
  isDragging.value = false
  window.removeEventListener('mousemove', updateDragPosition)
  window.removeEventListener('mouseup', stopDrag)
  window.removeEventListener('touchmove', updateDragPosition)
  window.removeEventListener('touchend', stopDrag)
}

const handleNewsletter = () => {
  alert(`Thanks for subscribing with ${newsletterEmail.value}!`)
  newsletterEmail.value = ''
}

// Auto-rotate ingredients
let ingredientInterval = null
onMounted(() => {
  ingredientInterval = setInterval(() => {
    currentIngredientIndex.value = (currentIngredientIndex.value + 1) % ingredients.length
  }, 4000)

  // Trigger scroll animations after load
  setTimeout(() => {
    document.querySelectorAll('.fade-in-up, .fade-in').forEach((el, i) => {
      setTimeout(() => el.classList.add('visible'), i * 100)
    })
  }, 1200)
})

onUnmounted(() => {
  if (ingredientInterval) clearInterval(ingredientInterval)
})
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 70px;
  width: 100%;
}

/* Hero Section */
.hero-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 2rem 1rem;
  position: relative;
}

.hero-subtitle {
  font-size: clamp(1rem, 2vw, 1.25rem);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: var(--color-text);
  margin: 1rem 0;
  opacity: 0;
}

.hero-subtitle.visible {
  opacity: 1;
  transition: opacity 1s ease;
}

/* Carousel */
.carousel-container {
  position: relative;
  width: 100%;
  max-width: 600px;
  margin: 2rem 0;
}

.carousel-line {
  position: absolute;
  top: 50%;
  left: 5px;
  width: calc(100% - 10px);
  height: 1px;
  background: var(--color-text);
  opacity: 0.2;
  border: none;
}

.carousel {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  position: relative;
  z-index: 1;
}

.carousel-btn {
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform var(--transition-base);
}

.carousel-btn:hover {
  transform: scale(1.1);
}

.arrow-icon {
  width: 50px;
  height: auto;
  fill: var(--color-flavor);
  transition: fill 0.6s ease;
}

.carousel-btn.next .arrow-icon {
  transform: rotate(180deg);
}

.fruit-list {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

.fruit-item {
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.fruit-icon {
  width: 50px;
  height: 70px;
}

.fruit-icon svg {
  width: 100%;
  height: 100%;
  fill: currentColor;
  transition: fill 0.6s ease;
}

.fruit-item.blur {
  filter: blur(1px);
}

/* Spin Section */
.spin-section {
  position: relative;
  margin: 2rem 0;
  width: 100%;
  max-width: 500px;
}

.spin-container {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3rem;
}

.product-display {
  width: 280px;
  height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  perspective: 1000px;
}

.product-sprite {
  display: flex;
  width: 100%;
  height: 100%;
  transition: transform 0.1s ease-out;
}

.product-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 280px;
}

.product-shape {
  width: 200px;
  height: 340px;
  border-radius: 50% 50% 45% 45% / 35% 35% 45% 45%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition: background 0.6s ease;
  filter: drop-shadow(0 20px 40px rgba(0,0,0,0.15));
}

.product-svg {
  width: 160px;
  height: 280px;
}

/* Scrubber */
.scrubber {
  width: 100%;
  max-width: 400px;
  padding: 0 30px;
}

.scrubber-track {
  position: relative;
  width: 100%;
  height: 4px;
  background: rgba(35, 31, 32, 0.1);
  border-radius: 2px;
  cursor: grab;
}

.scrubber-track:active {
  cursor: grabbing;
}

.scrubber-drag {
  position: absolute;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  width: 60px;
  height: 60px;
  margin-left: -30px;
  cursor: grab;
  touch-action: pan-y;
  user-select: none;
}

.scrubber-drag:active {
  cursor: grabbing;
}

.scrubber-drag svg {
  width: 100%;
  height: 100%;
}

/* Hero Title */
.hero-title {
  font-size: clamp(2.5rem, 7vw, 5rem);
  font-weight: 400;
  text-align: center;
  margin: 1rem 0;
  line-height: 1.1;
}

.hero-title span {
  display: block;
  font-size: 0.5em;
  opacity: 0.7;
  margin-top: 0.5rem;
}

/* Buy Button */
.buy-button {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  padding: 0.875rem 2.5rem;
  border: 2px solid var(--color-text);
  border-radius: 9999px;
  font-size: 1.125rem;
  font-weight: 500;
  color: var(--color-text);
  background: transparent;
  margin: 2rem 0 3rem;
  transition: all var(--transition-base);
  position: relative;
  overflow: hidden;
}

.buy-button:hover {
  background: var(--color-text);
  color: var(--color-bg);
  transform: translateY(-2px);
}

.buy-button svg {
  width: 30px;
  height: auto;
  transition: transform var(--transition-base);
}

.buy-button:hover svg {
  transform: translateX(4px);
}

/* Feature Bar */
.feature-bar {
  width: 100%;
  display: flex;
  justify-content: center;
  margin: 2rem 0 4rem;
}

.feature-svg {
  max-width: 500px;
  width: 90%;
  height: auto;
}

.feature-bg {
  transition: fill 0.6s ease;
}

/* Ingredients Section */
.ingredients-section {
  width: 100%;
  padding: 4rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.ingredients-geo {
  position: relative;
  width: 100%;
  max-width: 700px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.geo-svg {
  width: 100%;
  height: auto;
  max-height: 500px;
}

.feature-dot {
  transition: r 0.3s ease;
}

.feature-dot:hover {
  r: 6;
}

.ingredient-content {
  text-align: center;
  margin-top: 2rem;
  max-width: 600px;
}

.ingredient-title {
  font-size: clamp(1.5rem, 3vw, 2rem);
  margin-bottom: 0.5rem;
}

.ingredient-title span {
  display: block;
  font-family: var(--font-outfit);
  font-size: 0.6em;
  font-weight: 400;
  opacity: 0.7;
  margin-top: 0.25rem;
}

.ingredient-desc {
  font-size: 1rem;
  line-height: 1.7;
  color: var(--color-text-light);
}

/* Featured Products */
.featured-products {
  width: 100%;
  padding: 4rem 1.5rem;
  max-width: 1200px;
  margin: 0 auto;
}

.section-title {
  font-size: clamp(2rem, 4vw, 3rem);
  margin-bottom: 0.75rem;
}

.section-subtitle {
  font-size: 1.125rem;
  margin-bottom: 3rem;
  opacity: 0.7;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
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

.mt-12 {
  margin-top: 3rem;
}

.btn-arrow {
  width: 24px;
  height: auto;
}

/* Values Section */
.values-section {
  width: 100%;
  padding: 4rem 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3rem;
}

.values-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2.5rem;
  list-style: none;
  padding: 0;
  max-width: 900px;
}

.value-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.95rem;
  font-weight: 500;
  color: var(--color-text);
  text-align: center;
  min-width: 100px;
}

.value-icon {
  width: 45px;
  height: 45px;
  transition: transform var(--transition-base);
}

.value-item:hover .value-icon {
  transform: scale(1.15);
}

.info-list {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.info-list h2 {
  font-size: clamp(1rem, 2vw, 1.25rem);
  font-weight: 400;
  letter-spacing: 0.05em;
  opacity: 0.8;
}

/* Wholesale Banner */
.wholesale-banner {
  width: 100%;
  max-width: 1000px;
  margin: 4rem auto;
  padding: 0 1.5rem;
}

.wholesale-content {
  background: linear-gradient(135deg, var(--color-flavor) 0%, var(--color-flavor-dark) 100%);
  border-radius: 24px;
  padding: 3.5rem 2rem;
  text-align: center;
  color: white;
}

.wholesale-title {
  font-size: clamp(2rem, 4vw, 3rem);
  margin-bottom: 1rem;
  color: white;
}

.wholesale-desc {
  font-size: 1.05rem;
  max-width: 550px;
  margin: 0 auto 2rem;
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.7;
}

.wholesale-btn {
  background: white;
  color: var(--color-flavor);
}

.wholesale-btn:hover {
  background: var(--color-text);
  color: white;
  transform: translateY(-2px);
}

/* Newsletter */
.newsletter-signup {
  position: relative;
  width: 100%;
  padding: 4rem 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: hidden;
}

.newsletter-texture {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background:
    radial-gradient(ellipse at bottom, var(--color-flavor-light) 0%, transparent 60%);
  pointer-events: none;
}

.newsletter-title {
  font-size: clamp(1.75rem, 3.5vw, 2.5rem);
  margin-bottom: 1rem;
  position: relative;
  z-index: 1;
}

.newsletter-desc {
  font-size: 1rem;
  margin-bottom: 2rem;
  max-width: 500px;
  position: relative;
  z-index: 1;
}

.newsletter-form {
  display: flex;
  width: 100%;
  max-width: 450px;
  position: relative;
  z-index: 1;
}

.newsletter-form input {
  flex: 1;
  padding: 0.875rem 1.25rem;
  border: 2px solid var(--color-text);
  border-right: none;
  border-radius: 9999px 0 0 9999px;
  background: transparent;
  font-family: inherit;
  font-size: 1rem;
  color: var(--color-text);
  outline: none;
}

.newsletter-form input::placeholder {
  color: var(--color-text-light);
}

.newsletter-form button {
  width: 56px;
  height: 56px;
  border: 2px solid var(--color-text);
  border-left: none;
  border-radius: 0 9999px 9999px 0;
  background: var(--color-text);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all var(--transition-base);
}

.newsletter-form button:hover {
  background: var(--color-flavor);
  border-color: var(--color-flavor);
}

.newsletter-form button svg {
  width: 30px;
  height: 30px;
  transform: rotate(-45deg);
  transition: transform var(--transition-base);
}

.newsletter-form button:hover svg {
  transform: rotate(-45deg) scale(1.1);
}

@media (max-width: 768px) {
  .home {
    padding-top: 60px;
  }

  .hero-section {
    padding: 1rem 0.5rem;
  }

  .carousel-btn {
    width: 40px;
    height: 40px;
  }

  .arrow-icon {
    width: 35px;
  }

  .fruit-list {
    gap: 1rem;
  }

  .fruit-icon {
    width: 35px;
    height: 50px;
  }

  .product-display {
    width: 220px;
    height: 300px;
  }

  .product-shape {
    width: 160px;
    height: 280px;
  }

  .product-svg {
    width: 130px;
    height: 230px;
  }

  .scrubber {
    max-width: 300px;
  }

  .scrubber-drag {
    width: 50px;
    height: 50px;
    margin-left: -25px;
  }

  .product-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }

  .featured-products {
    padding: 2rem 1rem;
  }

  .values-list {
    gap: 1.5rem;
  }

  .value-item {
    min-width: 80px;
    font-size: 0.85rem;
  }

  .value-icon {
    width: 35px;
    height: 35px;
  }

  .wholesale-content {
    padding: 2.5rem 1.5rem;
  }

  .newsletter-form input {
    font-size: 0.9rem;
  }

  .newsletter-form button {
    width: 50px;
    height: 50px;
  }
}
</style>
