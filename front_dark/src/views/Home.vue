<template>
  <div class="home">
    <!-- ============ HERO SECTION ============ -->
    <section class="hero-section">
      <!-- Navigation arrows -->
      <button class="hero-arrow left" @click="prevHero" aria-label="Previous product">
        <svg viewBox="0 0 24 24" class="arrow-svg">
          <path d="M15 18l-6-6 6-6" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <button class="hero-arrow right" @click="nextHero" aria-label="Next product">
        <svg viewBox="0 0 24 24" class="arrow-svg">
          <path d="M9 18l6-6-6-6" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>

      <!-- Floating product -->
      <div v-if="heroProducts.length > 0" class="hero-product animate-hero-in-1">
        <div class="product-float animate-float" :key="activeHeroIndex">
          <svg :viewBox="heroProducts[activeHeroIndex].viewBox" class="product-hero-svg"
               :style="{ filter: `drop-shadow(0 30px 60px ${heroProducts[activeHeroIndex].glowColor})` }">
            <defs>
              <radialGradient :id="'heroGrad' + activeHeroIndex" cx="30%" cy="25%" r="70%">
                <stop offset="0%" stop-color="rgba(255,255,255,0.6)" />
                <stop offset="40%" stop-color="rgba(255,255,255,0.2)" />
                <stop offset="100%" stop-color="rgba(255,255,255,0)" />
              </radialGradient>
            </defs>
            <g v-html="heroProducts[activeHeroIndex].heroSvg"></g>
          </svg>
        </div>
      </div>
      <div v-else class="hero-product hero-skeleton">
        <div class="skeleton-box"></div>
      </div>

      <!-- Product wordmark / title -->
      <div class="hero-wordmark animate-hero-in-2">
        <h2 v-if="heroProducts.length > 0" class="wordmark-text">
          {{ heroProducts[activeHeroIndex].wordmark }}
        </h2>
        <h2 v-else class="wordmark-text">
          LUST8
        </h2>
      </div>

      <!-- Tagline -->
      <p class="hero-tagline text-title-serif animate-hero-in-3">
        {{ t.heroTagline[activeHeroIndex] || t.heroTaglineDefault }}
      </p>

      <!-- Price / Buy row -->
      <div class="hero-cta-row animate-hero-in-3">
        <span class="cta-label">{{ t.sizeLabel[activeHeroIndex] || t.premiumToy }}</span>
        <router-link
          v-if="heroProducts[activeHeroIndex]"
          :to="`/products/${heroProducts[activeHeroIndex].slug}`"
          class="cta-buy-btn"
        >
          <span class="cta-price">${{ heroProducts[activeHeroIndex].price }}</span>
          <span class="cta-action">{{ t.shopNow }}</span>
        </router-link>
        <router-link v-else to="/products" class="cta-buy-btn">
          <span class="cta-action">{{ t.shopNow }}</span>
        </router-link>
        <span class="cta-label">{{ t.clubKey }}</span>
      </div>
    </section>

    <!-- ============ PERFORMANCE KEY SECTION (Light / Paper) ============ -->
    <section class="perf-section noise-overlay">
      <div class="perf-content">
        <h1 class="perf-title text-section-display" v-html="t.pleasureKeyTitle.replace(/\n/, '<br/>')"></h1>

        <div class="perf-features">
          <div class="perf-feature">
            <div class="perf-icon-wrap">
              <svg viewBox="0 0 24 24" class="perf-icon">
                <path d="M4 7h16M4 12h16M4 17h10" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/>
                <rect x="3" y="4" width="18" height="16" rx="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
              </svg>
            </div>
            <h3 class="perf-feature-title">{{ t.perfBodySafe }}</h3>
            <p class="perf-feature-desc" v-html="t.perfBodySafeDesc.replace(/\n/, '<br/>')"></p>
          </div>

          <div class="perf-feature">
            <div class="perf-icon-wrap">
              <svg viewBox="0 0 24 24" class="perf-icon">
                <path d="M13 2L3 14h7l-1 8 10-12h-7l1-8z" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linejoin="round"/>
              </svg>
            </div>
            <h3 class="perf-feature-title">{{ t.perfQuiet }}</h3>
            <p class="perf-feature-desc" v-html="t.perfQuietDesc.replace(/\n/, '<br/>')"></p>
          </div>

          <div class="perf-feature">
            <div class="perf-icon-wrap">
              <svg viewBox="0 0 24 24" class="perf-icon">
                <path d="M12 2L2 7v10l10 5 10-5V7L12 2z" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linejoin="round"/>
                <path d="M2 7l10 5 10-5" stroke="currentColor" stroke-width="1.5" fill="none"/>
                <path d="M12 12v10" stroke="currentColor" stroke-width="1.5" fill="none"/>
              </svg>
            </div>
            <h3 class="perf-feature-title">{{ t.perfAccess }}</h3>
            <p class="perf-feature-desc" v-html="t.perfAccessDesc.replace(/\n/, '<br/>')"></p>
          </div>
        </div>
      </div>

      <!-- Floating product at bottom -->
      <div class="perf-product-img">
        <svg viewBox="0 0 400 300" class="perf-product-svg" :style="{ filter: 'drop-shadow(0 20px 40px rgba(0,0,0,0.1))' }">
          <defs>
            <linearGradient id="perfGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#2d2d2d" />
              <stop offset="50%" stop-color="#1a1a1a" />
              <stop offset="100%" stop-color="#0d0d0d" />
            </linearGradient>
          </defs>
          <!-- Sleek wand product -->
          <ellipse cx="200" cy="70" rx="55" ry="60" fill="url(#perfGrad)" />
          <path d="M160 120 Q150 180 155 250 Q200 270 245 250 Q250 180 240 120 Z" fill="url(#perfGrad)" />
          <circle cx="200" cy="180" r="8" fill="rgba(255,255,255,0.2)" />
          <circle cx="200" cy="210" r="6" fill="rgba(255,255,255,0.15)" />
        </svg>
      </div>
    </section>

    <!-- ============ ALWAYS WITH YOU SECTION ============ -->
    <section class="showcase-section">
      <div class="showcase-bg">
        <svg viewBox="0 0 800 600" class="showcase-bg-svg">
          <defs>
            <radialGradient id="showcaseGlow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" :stop-color="activeShowcaseProduct?.glowColor || 'rgba(221, 93, 162, 0.3)'" />
              <stop offset="100%" stop-color="rgba(28,28,28,0)" />
            </radialGradient>
          </defs>
          <rect width="800" height="600" fill="url(#showcaseGlow)" />
        </svg>
      </div>

      <div class="showcase-content">
        <span class="section-label font-mono">{{ t.alwaysWithYou }}</span>
        <h2 class="section-title text-section-display">{{ t.potgTitle }}</h2>
        <p class="section-subtitle text-title-serif">
          {{ t.potgDesc }}
        </p>
      </div>

      <!-- Large product display -->
      <div v-if="heroProducts.length > 0" class="showcase-product">
        <div class="showcase-product-inner" :key="'showcase-' + activeShowcaseIndex">
          <svg :viewBox="activeShowcaseProduct.viewBox" class="showcase-product-svg"
               :style="{ filter: `drop-shadow(0 40px 80px ${activeShowcaseProduct.glowColor})` }">
            <g v-html="activeShowcaseProduct.heroSvg"></g>
          </svg>
        </div>
      </div>
    </section>

    <!-- ============ FEATURE CAROUSEL SECTION ============ -->
    <section class="carousel-section">
      <div class="carousel-container">
        <div class="carousel-row">
          <div
            v-for="(slide, index) in carouselSlides"
            :key="index"
            class="carousel-slide"
            :class="{ active: activeSlideIndex === index }"
            @click="activeSlideIndex = index"
          >
            <div
              class="slide-img-wrap"
              :style="{
                background: `
                radial-gradient(ellipse at 20% 15%, ${slide.color}22 0%, transparent 50%),
                radial-gradient(ellipse at 80% 85%, ${slide.colorDark}33 0%, transparent 55%),
                linear-gradient(160deg, ${slide.bgTop} 0%, ${slide.bgBottom} 100%)
              `
              }"
            >
              <div class="slide-ambient" :style="{ background: `radial-gradient(ellipse at 50% 60%, ${slide.color}30 0%, transparent 60%)` }"></div>
              <svg :viewBox="slide.viewBox" class="slide-svg">
                <defs>
                  <linearGradient :id="'slideGrad' + index" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" :stop-color="slide.colorLight" />
                    <stop offset="50%" :stop-color="slide.color" />
                    <stop offset="100%" :stop-color="slide.colorDark" />
                  </linearGradient>
                  <radialGradient :id="'slideHL' + index" cx="30%" cy="25%" r="60%">
                    <stop offset="0%" stop-color="rgba(255,255,255,0.6)" />
                    <stop offset="50%" stop-color="rgba(255,255,255,0.2)" />
                    <stop offset="100%" stop-color="rgba(255,255,255,0)" />
                  </radialGradient>
                </defs>
                <g v-html="slide.svgContent.replace(/slideGrad/g, 'slideGrad' + index).replace(/slideHL/g, 'slideHL' + index)"></g>
              </svg>
              <div class="slide-reflection" :style="{ background: `linear-gradient(to top, ${slide.color}10 0%, transparent 100%)` }"></div>
            </div>
          </div>
        </div>

        <!-- Caption that follows active slide -->
        <div
          class="carousel-caption"
          :style="{ left: captionPosition }"
        >
          <span class="section-label font-mono">{{ t.carousel[activeSlideIndex]?.label }}</span>
          <h2 class="text-section-display carousel-title">
            {{ t.carousel[activeSlideIndex]?.title }}
          </h2>
          <p class="text-title-serif carousel-desc">
            {{ t.carousel[activeSlideIndex]?.desc }}
          </p>
        </div>
      </div>
    </section>

    <!-- ============ STATS / CAPACITY SECTION (Light) ============ -->
    <section class="stats-section noise-overlay">
      <div class="stats-content">
        <span class="section-label font-mono">{{ t.twentyPatterns }}</span>
        <h2 class="text-section-display">{{ t.sensationsTitle }}</h2>
        <p class="stats-desc text-title-serif" v-html="t.sensationsDesc.replace(/\n/, '<br/>')"></p>
      </div>
      <div class="stats-visual">
        <!-- Vibration pattern visualization -->
        <div class="wave-container fade-in-up">
          <svg viewBox="0 0 600 240" class="wave-svg">
            <!-- Wave 1 - soft -->
            <path d="M0,120 Q75,80 150,120 T300,120 T450,120 T600,120"
                  stroke="currentColor" stroke-width="1.5" fill="none" opacity="0.25"/>
            <!-- Wave 2 - medium -->
            <path d="M0,120 Q75,60 150,120 T300,120 T450,120 T600,120"
                  stroke="currentColor" stroke-width="1.5" fill="none" opacity="0.4"/>
            <!-- Wave 3 - intense -->
            <path d="M0,120 Q75,40 150,120 T300,120 T450,120 T600,120"
                  stroke="currentColor" stroke-width="2" fill="none"/>
            <!-- Dots -->
            <circle cx="150" cy="120" r="6" fill="currentColor"/>
            <circle cx="300" cy="120" r="6" fill="currentColor" opacity="0.5"/>
            <circle cx="450" cy="120" r="6" fill="currentColor" opacity="0.25"/>
            <!-- Labels -->
            <text x="150" y="170" text-anchor="middle" class="wave-label" font-family="var(--font-mono)" font-size="11" fill="currentColor" opacity="0.6">SOFT</text>
            <text x="300" y="170" text-anchor="middle" class="wave-label" font-family="var(--font-mono)" font-size="11" fill="currentColor" opacity="0.6">MEDIUM</text>
            <text x="450" y="170" text-anchor="middle" class="wave-label" font-family="var(--font-mono)" font-size="11" fill="currentColor" opacity="0.6">INTENSE</text>
          </svg>
        </div>
      </div>
    </section>

    <!-- ============ UNLOCK / APP SECTION ============ -->
    <section class="unlock-section">
      <div class="unlock-content">
        <span class="section-label font-mono">{{ t.unlock }}</span>
        <h2 class="text-section-display">{{ t.tapPlay }}</h2>
        <p class="unlock-desc text-title-serif" v-html="t.tapPlayDesc.replace(/\n/, '<br/>')"></p>
        <div class="unlock-platform">
          <svg viewBox="0 0 24 24" class="platform-icon">
            <path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83" fill="currentColor"/>
            <path d="M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z" fill="currentColor"/>
          </svg>
          <span>{{ t.iosAndroid }}</span>
        </div>
      </div>
    </section>

    <!-- ============ BOTTOM CTA SECTION ============ -->
    <section class="bottom-cta">
      <!-- Background glow -->
      <div class="bottom-cta-glow"
           :style="{ background: `radial-gradient(ellipse at center top, ${heroProducts[activeHeroIndex]?.glowColor || 'rgba(221, 93, 162, 0.4)'} 0%, transparent 60%)` }">
      </div>

      <!-- Product image -->
      <div v-if="heroProducts.length > 0" class="bottom-cta-product fade-in-up" :key="'btm-' + activeHeroIndex">
        <svg :viewBox="heroProducts[activeHeroIndex].viewBox" class="bottom-product-svg"
             :style="{ filter: `drop-shadow(0 20px 40px ${heroProducts[activeHeroIndex].glowColor})` }">
          <g v-html="heroProducts[activeHeroIndex].heroSvg"></g>
        </svg>
      </div>

      <div class="bottom-cta-wordmark">
        <h2 v-if="heroProducts[activeHeroIndex]" class="wordmark-text large">
          {{ heroProducts[activeHeroIndex].wordmark }}
        </h2>
        <h2 v-else class="wordmark-text large">LUST8</h2>
      </div>
      <p class="cta-bottom-text text-title-serif">
        {{ t.limitedSupply }}
      </p>
      <div class="hero-cta-row">
        <span class="cta-label">{{ t.sizeLabel[activeHeroIndex] || t.premiumToy }}</span>
        <router-link
          v-if="heroProducts[activeHeroIndex]"
          :to="`/products/${heroProducts[activeHeroIndex].slug}`"
          class="cta-buy-btn"
        >
          <span class="cta-price">${{ heroProducts[activeHeroIndex].price }}</span>
          <span class="cta-action">{{ t.shopNow }}</span>
        </router-link>
        <router-link v-else to="/products" class="cta-buy-btn">
          <span class="cta-action">{{ t.shopNow }}</span>
        </router-link>
        <span class="cta-label">{{ t.clubKey }}</span>
      </div>
      <div class="view-all-link">
        <router-link to="/products">{{ t.viewAllProducts }}</router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, inject } from 'vue'
