<script setup>
import { ref, onMounted, provide } from 'vue'
import { useRoute } from 'vue-router'
import HeaderNav from './components/HeaderNav.vue'
import FooterNav from './components/FooterNav.vue'
import IntroLoader from './components/IntroLoader.vue'
import { useScrollAnimation } from './composables/useScrollAnimation'

const route = useRoute()
const isLoaded = ref(false)
const cartCount = ref(0)
const theme = ref('strawberry') // strawberry, pineapple, peach

provide('cartCount', cartCount)
provide('theme', theme)

const addToCart = () => {
  cartCount.value++
}

provide('addToCart', addToCart)

useScrollAnimation()

onMounted(() => {
  // Simulate page load animation
  setTimeout(() => {
    isLoaded.value = true
  }, 800)
})
</script>

<template>
  <div class="app-wrapper" :class="`theme-${theme}`">
    <IntroLoader :loaded="isLoaded" />

    <HeaderNav :cart-count="cartCount" />

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
  transition: background-color 0.6s ease;
}

main {
  flex: 1;
  display: flex;
  flex-direction: column;
}
</style>
