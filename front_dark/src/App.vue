<script setup>
import { ref, onMounted, provide, watch } from 'vue'
import { useRoute } from 'vue-router'
import HeaderNav from './components/HeaderNav.vue'
import FooterNav from './components/FooterNav.vue'
import { useScrollAnimation } from './composables/useScrollAnimation'
import { useCartStore } from './stores/cart'

const route = useRoute()
const lang = ref('en')

const cartStore = useCartStore()

// Provide cart state and actions globally
provide('cartStore', cartStore)
provide('cartCount', cartStore.state.totalItems)
provide('lang', lang)

provide('addToCart', async (product, quantity = 1, color = '') => {
  await cartStore.addProductToCart(product.id, quantity, color, lang.value)
})

useScrollAnimation()

onMounted(() => {
  // Load cart on app start (uses session_id cookie for guests)
  cartStore.fetchCart(lang.value)

  // Page load animation
  document.body.style.opacity = '0'
  setTimeout(() => {
    document.body.style.transition = 'opacity 0.6s ease'
    document.body.style.opacity = '1'
  }, 100)
})

// Refresh cart when language changes
watch(lang, (newLang) => {
  cartStore.fetchCart(newLang)
})
</script>

<template>
  <div class="app-wrapper">
    <HeaderNav :cart-count="cartStore.state.totalItems" :lang="lang" @update:lang="lang = $event" />

    <main>
      <router-view v-slot="{ Component }">
        <transition name="page" mode="out-in">
          <component :is="Component" :key="route.fullPath" />
        </transition>
      </router-view>
    </main>

    <FooterNav />
  </div>
</template>

<style scoped>
.app-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--color-bg);
}

main {
  flex: 1;
  display: flex;
  flex-direction: column;
}
</style>