import { getFeaturedProducts } from '../api/products'
import { useScrollAnimation } from '../composables/useScrollAnimation'

const lang = inject('lang', ref('en'))
const { refreshObserver } = useScrollAnimation()

// Featured products data from API
const featuredProducts = ref([])
const loading = ref(true)

// Hero product display config (visual SVGs)
// These are the 3 signature products mapped by slug
const heroProductConfigs = {
  'halo-clitoral': {
    wordmark: 'H A L O',
    accentColor: '#dd5da2',
    glowColor: 'rgba(221, 93, 162, 0.4)',
    viewBox: '0 0 300 400',
    heroSvg: `
      <defs>
        <linearGradient id="haloBody0" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#dd5da2" stop-opacity="0.9"/>
          <stop offset="40%" stop-color="#c94a8e" stop-opacity="0.85"/>
          <stop offset="100%" stop-color="#a03070" stop-opacity="0.9"/>
        </linearGradient>
        <radialGradient id="haloHighlight0" cx="30%" cy="20%" r="60%">
          <stop offset="0%" stop-color="rgba(255,255,255,0.7)" />
          <stop offset="50%" stop-color="rgba(255,255,255,0.2)" />
          <stop offset="100%" stop-color="rgba(255,255,255,0)" />
        </radialGradient>
        <radialGradient id="haloInner0" cx="50%" cy="60%" r="50%">
          <stop offset="0%" stop-color="#1a0a14" stop-opacity="0.8"/>
          <stop offset="100%" stop-color="#2d1524" stop-opacity="0.6"/>
        </radialGradient>
      </defs>
      <ellipse cx="150" cy="220" rx="70" ry="130" fill="url(#haloBody0)" />
      <ellipse cx="150" cy="100" rx="50" ry="55" fill="url(#haloBody0)" />
      <ellipse cx="150" cy="100" rx="34" ry="38" fill="url(#haloInner0)" />
      <ellipse cx="150" cy="110" rx="28" ry="28" fill="rgba(0,0,0,0.3)" />
      <ellipse cx="100" cy="190" rx="20" ry="70" fill="url(#haloHighlight0)" transform="rotate(-12 100 190)" />
      <circle cx="150" cy="225" r="18" fill="rgba(255,255,255,0.15)" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
      <circle cx="150" cy="225" r="10" fill="rgba(255,255,255,0.3)" />
      <rect x="135" y="340" width="30" height="12" rx="6" fill="rgba(0,0,0,0.3)" />
      <ellipse cx="150" cy="100" rx="52" ry="57" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="2" />
    `
  },
  'aura-wand': {
    wordmark: 'A U R A',
    accentColor: '#e5c000',
    glowColor: 'rgba(229, 192, 0, 0.4)',
    viewBox: '0 0 300 450',
    heroSvg: `
      <defs>
        <linearGradient id="wandBody1" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#f5d300" stop-opacity="0.9"/>
          <stop offset="40%" stop-color="#e5c000" stop-opacity="0.85"/>
          <stop offset="100%" stop-color="#c9a800" stop-opacity="0.9"/>
        </linearGradient>
        <radialGradient id="wandHeadHighlight1" cx="30%" cy="25%" r="60%">
          <stop offset="0%" stop-color="rgba(255,255,255,0.8)" />
          <stop offset="50%" stop-color="rgba(255,255,255,0.25)" />
          <stop offset="100%" stop-color="rgba(255,255,255,0)" />
        </radialGradient>
      </defs>
      <ellipse cx="150" cy="70" rx="65" ry="70" fill="url(#wandBody1)" />
      <ellipse cx="150" cy="70" rx="65" ry="70" fill="url(#wandHeadHighlight1)" />
      <path d="M115 130 Q108 170 115 220 Q150 240 185 220 Q192 170 185 130 Z" fill="url(#wandBody1)" />
      <path d="M108 220 Q100 300 108 380 Q150 400 192 380 Q200 300 192 220 Z" fill="url(#wandBody1)" />
      <path d="M115 220 Q108 300 115 380 Q120 400 125 380 Q118 300 122 220 Z" fill="rgba(255,255,255,0.2)" />
      <circle cx="150" cy="270" r="14" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.3)" stroke-width="1"/>
      <circle cx="150" cy="270" r="7" fill="rgba(255,255,255,0.4)" />
      <circle cx="150" cy="310" r="12" fill="rgba(255,255,255,0.15)" />
      <ellipse cx="150" cy="380" rx="42" ry="18" fill="rgba(0,0,0,0.15)" />
    `
  },
  'nocturne-rabbit': {
    wordmark: 'N O C T U R N E',
    accentColor: '#f29520',
    glowColor: 'rgba(242, 149, 32, 0.4)',
    viewBox: '0 0 300 420',
    heroSvg: `
      <defs>
        <linearGradient id="rabbitBody2" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#ffb347" stop-opacity="0.9"/>
          <stop offset="40%" stop-color="#f29520" stop-opacity="0.85"/>
          <stop offset="100%" stop-color="#d97a00" stop-opacity="0.9"/>
        </linearGradient>
        <radialGradient id="rabbitHighlight2" cx="30%" cy="20%" r="60%">
          <stop offset="0%" stop-color="rgba(255,255,255,0.7)" />
          <stop offset="50%" stop-color="rgba(255,255,255,0.2)" />
          <stop offset="100%" stop-color="rgba(255,255,255,0)" />
        </radialGradient>
      </defs>
      <ellipse cx="100" cy="60" rx="20" ry="35" fill="url(#rabbitBody2)" transform="rotate(-22 100 60)" />
      <ellipse cx="200" cy="60" rx="20" ry="35" fill="url(#rabbitBody2)" transform="rotate(22 200 60)" />
      <ellipse cx="92" cy="55" rx="8" ry="20" fill="rgba(255,255,255,0.3)" transform="rotate(-22 92 55)" />
      <ellipse cx="192" cy="55" rx="8" ry="20" fill="rgba(255,255,255,0.3)" transform="rotate(-22 192 55)" />
      <path d="M90 95 Q82 170 90 260 Q100 330 150 370 Q200 330 210 260 Q218 170 210 95 Q185 115 150 115 Q115 115 90 95 Z" fill="url(#rabbitBody2)" />
      <path d="M100 100 Q92 170 100 260 Q105 320 115 350 Q105 320 110 260 Q118 170 112 105 Z" fill="rgba(255,255,255,0.18)" />
      <ellipse cx="225" cy="160" rx="20" ry="28" fill="url(#rabbitBody2)" transform="rotate(35 225 160)" />
      <ellipse cx="220" cy="155" rx="8" ry="15" fill="rgba(255,255,255,0.25)" transform="rotate(35 220 155)" />
      <circle cx="115" cy="275" r="10" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.3)" stroke-width="1"/>
      <circle cx="115" cy="305" r="9" fill="rgba(255,255,255,0.15)" />
      <ellipse cx="150" cy="370" rx="30" ry="15" fill="rgba(255,255,255,0.1)" />
    `
  },
}

