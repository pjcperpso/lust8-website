<template>
  <footer class="footer noise-overlay">
    <div class="footer-content">
      <!-- Left: Links -->
      <div class="footer-links">
        <div class="link-group">
          <a href="#" class="footer-link">Instagram</a>
          <a href="#" class="footer-link">X</a>
          <a href="#" class="footer-link">TikTok</a>
        </div>
        <div class="link-group">
          <a href="#" class="footer-link">About</a>
          <a href="#" class="footer-link">Journal</a>
          <a href="#" class="footer-link">Careers</a>
        </div>
        <div class="link-group">
          <a href="#" class="footer-link">Support</a>
          <a href="#" class="footer-link">Privacy</a>
        </div>
      </div>

      <!-- Right: Brand -->
      <div class="footer-brand">
        <div class="suit-icons">
          <svg viewBox="0 0 24 24" class="suit-icon">
            <path d="M12 2C12 2 6 9 6 14C6 17.3 8.7 20 12 20C15.3 20 18 17.3 18 14C18 9 12 2 12 2Z" fill="currentColor" />
          </svg>
          <svg viewBox="0 0 24 24" class="suit-icon diamond">
            <path d="M12 2L2 12L12 22L22 12L12 2Z" fill="currentColor" />
          </svg>
          <svg viewBox="0 0 24 24" class="suit-icon heart">
            <path d="M12 21C12 21 3 14 3 8.5C3 5.5 5.5 3 8.5 3C10.5 3 12 4.5 12 4.5C12 4.5 13.5 3 15.5 3C18.5 3 21 5.5 21 8.5C21 14 12 21 12 21Z" fill="currentColor" />
          </svg>
        </div>
        <p class="brand-text">
          A <span class="brand-underline">lust8.com</span> company
        </p>
        <p class="brand-location">
          Made in Shanghai, CN
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.footer {
  position: relative;
  width: 100%;
  padding: 80px 80px 60px;
  background-color: var(--color-bg-dark);
  overflow: hidden;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  max-width: 1400px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

/* Left links */
.footer-links {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.link-group {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.footer-link {
  font-family: var(--font-mono);
  font-size: 13px;
  font-weight: 500;
  color: var(--color-text-secondary);
  letter-spacing: 0.02em;
  transition: color var(--transition-fast);
}

.footer-link:hover {
  color: var(--color-text);
}

/* Right brand */
.footer-brand {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 12px;
  text-align: right;
}

.suit-icons {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 8px;
}

.suit-icon {
  width: 28px;
  height: 28px;
  color: var(--color-text);
  filter: drop-shadow(0 0 12px rgba(255, 255, 255, 0.2));
  transition: all var(--transition-base);
}

.suit-icon:hover {
  filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.4));
  transform: translateY(-2px);
}

.suit-icon.diamond {
  width: 24px;
  height: 24px;
}

.suit-icon.heart {
  width: 28px;
  height: 28px;
}

.brand-text {
  font-family: var(--font-serif);
  font-style: italic;
  font-size: 15px;
  color: var(--color-text-secondary);
  margin: 0;
  line-height: 1.4;
}

.brand-underline {
  text-decoration: underline;
  text-underline-offset: 2px;
  color: var(--color-text);
  font-family: var(--font-mono);
  font-style: normal;
  font-size: 13px;
}

.brand-location {
  font-family: var(--font-serif);
  font-style: italic;
  font-size: 14px;
  color: var(--color-text-tertiary);
  margin: 0;
}

@media (max-width: 768px) {
  .footer {
    padding: 60px 25px 40px;
  }

  .footer-content {
    flex-direction: column-reverse;
    gap: 40px;
  }

  .footer-brand {
    align-items: flex-start;
    text-align: left;
  }

  .suit-icons {
    gap: 12px;
  }

  .suit-icon {
    width: 24px;
    height: 24px;
  }

  .footer-links {
    gap: 16px;
  }

  .footer-link {
    font-size: 12px;
  }
}
</style>
