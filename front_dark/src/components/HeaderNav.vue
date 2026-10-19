<template>
  <header class="header">
    <!-- Left: Logo -->
    <router-link to="/" class="header-logo">
      <svg viewBox="0 0 80 24" class="logo-icon">
        <ellipse cx="12" cy="12" rx="10" ry="8" fill="none" stroke="currentColor" stroke-width="1.5" />
        <rect x="6" y="10" width="12" height="4" rx="1" fill="currentColor" opacity="0.6" />
      </svg>
      <span class="logo-text">LUST8</span>
    </router-link>

    <!-- Center: Select label -->
    <div class="header-center font-mono">
      {{ lang === 'en' ? 'Select your vibe' : '选择你的玩具' }}
    </div>

    <!-- Right: Lang toggle + Join button -->
    <div class="header-right">
      <div class="lang-toggle">
        <button
          class="lang-btn"
          :class="{ active: lang === 'en' }"
          @click="$emit('update:lang', 'en')"
        >EN</button>
        <span class="lang-divider"></span>
        <button
          class="lang-btn"
          :class="{ active: lang === 'zh' }"
          @click="$emit('update:lang', 'zh')"
        >中文</button>
      </div>
      <button class="join-btn">
        <span>{{ lang === 'en' ? 'Join' : '加入' }}</span>
        <span class="join-dot"></span>
      </button>
    </div>

    <!-- Mobile Menu Overlay -->
    <div v-if="menuOpen" class="menu-overlay" @click.self="toggleMenu">
      <div class="menu-panel">
        <div class="menu-header">
          <span class="menu-title font-mono">MENU</span>
          <button class="close-btn" @click="toggleMenu">
            <svg viewBox="0 0 24 24" class="close-icon">
              <path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg>
          </button>
        </div>
        <nav class="mobile-nav">
          <router-link to="/" @click="toggleMenu"><span class="nav-num">01</span> Home</router-link>
          <router-link to="/products" @click="toggleMenu"><span class="nav-num">02</span> All Products</router-link>
          <router-link to="/products?category=wand" @click="toggleMenu"><span class="nav-num">03</span> Wand Massagers</router-link>
          <router-link to="/products?category=suction" @click="toggleMenu"><span class="nav-num">04</span> Suction Toys</router-link>
          <router-link to="/products?category=couples" @click="toggleMenu"><span class="nav-num">05</span> Couples</router-link>
          <router-link to="/wholesale" @click="toggleMenu"><span class="nav-num">06</span> B2B Wholesale</router-link>
        </nav>
        <div class="menu-footer">
          <a href="#" class="menu-link">Instagram</a>
          <a href="#" class="menu-link">X</a>
          <a href="#" class="menu-link">TikTok</a>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  cartCount: {
    type: Number,
    default: 0
  },
  lang: {
    type: String,
    default: 'en'
  }
})

defineEmits(['update:lang'])

const menuOpen = ref(false)

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
  document.body.style.overflow = menuOpen.value ? 'hidden' : ''
}
</script>

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 68px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  z-index: 50;
  background: transparent;
  pointer-events: none;
}

.header > * {
  pointer-events: auto;
}

/* Logo */
.header-logo {
  display: flex;
  align-items: center;
  gap: 10px;
  color: var(--color-text);
  transition: opacity var(--transition-fast);
}

.header-logo:hover {
  opacity: 0.7;
}

.logo-icon {
  width: 36px;
  height: auto;
}

.logo-text {
  font-family: var(--font-sans);
  font-weight: 700;
  font-size: 16px;
  letter-spacing: -0.01em;
}

/* Center label */
.header-center {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  font-size: 13px;
  color: var(--color-text-tertiary);
  letter-spacing: 0.08em;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

/* Language toggle */
.lang-toggle {
  display: flex;
  align-items: center;
  gap: 0;
  padding: 4px;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.lang-btn {
  padding: 4px 10px;
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--color-text-tertiary);
  border-radius: var(--radius-full);
  transition: all var(--transition-fast);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.lang-btn:hover {
  color: var(--color-text-secondary);
}

.lang-btn.active {
  background: rgba(255, 255, 255, 0.12);
  color: var(--color-text);
}

.lang-divider {
  width: 1px;
  height: 12px;
  background: rgba(255, 255, 255, 0.1);
}

/* Join button */
.join-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(10px);
  color: var(--color-text);
  font-family: var(--font-sans);
  font-size: 13px;
  font-weight: 500;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all var(--transition-base);
}

.join-btn:hover {
  background: rgba(255, 255, 255, 0.14);
  transform: translateY(-1px);
}

.join-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--color-text);
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
}

/* Mobile Menu */
.menu-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(8px);
  z-index: 100;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.menu-panel {
  width: 340px;
  max-width: 85vw;
  height: 100%;
  background: var(--color-bg-dark);
  animation: slideIn 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  flex-direction: column;
  padding: 32px 0;
}

@keyframes slideIn {
  from { transform: translateX(-100%); }
  to { transform: translateX(0); }
}

.menu-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px 24px;
  border-bottom: 1px solid var(--color-border);
}

.menu-title {
  font-size: 11px;
  color: var(--color-text-tertiary);
  letter-spacing: 0.1em;
}

.close-btn {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-secondary);
  transition: color var(--transition-fast);
}

.close-btn:hover {
  color: var(--color-text);
}

.close-icon {
  width: 20px;
  height: 20px;
}

.mobile-nav {
  flex: 1;
  padding: 24px 0;
  display: flex;
  flex-direction: column;
}

.mobile-nav a {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 14px 32px;
  font-family: var(--font-sans);
  font-size: 16px;
  font-weight: 500;
  color: var(--color-text);
  transition: all var(--transition-fast);
  border-left: 2px solid transparent;
}

.mobile-nav a:hover {
  background: rgba(255, 255, 255, 0.05);
  border-left-color: var(--color-text);
}

.nav-num {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--color-text-tertiary);
  font-weight: 400;
  letter-spacing: 0.05em;
  min-width: 28px;
}

.menu-footer {
  display: flex;
  gap: 24px;
  padding: 24px 32px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.menu-link {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--color-text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  transition: color var(--transition-fast);
}

.menu-link:hover {
  color: var(--color-text);
}

@media (max-width: 768px) {
  .header {
    padding: 0 20px;
    height: 60px;
  }

  .header-center {
    display: none;
  }

  .logo-text {
    font-size: 14px;
  }

  .join-btn {
    padding: 6px 14px;
    font-size: 12px;
  }

  .menu-panel {
    width: 300px;
  }
}
</style>
