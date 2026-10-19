<template>
  <div class="intro-loader" :class="{ active: !loaded, loaded }">
    <div class="loader-bg">
      <div class="loader-bg__inner"></div>
      <div class="loader-bg__inner"></div>
      <div class="loader-bg__inner"></div>
      <div class="loader-bg__inner"></div>
      <div class="loader-bg__inner"></div>
    </div>
    <svg v-if="!loaded" viewBox="0 0 240 240" fill="none" class="gooey-loader">
      <defs>
        <filter id="goo">
          <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="blur" />
          <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 60 -32" />
        </filter>
      </defs>
      <g filter="url(#goo)">
        <circle cx="119" cy="74" r="20" stroke="#ffffff" stroke-width="8" fill="none" />
        <circle cx="79" cy="141" r="20" stroke="#ffffff" stroke-width="8" fill="none" />
        <circle cx="157" cy="141" r="20" stroke="#ffffff" stroke-width="8" fill="none" />
        <circle r="14" fill="#ffffff">
          <animateMotion path="M102.546 83.5C109.859 70.8333 128.141 70.8333 135.454 83.5L157.971 122.5C165.284 135.167 156.143 151 141.517 151H96.4833C81.8571 151 72.7158 135.167 80.0289 122.5L102.546 83.5Z" dur="2s" repeatCount="indefinite" />
        </circle>
      </g>
    </svg>
  </div>
</template>

<script setup>
defineProps({
  loaded: {
    type: Boolean,
    default: false
  }
})
</script>

<style scoped>
.intro-loader {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 0;
  overflow: hidden;
  z-index: 100;
  pointer-events: none;
  transition: height 0s ease 1.2s;
}

.intro-loader.active {
  height: 100%;
  pointer-events: all;
  transition: height 0s ease 0s;
}

.loader-bg {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
}

.loader-bg__inner {
  flex: 1;
  background-color: var(--color-flavor);
  transform: scaleY(1);
  transform-origin: 50% 100%;
  transition: transform 0.7s cubic-bezier(0.77, 0, 0.175, 1);
}

.intro-loader.loaded .loader-bg__inner {
  transform: scaleY(0);
}

/* Stagger down */
.intro-loader.loaded .loader-bg__inner:nth-child(1) { transition-delay: 0.35s; }
.intro-loader.loaded .loader-bg__inner:nth-child(2) { transition-delay: 0.3s; }
.intro-loader.loaded .loader-bg__inner:nth-child(3) { transition-delay: 0.25s; }
.intro-loader.loaded .loader-bg__inner:nth-child(4) { transition-delay: 0.3s; }
.intro-loader.loaded .loader-bg__inner:nth-child(5) { transition-delay: 0.35s; }

/* Stagger up */
.intro-loader:not(.loaded).active .loader-bg__inner:nth-child(1) { transition-delay: 0s; }
.intro-loader:not(.loaded).active .loader-bg__inner:nth-child(2) { transition-delay: 0.05s; }
.intro-loader:not(.loaded).active .loader-bg__inner:nth-child(3) { transition-delay: 0.1s; }
.intro-loader:not(.loaded).active .loader-bg__inner:nth-child(4) { transition-delay: 0.05s; }
.intro-loader:not(.loaded).active .loader-bg__inner:nth-child(5) { transition-delay: 0s; }

.gooey-loader {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 120px;
  height: 120px;
  z-index: 101;
}
</style>