const heroProducts = computed(() => {
  // Map featured products with hero visual configs
  return featuredProducts.value
    .filter((p) => heroProductConfigs[p.slug])
    .map((p) => ({
      ...p,
      ...heroProductConfigs[p.slug],
    }))
    .slice(0, 3)
})

const activeHeroIndex = ref(0)
const activeSlideIndex = ref(2)

// ===== I18N =====
const t = computed(() => ({
  selectVibe: lang.value === 'en' ? 'Select your vibe' : '选择你的玩具',
  join: lang.value === 'en' ? 'Join' : '加入',
  heroTaglineDefault: lang.value === 'en' ? 'Premium intimate wellness products.' : '高端情趣健康产品。',
  premiumToy: lang.value === 'en' ? 'Premium Toy' : '高端玩具',
  heroTagline: heroProducts.value.map((p) => p.tagline),
  sizeLabel: heroProducts.value.map((p) => p.tagline),
  shopNow: lang.value === 'en' ? 'Shop now' : '立即购买',
  clubKey: lang.value === 'en' ? 'Club Key' : '会员密钥',
  pleasureKeyTitle: lang.value === 'en' ? "LUST8's\nPleasure Key" : "LUST8 的\n愉悦密钥",
  perfBodySafe: lang.value === 'en' ? 'BODY-SAFE' : '身体安全',
  perfBodySafeDesc: lang.value === 'en' ? 'Medical-grade silicone, crafted\nfor the most intimate moments.' : '医疗级硅胶，为最亲密的时刻而打造。',
  perfQuiet: lang.value === 'en' ? 'WHISPER-QUIET' : '静音设计',
  perfQuietDesc: lang.value === 'en' ? 'Advanced noise-dampening motors\nfor completely discreet play.' : '先进的降噪马达，让玩耍完全私密。',
  perfAccess: lang.value === 'en' ? 'LUST8 ACCESS' : 'LUST8 会员',
  perfAccessDesc: lang.value === 'en' ? 'Each toy unlocks our private\ncommunity of pleasure seekers.' : '每个玩具都解锁我们的私密愉悦社区。',
  alwaysWithYou: lang.value === 'en' ? 'ALWAYS WITH YOU' : '随身携带',
  potgTitle: lang.value === 'en' ? 'Pleasure on the Go' : '随时随地的愉悦',
  potgDesc: lang.value === 'en' ? 'A compact companion that goes\nwherever you go.' : '小巧伴侣，陪你去任何地方。',
  portablePleasure: lang.value === 'en' ? 'PORTABLE PLEASURE' : '便携愉悦',
  feelFaster: lang.value === 'en' ? 'Feel Faster' : '更快感受',
  twentyPatterns: lang.value === 'en' ? '20+ VIBRATION PATTERNS' : '20+ 种震动模式',
  sensationsTitle: lang.value === 'en' ? 'Sensations for Every Mood' : '每种心情的感觉',
  sensationsDesc: lang.value === 'en' ? '20 patterns, 8 speeds, or infinity with app control —\nfind exactly what you\'re looking for.' : '20 种模式、8 种速度，或通过应用无限控制——找到你想要的。',
  unlock: lang.value === 'en' ? 'UNLOCK NEW PLEASURES' : '解锁新的愉悦',
  tapPlay: lang.value === 'en' ? 'Tap & Play' : '点击即玩',
  tapPlayDesc: lang.value === 'en' ? 'Connect your toy to share vibes and discover\npeople who like what you like.' : '连接你的玩具，分享震动，发现和你兴趣相投的人。',
  iosAndroid: lang.value === 'en' ? 'iOS & Android App' : 'iOS 和安卓应用',
  limitedSupply: lang.value === 'en' ? 'Limited supply available.' : '限量供应。',
  viewAllProducts: lang.value === 'en' ? 'or View All Products →' : '或查看全部产品 →',
  carousel: [
    {
      label: lang.value === 'en' ? 'LUXURY DESIGN' : '奢华设计',
      title: lang.value === 'en' ? 'Crafted for Pleasure' : '为愉悦而造',
      desc: lang.value === 'en' ? 'Sleek ergonomic design that fits perfectly in your hand.' : '符合人体工学的流畅设计，完美贴合你的手。'
    },
    {
      label: lang.value === 'en' ? 'BODY SAFE' : '身体安全',
      title: lang.value === 'en' ? 'Pure Silicone' : '纯硅胶',
      desc: lang.value === 'en' ? 'Medical-grade platinum-cured silicone for total peace of mind.' : '医疗级铂金固化硅胶，让你完全放心。'
    },
    {
      label: lang.value === 'en' ? 'WHISPER QUIET' : '静音设计',
      title: lang.value === 'en' ? 'Silent Power' : '静音动力',
      desc: lang.value === 'en' ? 'Noise-dampening motors for completely discreet play sessions.' : '降噪马达，让玩耍完全私密。'
    },
    {
      label: lang.value === 'en' ? 'APP CONNECTED' : '智能连接',
      title: lang.value === 'en' ? 'Smart Control' : '智能控制',
      desc: lang.value === 'en' ? 'Custom patterns, long-distance play, and so much more.' : '自定义模式、远程玩耍，以及更多功能。'
    }
  ]
}))

