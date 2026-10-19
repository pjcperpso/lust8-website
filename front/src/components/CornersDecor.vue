<template>
  <div class="corners">
    <hr class="corners__left" />
    <svg class="corners__top-left" viewBox="0 0 39 39">
      <rect x=".5" y=".5" width="12.667" height="12.667" fill="none" :stroke="strokeColor" stroke-miterlimit="10" />
      <rect x="13.167" y="13.167" width="12.667" height="12.667" fill="none" :stroke="strokeColor" stroke-miterlimit="10" />
      <rect x="13.167" y="25.833" width="12.667" height="12.667" fill="none" :stroke="strokeColor" stroke-miterlimit="10" />
      <rect x="25.833" y="13.167" width="12.667" height="12.667" fill="none" :stroke="strokeColor" stroke-miterlimit="10" />
      <polyline points="38.5 .5 25.833 .5 25.833 13.167" fill="none" :stroke="strokeColor" stroke-linecap="square" stroke-miterlimit="10" />
      <polyline points=".5 38.5 .5 25.833 13.167 25.833" fill="none" :stroke="strokeColor" stroke-linecap="square" stroke-miterlimit="10" />
    </svg>
    <hr class="corners__top" />
    <svg class="corners__top-right" viewBox="0 0 39 39">
      <rect x=".5" y=".5" width="12.667" height="12.667" fill="none" :stroke="strokeColor" stroke-miterlimit="10" />
      <rect x="13.167" y="13.167" width="12.667" height="12.667" fill="none" :stroke="strokeColor" stroke-miterlimit="10" />
      <rect x="13.167" y="25.833" width="12.667" height="12.667" fill="none" :stroke="strokeColor" stroke-miterlimit="10" />
      <rect x="25.833" y="13.167" width="12.667" height="12.667" fill="none" :stroke="strokeColor" stroke-miterlimit="10" />
      <polyline points="38.5 .5 25.833 .5 25.833 13.167" fill="none" :stroke="strokeColor" stroke-linecap="square" stroke-miterlimit="10" />
      <polyline points=".5 38.5 .5 25.833 13.167 25.833" fill="none" :stroke="strokeColor" stroke-linecap="square" stroke-miterlimit="10" />
    </svg>
    <hr class="corners__right" />
  </div>
</template>

<script setup>
defineProps({
  strokeColor: {
    type: String,
    default: '#231f20'
  }
})
</script>

<style scoped>
.corners {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 10;
}

.corners__top-left,
.corners__top-right {
  position: absolute;
  top: 20px;
  width: 39px;
  height: 39px;
}

.corners__top-left {
  left: 20px;
}

.corners__top-right {
  right: 20px;
}

.corners__left,
.corners__right {
  position: absolute;
  top: 59px;
  width: 1px;
  height: calc(50% - 59px);
  border: none;
  background: var(--color-text);
  opacity: 0.2;
}

.corners__left {
  left: 39.5px;
}

.corners__right {
  right: 39.5px;
}

.corners__top {
  position: absolute;
  top: 39.5px;
  left: 59px;
  width: calc(50% - 59px);
  height: 1px;
  border: none;
  background: var(--color-text);
  opacity: 0.2;
}

@media (max-width: 768px) {
  .corners__top-left,
  .corners__top-right {
    top: 12px;
    width: 28px;
    height: 28px;
  }

  .corners__top-left {
    left: 12px;
  }

  .corners__top-right {
    right: 12px;
  }

  .corners__left,
  .corners__right {
    top: 40px;
  }

  .corners__left {
    left: 26px;
  }

  .corners__right {
    right: 26px;
  }

  .corners__top {
    top: 26px;
    left: 40px;
  }
}
</style>
