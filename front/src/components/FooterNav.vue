<template>
  <footer class="footer">
    <div class="footer-texture"></div>

    <div class="footer-content">
      <a href="#" class="footer-contact">
        <svg viewBox="0 0 50 50" class="contact-icon">
          <path d="M24.999,3L2.5,34.166l22.499,12.834,22.501-12.834L24.999,3ZM23.159,31.709v9.956l-15.236-8.691,15.236-21.104v16.103h3.681V11.87l15.236,21.104-15.236,8.691v-9.956h-3.681Z" />
        </svg>
      </a>

      <div class="footer-main">
        <svg viewBox="0 0 100 120" class="footer-logo">
          <path d="M50 10 C35 10 25 25 25 42 C25 60 35 75 50 95 C65 75 75 60 75 42 C75 25 65 10 50 10 Z M50 50 C44 50 40 46 40 40 C40 34 44 30 50 30 C56 30 60 34 60 40 C60 46 56 50 50 50 Z M30 100 L30 110 M70 100 L70 110 M50 95 L50 110"
                fill="none"
                stroke="currentColor"
                stroke-width="3"
                stroke-linecap="round" />
        </svg>

        <p class="copyright">
          © LUST8. All rights reserved.<span class="year"> 2026</span>
        </p>

        <div class="footer-links">
          <router-link to="/">Home</router-link>
          <router-link to="/products">Products</router-link>
          <router-link to="/wholesale">Wholesale</router-link>
          <a href="#">Privacy</a>
          <a href="#">Terms</a>
        </div>

        <div class="social">
          <a href="#" target="_blank" aria-label="Instagram">
            <svg viewBox="0 0 640 640">
              <path d="M320.3 205C256.8 204.8 205.2 256.2 205 319.7C204.8 383.2 256.2 434.8 319.7 435C383.2 435.2 434.8 383.8 435 320.3C435.2 256.8 383.8 205.2 320.3 205zM319.7 245.4C360.9 245.2 394.4 278.5 394.6 319.7C394.8 360.9 361.5 394.4 320.3 394.6C279.1 394.8 245.6 361.5 245.4 320.3C245.2 279.1 278.5 245.6 319.7 245.4zM413.1 200.3C413.1 185.5 425.1 173.5 439.9 173.5C454.7 173.5 466.7 185.5 466.7 200.3C466.7 215.1 454.7 227.1 439.9 227.1C425.1 227.1 413.1 215.1 413.1 200.3zM542.8 227.5C541.1 191.6 532.9 159.8 506.6 133.6C480.4 107.4 448.6 99.2 412.7 97.4C375.7 95.3 264.8 95.3 227.8 97.4C192 99.1 160.2 107.3 133.9 133.5C107.6 159.7 99.5 191.5 97.7 227.4C95.6 264.4 95.6 375.3 97.7 412.3C99.4 448.2 107.6 480 133.9 506.2C160.2 532.4 191.9 540.6 227.8 542.4C264.8 544.5 375.7 544.5 412.7 542.4C448.6 540.7 480.4 532.5 506.6 506.2C532.8 480 541 448.2 542.8 412.3C544.9 375.3 544.9 264.5 542.8 227.5zM495 452C487.2 471.6 472.1 486.7 452.4 494.6C422.9 506.3 352.9 503.6 320.3 503.6C287.7 503.6 217.6 506.2 188.2 494.6C168.6 486.8 153.5 471.7 145.6 452C133.9 422.5 136.6 352.5 136.6 319.9C136.6 287.3 134 217.2 145.6 187.8C153.4 168.2 168.5 153.1 188.2 145.2C217.7 133.5 287.7 136.2 320.3 136.2C352.9 136.2 423 133.6 452.4 145.2C472 153 487.1 168.1 495 187.8C506.7 217.3 504 287.3 504 319.9C504 352.5 506.7 422.6 495 452z" />
            </svg>
          </a>
          <a href="#" target="_blank" aria-label="Twitter">
            <svg viewBox="0 0 640 640">
              <path d="M196.3 512L103.4 512L103.4 212.9L196.3 212.9L196.3 512zM149.8 172.1C120.1 172.1 96 147.5 96 117.8C96 103.5 101.7 89.9 111.8 79.8C121.9 69.7 135.6 64 149.8 64C164 64 177.7 69.7 187.8 79.8C197.9 89.9 203.6 103.6 203.6 117.8C203.6 147.5 179.5 172.1 149.8 172.1zM543.9 512L451.2 512L451.2 366.4C451.2 331.7 450.5 287.2 402.9 287.2C354.6 287.2 347.2 324.9 347.2 363.9L347.2 512L254.4 512L254.4 212.9L343.5 212.9L343.5 253.7L344.8 253.7C357.2 230.2 387.5 205.4 432.7 205.4C526.7 205.4 544 267.3 544 347.7L544 512L543.9 512z" />
            </svg>
          </a>
          <a href="#" target="_blank" aria-label="TikTok">
            <svg viewBox="0 0 640 640">
              <path d="M340 120 C380 125 420 145 440 180 L440 260 C440 360 360 420 280 400 C230 388 200 340 200 290 C200 240 240 200 290 200 C310 200 330 210 340 225 L340 120 Z M280 260 C260 260 250 280 250 295 C250 315 265 330 285 330 C310 330 325 310 325 285 L325 240 C325 240 310 260 280 260 Z" />
            </svg>
          </a>
          <a href="#" target="_blank" aria-label="YouTube">
            <svg viewBox="0 0 640 640">
              <path d="M581.7 188.1C575.5 164.4 556.9 145.8 533.4 139.5C490.9 128 320.1 128 320.1 128C320.1 128 149.3 128 106.7 139.5C83.2 145.8 64.7 164.4 58.4 188.1C47 231 47 320.4 47 320.4C47 320.4 47 409.8 58.4 452.7C64.7 476.3 83.2 494.2 106.7 500.5C149.3 512 320.1 512 320.1 512C320.1 512 490.9 512 533.5 500.5C557 494.2 575.5 476.3 581.8 452.7C593.2 409.8 593.2 320.4 593.2 320.4C593.2 320.4 593.2 231 581.7 188.1zM264.2 401.6L264.2 239.2L406.9 320.4L264.2 401.6z" />
            </svg>
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.footer {
  position: relative;
  padding: 4rem 1.5rem 2rem;
  text-align: center;
  overflow: hidden;
}