// Carousel slides data - 4 product showcase cards
const carouselSlides = [
  {
    color: '#dd5da2',
    colorLight: '#ff7bb8',
    colorDark: '#c94a8e',
    bgTop: '#2a1520',
    bgBottom: '#1a0d14',
    viewBox: '0 0 300 400',
    heroIndex: 0,
    svgContent: `
      <ellipse cx="150" cy="220" rx="75" ry="130" fill="url(#slideGrad)" />
      <ellipse cx="150" cy="110" rx="52" ry="58" fill="url(#slideGrad)" />
      <ellipse cx="150" cy="110" rx="36" ry="42" fill="rgba(0,0,0,0.15)" />
      <ellipse cx="100" cy="190" rx="22" ry="70" fill="url(#slideHL)" transform="rotate(-12 100 190)" />
      <circle cx="150" cy="230" r="16" fill="rgba(255,255,255,0.25)" stroke="rgba(255,255,255,0.3)" stroke-width="1"/>
      <circle cx="150" cy="230" r="8" fill="rgba(255,255,255,0.4)" />
    `
  },
  {
    color: '#e5c000',
    colorLight: '#f5d830',
    colorDark: '#c9a800',
    bgTop: '#2a2510',
    bgBottom: '#1a180a',
    viewBox: '0 0 300 450',
    heroIndex: 1,
    svgContent: `
      <ellipse cx="150" cy="70" rx="60" ry="65" fill="url(#slideGrad)" />
      <ellipse cx="150" cy="70" rx="60" ry="65" fill="url(#slideHL)" />
      <path d="M108 125 Q100 200 108 300 Q150 320 192 300 Q200 200 192 125 Z" fill="url(#slideGrad)" />
      <path d="M115 130 Q108 200 115 300 Q120 320 125 300 Q118 200 122 130 Z" fill="rgba(255,255,255,0.2)" />
      <circle cx="150" cy="230" r="12" fill="rgba(255,255,255,0.3)" />
      <circle cx="150" cy="270" r="10" fill="rgba(255,255,255,0.2)" />
    `
  },
  {
    color: '#f29520',
    colorLight: '#ffb347',
    colorDark: '#d97a00',
    bgTop: '#2a1d10',
    bgBottom: '#1a140a',
    viewBox: '0 0 300 420',
    heroIndex: 2,
    svgContent: `
      <ellipse cx="95" cy="55" rx="18" ry="32" fill="url(#slideGrad)" transform="rotate(-22 95 55)" />
      <ellipse cx="205" cy="55" rx="18" ry="32" fill="url(#slideGrad)" transform="rotate(22 205 55)" />
      <path d="M85 95 Q78 170 85 260 Q95 330 150 370 Q205 330 215 260 Q222 170 215 95 Q190 115 150 115 Q110 115 85 95 Z" fill="url(#slideGrad)" />
      <path d="M95 100 Q88 170 95 260 Q100 320 110 350 Q100 320 105 260 Q112 170 107 105 Z" fill="rgba(255,255,255,0.2)" />
      <ellipse cx="228" cy="155" rx="18" ry="25" fill="url(#slideGrad)" transform="rotate(35 228 155)" />
      <circle cx="110" cy="280" r="10" fill="rgba(255,255,255,0.3)" />
    `
  },
  {
    color: '#8b5cf6',
    colorLight: '#a78bfa',
    colorDark: '#7c3aed',
    bgTop: '#1e1a2e',
    bgBottom: '#12101d',
    viewBox: '0 0 300 400',
    heroIndex: 0,
    svgContent: `
      <ellipse cx="150" cy="200" rx="80" ry="35" fill="url(#slideGrad)" />
      <ellipse cx="150" cy="200" rx="60" ry="22" fill="rgba(0,0,0,0.1)" />
      <ellipse cx="150" cy="200" rx="80" ry="35" fill="url(#slideHL)" />
      <circle cx="240" cy="200" r="22" fill="url(#slideGrad)" />
      <circle cx="240" cy="200" r="14" fill="rgba(255,255,255,0.3)" />
      <circle cx="60" cy="200" r="16" fill="rgba(255,255,255,0.25)" />
    `
  }
]

