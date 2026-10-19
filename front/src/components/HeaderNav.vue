<template>
  <header class="header">
    <nav class="header-menu-desktop" role="navigation">
      <button class="header-menu-item reset" @click="toggleMenu">
        <svg viewBox="0 0 50 50" class="menu-icon">
          <path d="M24.999,3L2.5,34.166l22.499,12.834,22.501-12.834L24.999,3ZM23.159,31.709v9.956l-15.236-8.691,15.236-21.104v16.103h3.681V11.87l15.236,21.104-15.236,8.691v-9.956h-3.681Z" />
        </svg>
      </button>
    </nav>

    <router-link to="/" class="header-logo" aria-label="Home">
      <svg viewBox="0 0 100 120" class="logo-svg">
        <!-- Stylized pleasure symbol -->
        <path d="M50 10 C35 10 25 25 25 42 C25 60 35 75 50 95 C65 75 75 60 75 42 C75 25 65 10 50 10 Z M50 50 C44 50 40 46 40 40 C40 34 44 30 50 30 C56 30 60 34 60 40 C60 46 56 50 50 50 Z M30 100 L30 110 M70 100 L70 110 M50 95 L50 110"
              fill="none"
              stroke="currentColor"
              stroke-width="3"
              stroke-linecap="round" />
      </svg>
    </router-link>

    <nav class="header-ctas" role="navigation">
      <button class="header-menu-mobile-toggle reset md:hidden" @click="toggleMenu">
        <span>☰</span>
      </button>
      <router-link to="/wholesale" class="cta-link" title="Wholesale">
        <svg viewBox="0 0 50 50" class="cta-icon">
          <!-- Building icon for B2B -->
          <path d="M10 45 L10 15 L25 5 L40 15 L40 45 M18 20 L18 25 M25 15 L25 45 M32 20 L32 25 M18 32 L18 37 M32 32 L32 37"
                fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </router-link>
      <router-link to="/cart" class="cta-link cart-link" title="Cart">
        <span class="cart-count">{{ cartCount }}</span>
        <svg viewBox="0 0 50 50" class="cta-icon">
          <path d="M17.837,42.495c0,1.577-1.256,2.855-2.805,2.855s-2.805-1.278-2.805-2.855,1.256-2.855,2.805-2.855,2.805,1.278,2.805,2.855ZM41.718,39.641c-1.549,0-2.805,1.278-2.805,2.855s1.256,2.855,2.805,2.855,2.805-1.278,2.805-2.855-1.256-2.855-2.805-2.855ZM16.564,30.108h27.621l5.815-20.049h-4.473l-4.549,15.683h-24.94L10.333,5.35H0v4.366h7.094l5.18,18.514v9.694h32.247v-4.366h-27.958v-3.451Z" />
        </svg>
      </router-link>
    </nav>

    <!-- Mobile Menu Overlay -->
    <div v-if="menuOpen" class="menu-overlay" @click.self="toggleMenu">
      <aside class="menu-panel">
        <header class="panel-header">
          <span class="panel-title font-plaster">Menu</span>
          <button class="close reset" @click="toggleMenu">×</button>
        </header>
        <nav class="mobile-nav">
          <router-link to="/" @click="toggleMenu">Home</router-link>
          <router-link to="/products" @click="toggleMenu">All Products</router-link>
          <router-link to="/products?category=wand" @click="toggleMenu">Wand Massagers</router-link>
          <router-link to="/products?category=couples" @click="toggleMenu">Couples Toys</router-link>
          <router-link to="/wholesale" @click="toggleMenu">B2B Wholesale</router-link>
        </nav>
      </aside>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  cartCount: {
    type: Number,
    default: 0
  }
})

const menuOpen = ref(false)

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
  if (menuOpen.value) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = ''
  }
}
</script>

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 2rem;
  z-index: 50;
  background: transparent;
}

.header-menu-desktop {
  display: flex;
  align-items: center;
}

.header-menu-item {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform var(--transition-fast);
}

.header-menu-item:hover {
  transform: scale(1.1);
}

.menu-icon {
  width: 28px;
  height: 28px;
  fill: var(--color-text);
}

.header-logo {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  color: var(--color-text);
  transition: transform var(--transition-fast);
}

.header-logo:hover {
  transform: translate(-50%, -50%) scale(1.05);
}

.logo-svg {
  width: 40px;
  height: 48px;
  color: var(--color-text);
}

.header-ctas {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.cta-link {
  position: relative;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text);
  transition: transform var(--transition-fast);
}

.cta-link:hover {
  transform: scale(1.1);
  color: var(--color-flavor);
}

.cta-icon {
  width: 26px;
  height: 26px;
  fill: currentColor;
}

.cart-count {
  position: absolute;
  top: -2px;
  right: -2px;
  background: var(--color-flavor);
  color: var(--color-text);
  font-size: 11px;
  font-weight: 600;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
}

.header-menu-mobile-toggle {
  display: none;
  font-size: 1.5rem;
  color: var(--color-text);
}

/* Mobile Menu */
.menu-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
  z-index: 100;
  display: flex;
  justify-content: flex-end;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.menu-panel {
  width: 320px;
  max-width: 85vw;
  height: 100%;
  background: var(--color-bg);
  animation: slideIn 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  flex-direction: column;
}

@keyframes slideIn {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}

.panel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 1.5rem;
  border-bottom: 1px solid rgba(35, 31, 32, 0.1);
}

.panel-title {
  font-size: 1.75rem;
  color: var(--color-text);
}

.close {
  font-size: 2rem;
  color: var(--color-text);
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.mobile-nav {
  flex: 1;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.mobile-nav a {
  font-size: 1.25rem;
  font-weight: 500;
  color: var(--color-text);
  padding: 0.5rem 0;
  border-bottom: 1px solid rgba(35, 31, 32, 0.1);
  transition: color var(--transition-fast);
}

.mobile-nav a:hover {
  color: var(--color-flavor);
}

@media (max-width: 768px) {
  .header {
    padding: 0 1rem;
    height: 60px;
  }

  .header-menu-desktop {
    display: none;
  }

  .header-menu-mobile-toggle {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .logo-svg {
    width: 34px;
    height: 40px;
  }

  .header-ctas {
    gap: 0.75rem;
  }

  .cta-icon {
    width: 22px;
    height: 22px;
  }
}

/* Reset button default styles */
.reset {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  font: inherit;
  color: inherit;
}
</style>