.footer-texture {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background:
    radial-gradient(ellipse at top, var(--color-flavor-light) 0%, transparent 60%);
  opacity: 0.5;
  pointer-events: none;
}

.footer-content {
  position: relative;
  z-index: 1;
  max-width: 600px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
}

.footer-contact {
  margin-bottom: 1rem;
  transition: transform var(--transition-base);
}

.footer-contact:hover {
  transform: translateY(-4px);
}

.contact-icon {
  width: 32px;
  height: 32px;
  fill: var(--color-text);
}

.footer-main {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  width: 100%;
}

.footer-logo {
  width: 60px;
  height: 72px;
  color: var(--color-text);
}

.copyright {
  font-size: 0.875rem;
  color: var(--color-text-light);
  margin: 0;
}

.year {
  color: var(--color-text-light);
}

.footer-links {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
  font-size: 0.875rem;
  color: var(--color-text-light);
}

.footer-links a {
  color: var(--color-text-light);
  transition: color var(--transition-fast);
}

.footer-links a:hover {
  color: var(--color-flavor);
}

.social {
  display: flex;
  gap: 1.25rem;
  margin-top: 0.5rem;
}

.social a {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-light);
  transition: all var(--transition-base);
  border-radius: 50%;
}

.social a:hover {
  color: var(--color-flavor);
  transform: translateY(-2px);
}

.social svg {
  width: 24px;
  height: 24px;
  fill: currentColor;
}

@media (max-width: 768px) {
  .footer {
    padding: 3rem 1rem 1.5rem;
  }

  .footer-links {
    gap: 1rem;
    font-size: 0.8rem;
  }

  .social {
    gap: 1rem;
  }
}
</style>