// Calculate caption position based on active slide
const captionPosition = computed(() => {
  const positions = ['12.5%', '37.5%', '62.5%', '87.5%']
  return positions[activeSlideIndex.value] || '50%'
})

// Active showcase product (linked to carousel selection)
const activeShowcaseIndex = computed(() => {
  const idx = carouselSlides[activeSlideIndex.value]?.heroIndex ?? 0
  return Math.min(idx, heroProducts.value.length - 1 >= 0 ? heroProducts.value.length - 1 : 0)
})

const activeShowcaseProduct = computed(() => heroProducts.value[activeShowcaseIndex.value] || heroProducts.value[0] || {})

const nextHero = () => {
  if (heroProducts.value.length === 0) return
  activeHeroIndex.value = (activeHeroIndex.value + 1) % heroProducts.value.length
}

const prevHero = () => {
  if (heroProducts.value.length === 0) return
  activeHeroIndex.value = (activeHeroIndex.value - 1 + heroProducts.value.length) % heroProducts.value.length
}

// Auto-rotate
let autoRotate = null

const loadFeaturedProducts = async () => {
  try {
    const data = await getFeaturedProducts(12, lang.value)
    featuredProducts.value = data
    loading.value = false

    // Ensure active index is within bounds
    if (activeHeroIndex.value >= heroProducts.value.length) {
      activeHeroIndex.value = 0
    }

    // Refresh animations after data loads
    setTimeout(() => refreshObserver(), 100)
  } catch (err) {
    console.error('Failed to load featured products:', err.message)
    loading.value = false
  }
}

onMounted(() => {
  loadFeaturedProducts()

  autoRotate = setInterval(() => {
    nextHero()
  }, 5000)

  // Init scroll animations after a brief delay
  setTimeout(() => {
    refreshObserver()
  }, 300)
})

onUnmounted(() => {
  if (autoRotate) clearInterval(autoRotate)
})
</script>

<style scoped>
.home {
  width: 100%;
  background-color: var(--color-bg);
}

.hero-skeleton {
  display: flex;
  align-items: center;
  justify-content: center;
}

.skeleton-box {
  width: 200px;
  height: 300px;
  background: linear-gradient(90deg, rgba(255,255,255,0.05) 25%, rgba(255,255,255,0.1) 50%, rgba(255,255,255,0.05) 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 20px;
}

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

/* ========== HERO SECTION ========== */
.hero-section {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  width: 100%;
  padding: 100px 20px 80px;
  gap: 24px;
  overflow: hidden;
}

/* Hero background glow */
.hero-section::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -60%);
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(221, 93, 162, 0.12) 0%, transparent 65%);
  pointer-events: none;
  z-index: 0;
}

.hero-arrow {
  position: absolute;
  top: 40%;
  transform: translateY(-50%);
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-tertiary);
  transition: all var(--transition-base);
  z-index: 10;
  border-radius: 50%;
  background: none;
  border: none;
  cursor: pointer;
}

.hero-arrow.left { left: 60px; }
.hero-arrow.right { right: 60px; }

.hero-arrow:hover {
  color: var(--color-text);
  transform: translateY(-50%) scale(1.15);
  background: rgba(255, 255, 255, 0.05);
}

.arrow-svg {
  width: 32px;
  height: 32px;
}

/* Hero product */
.hero-product {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 900px;
  height: 420px;
  margin-bottom: -20px;
}

.product-float {
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.8s cubic-bezier(0.22, 1, 0.36, 1);
}

.product-hero-svg {
  width: auto;
  height: 400px;
  transition: all 0.6s ease;
}

/* Wordmark */
.hero-wordmark {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 1000px;
  display: flex;
  justify-content: center;
}

.wordmark-text {
  font-family: var(--font-sans);
  font-size: clamp(3.5rem, 11vw, 8rem);
  font-weight: 200;
  letter-spacing: 0.25em;
  color: var(--color-text);
  text-align: center;
  line-height: 1;
  text-shadow: 0 0 80px rgba(255, 255, 255, 0.08);
}

.wordmark-text.large {
  font-size: clamp(2.5rem, 8vw, 5.5rem);
  font-weight: 200;
}

/* Tagline */
.hero-tagline {
  color: var(--color-text);
  text-align: center;
  margin: 0;
  font-size: clamp(1.25rem, 2.5vw, 1.75rem);
}

/* CTA Row */
.hero-cta-row {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-top: 10px;
}

.cta-label {
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--color-text-secondary);
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.cta-buy-btn {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 12px 24px;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.12);
  transition: all var(--transition-base);
  color: var(--color-text);
  text-decoration: none;
}

.cta-buy-btn:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateY(-2px);
  opacity: 1;
}

.cta-price {
  font-family: var(--font-sans);
  font-size: 16px;
  font-weight: 600;
  color: var(--color-text);
}

.cta-action {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding-left: 12px;
  border-left: 1px solid rgba(255, 255, 255, 0.15);
}

/* ========== PERFORMANCE KEY SECTION ========== */
.perf-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  padding: 100px 80px 0;
  background-color: var(--color-paper);
  background-image:
    radial-gradient(ellipse at 15% 25%, rgba(180, 150, 120, 0.3) 0%, transparent 45%),
    radial-gradient(ellipse at 85% 15%, rgba(200, 180, 150, 0.25) 0%, transparent 45%),
    radial-gradient(ellipse at 50% 100%, rgba(150, 120, 90, 0.3) 0%, transparent 55%);
  color: var(--color-ink);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.perf-content {
  position: relative;
  z-index: 2;
  max-width: 1100px;
  margin: 0 auto;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
}

.perf-title {
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  color: var(--color-ink) !important;
  margin-bottom: 60px;
  line-height: 1;
  font-weight: 800;
}

.perf-features {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 60px;
  margin-bottom: 0;
}

.perf-feature {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.perf-icon-wrap {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-ink);
}

.perf-icon {
  width: 26px;
  height: 26px;
}

.perf-feature-title {
  font-family: var(--font-mono);
  font-size: 18px;
  font-weight: 700;
  color: var(--color-ink) !important;
  text-transform: uppercase;
  letter-spacing: 0.02em;
  margin: 0;
}

.perf-feature-desc {
  font-family: var(--font-serif);
  font-style: italic;
  font-size: clamp(1rem, 1.8vw, 1.375rem);
  color: var(--color-ink-secondary) !important;
  line-height: 1.5;
  margin: 0;
}

/* Performance product image */
.perf-product-img {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  z-index: 2;
  margin-top: auto;
  height: 300px;
  overflow: hidden;
}

.perf-product-svg {
  width: auto;
  height: 380px;
  transform: rotate(-10deg) translateY(30px);
  transition: transform 0.8s ease;
  filter: drop-shadow(0 30px 60px rgba(0,0,0,0.2));
}

.perf-product-svg:hover {
  transform: rotate(-6deg) translateY(10px);
}

/* ========== SHOWCASE SECTION ========== */
.showcase-section {
  position: relative;
  min-height: 80vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 100px 40px;
  overflow: hidden;
}

.showcase-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.showcase-bg-svg {
  width: 100%;
  height: 100%;
  max-width: 900px;
}

.showcase-content {
  position: relative;
  z-index: 2;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 50px;
}

.section-label {
  font-size: 11px;
  color: var(--color-text-tertiary);
  letter-spacing: 0.15em;
}

.section-title {
  font-size: clamp(2.5rem, 6vw, 4rem);
  margin: 0;
}

.section-subtitle {
  font-size: clamp(1.1rem, 2vw, 1.5rem);
  color: var(--color-text-secondary);
  margin: 0;
}

.showcase-product {
  position: relative;
  z-index: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.showcase-product-inner {
  animation: showcaseIn 0.6s cubic-bezier(0.22, 1, 0.36, 1) both,
             floatY 6s ease-in-out infinite 0.6s;
}

@keyframes showcaseIn {
  from {
    opacity: 0;
    transform: scale(0.9) translateY(20px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

.showcase-product-svg {
  width: 100%;
  max-width: 280px;
  height: auto;
  transition: filter 0.6s ease;
}

@keyframes floatY {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-15px); }
}

/* ========== CAROUSEL SECTION ========== */
.carousel-section {
  position: relative;
  width: 100%;
  min-height: 104vh;
  padding: 80px 40px 20px;
  overflow: hidden;
}

.carousel-container {
  position: relative;
  max-width: 1250px;
  margin: 0 auto;
}

.carousel-row {
  display: flex;
  justify-content: center;
  gap: 20px;
  align-items: flex-start;
}

.carousel-slide {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
  transform: scale(0.85);
  opacity: 0.6;
}

.carousel-slide.active {
  transform: scale(1);
  opacity: 1;
}

.carousel-slide:hover:not(.active) {
  opacity: 0.8;
  transform: scale(0.9);
}

.slide-img-wrap {
  position: relative;
  width: 100%;
  aspect-ratio: 3/4;
  border-radius: 2vw;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.06);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}

.slide-ambient {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  transition: opacity 0.4s ease;
}

.slide-reflection {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 30%;
  pointer-events: none;
  mask-image: linear-gradient(to top, rgba(0,0,0,0.3) 0%, transparent 100%);
  -webkit-mask-image: linear-gradient(to top, rgba(0,0,0,0.3) 0%, transparent 100%);
}

.carousel-slide.active .slide-img-wrap {
  box-shadow:
    0 30px 60px rgba(0, 0, 0, 0.5),
    inset 0 1px 0 rgba(255, 255, 255, 0.12),
    inset 0 -30px 60px rgba(0, 0, 0, 0.3);
  border-color: rgba(255, 255, 255, 0.12);
}

.slide-svg {
  position: relative;
  z-index: 2;
  width: 65%;
  height: auto;
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
  filter: drop-shadow(0 10px 30px rgba(0,0,0,0.3));
}

.carousel-slide.active .slide-svg {
  width: 75%;
  filter: drop-shadow(0 20px 40px rgba(0,0,0,0.4));
}

/* Caption */
.carousel-caption {
  position: absolute;
  top: min(40vw, 510px);
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  gap: 8px;
  transition: left 0.3s cubic-bezier(1, 0, 0.3, 0.93);
  transition-delay: 25ms;
  pointer-events: none;
  white-space: nowrap;
}

.carousel-title {
  font-size: clamp(1.75rem, 3vw, 2.75rem);
  margin: 0;
}

.carousel-desc {
  font-size: clamp(0.95rem, 1.5vw, 1.25rem);
  color: var(--color-text-secondary);
  margin: 0;
  max-width: 300px;
  white-space: normal;
  line-height: 1.4;
}

/* ========== STATS SECTION ========== */
.stats-section {
  position: relative;
  width: 100%;
  padding: 100px 80px;
  background-color: var(--color-paper);
  background-image:
    radial-gradient(ellipse at 30% 0%, rgba(180, 150, 120, 0.2) 0%, transparent 50%),
    radial-gradient(ellipse at 70% 100%, rgba(150, 120, 90, 0.2) 0%, transparent 50%);
  color: var(--color-ink);
  overflow: hidden;
}

.stats-content {
  position: relative;
  z-index: 2;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 14px;
  align-items: center;
  margin-bottom: 50px;
}

.stats-content .section-label {
  color: var(--color-ink-secondary);
}

.stats-content h2 {
  color: var(--color-ink) !important;
  font-size: clamp(2rem, 5vw, 3.5rem);
}

.stats-desc {
  font-size: clamp(1rem, 1.8vw, 1.25rem);
  color: var(--color-ink-secondary) !important;
  max-width: 600px;
  margin: 0;
}

.stats-desc em {
  color: var(--color-ink);
}

.stats-visual {
  display: flex;
  justify-content: center;
}

.wave-container {
  width: 100%;
  max-width: 550px;
  color: var(--color-ink);
}

.wave-svg {
  width: 100%;
  height: auto;
}

/* ========== UNLOCK SECTION ========== */
.unlock-section {
  position: relative;
  min-height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 80px 40px;
  background: linear-gradient(to bottom, var(--color-bg) 0%, var(--color-bg-dark) 100%);
}

.unlock-content {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 14px;
  align-items: center;
}

.unlock-content h2 {
  font-size: clamp(2.5rem, 6vw, 4rem);
  margin: 0;
}

.unlock-desc {
  font-size: clamp(1rem, 1.8vw, 1.25rem);
  color: var(--color-text-secondary);
  max-width: 550px;
  margin: 0 0 16px;
}

.unlock-platform {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--color-text-tertiary);
}

.platform-icon {
  width: 18px;
  height: 18px;
}

/* ========== BOTTOM CTA ========== */
.bottom-cta {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 80px 40px 100px;
  gap: 16px;
  background: var(--color-bg-dark);
  overflow: hidden;
}

.bottom-cta-glow {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 600px;
  height: 400px;
  pointer-events: none;
}

.bottom-cta-product {
  position: relative;
  z-index: 1;
  display: flex;
  justify-content: center;
  margin-bottom: -10px;
}

.bottom-product-svg {
  height: 180px;
  width: auto;
  opacity: 0.9;
}

.bottom-cta-wordmark {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 800px;
  display: flex;
  justify-content: center;
  margin-bottom: 5px;
}

.cta-bottom-text {
  position: relative;
  z-index: 2;
  font-size: clamp(1.25rem, 2.5vw, 1.75rem);
  color: var(--color-text);
  margin: 0;
}

.hero-cta-row {
  position: relative;
  z-index: 2;
}

.view-all-link {
  position: relative;
  z-index: 2;
  margin-top: 16px;
}

.view-all-link a {
  font-family: var(--font-mono);
  font-size: 13px;
  color: var(--color-text-secondary);
  letter-spacing: 0.02em;
  transition: color var(--transition-fast);
}

.view-all-link a:hover {
  color: var(--color-text);
  opacity: 1;
}

/* ========== RESPONSIVE ========== */
@media (max-width: 1024px) {
  .perf-section,
  .stats-section {
    padding: 80px 40px 0;
  }

  .media-section {
    padding: 80px 40px;
  }

  .perf-features {
    gap: 40px;
  }
}

@media (max-width: 768px) {
  .hero-section {
    min-height: auto;
    padding: 100px 20px 60px;
    gap: 16px;
  }

  .hero-arrow {
    width: 44px;
    height: 44px;
  }

  .hero-arrow.left { left: 12px; }
  .hero-arrow.right { right: 12px; }

  .arrow-svg {
    width: 22px;
    height: 22px;
  }

  .hero-product {
    height: 220px;
  }

  .product-hero-svg {
    height: 200px;
  }

  .hero-cta-row {
    gap: 12px;
    flex-wrap: wrap;
    justify-content: center;
  }

  .cta-label {
    font-size: 10px;
  }

  .perf-section,
  .stats-section {
    padding: 60px 25px 0;
  }

  .perf-features {
    grid-template-columns: 1fr;
    gap: 32px;
    margin-bottom: 40px;
  }

  .perf-title {
    margin-bottom: 40px;
  }

  .media-section {
    padding: 60px 25px;
    gap: 30px;
  }

  .showcase-section {
    padding: 60px 25px;
    min-height: auto;
  }

  .showcase-content {
    margin-bottom: 40px;
  }

  .unlock-section {
    padding: 60px 25px;
    min-height: auto;
  }

  .bottom-cta {
    padding: 60px 25px 80px;
  }
}
</style>
