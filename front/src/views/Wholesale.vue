<template>
  <div class="wholesale-page">
    <!-- Hero -->
    <section class="hero-banner">
      <div class="hero-content fade-in-up">
        <h1 class="font-plaster hero-title">B2B Wholesale</h1>
        <p class="hero-subtitle tracking-wide">
          Partner with LUST8 for premium adult pleasure products.
          Competitive wholesale pricing, OEM/ODM services, and discreet global shipping for retailers & distributors worldwide.
        </p>
      </div>
      <div class="hero-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
      </div>
    </section>

    <!-- Benefits -->
    <section class="benefits-section">
      <h2 class="section-title font-plaster text-center fade-in-up">
        Why Partner With Us
      </h2>

      <div class="benefits-grid">
        <div class="benefit-card fade-in-up" v-for="(benefit, i) in benefits" :key="i">
          <div class="benefit-icon">
            <svg viewBox="0 0 60 60" fill="none">
              <path :d="benefit.icon" :stroke="benefit.color" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none" />
            </svg>
          </div>
          <h3>{{ benefit.title }}</h3>
          <p>{{ benefit.desc }}</p>
        </div>
      </div>
    </section>

    <!-- Wholesale Tiers -->
    <section class="tiers-section">
      <h2 class="section-title font-plaster text-center fade-in-up">
        Wholesale Pricing Tiers
      </h2>
      <p class="section-subtitle text-center fade-in-up">
        Flexible MOQs to suit businesses of all sizes
      </p>

      <div class="tiers-grid">
        <div
          v-for="(tier, i) in pricingTiers"
          :key="i"
          class="tier-card fade-in-up"
          :class="{ featured: tier.featured }"
        >
          <div v-if="tier.featured" class="tier-badge">Most Popular</div>
          <h3 class="tier-name">{{ tier.name }}</h3>
          <div class="tier-price">
            <span class="price-amount">{{ tier.price }}</span>
            <span class="price-unit">/ unit</span>
          </div>
          <p class="tier-moq">MOQ: {{ tier.moq }}</p>
          <ul class="tier-features">
            <li v-for="(f, fi) in tier.features" :key="fi">
              <span class="check">✓</span> {{ f }}
            </li>
          </ul>
          <button class="tier-btn" @click="scrollToForm">
            Get Quote
          </button>
        </div>
      </div>
    </section>

    <!-- Categories We Offer -->
    <section class="categories-section fade-in-up">
      <h2 class="section-title font-plaster text-center">
        Product Categories
      </h2>
      <div class="category-tags">
        <span v-for="cat in categoryTags" :key="cat" class="cat-tag">
          {{ cat }}
        </span>
      </div>
    </section>

    <!-- Contact Form -->
    <section class="form-section" id="contact-form">
      <div class="form-container fade-in-up">
        <h2 class="form-title font-plaster">Request a Quote</h2>
        <p class="form-subtitle">
          Fill out the form below and our wholesale team will get back to you within 24 hours.
        </p>

        <form class="wholesale-form" @submit.prevent="handleSubmit">
          <div class="form-row">
            <div class="form-group">
              <label>Company Name *</label>
              <input type="text" v-model="form.company" required placeholder="Your company name" />
            </div>
            <div class="form-group">
              <label>Contact Person *</label>
              <input type="text" v-model="form.name" required placeholder="Your full name" />
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label>Email *</label>
              <input type="email" v-model="form.email" required placeholder="business@email.com" />
            </div>
            <div class="form-group">
              <label>Phone</label>
              <input type="tel" v-model="form.phone" placeholder="+1 (555) 000-0000" />
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label>Country / Region *</label>
              <input type="text" v-model="form.country" required placeholder="e.g. United States" />
            </div>
            <div class="form-group">
              <label>Business Type</label>
              <select v-model="form.businessType">
                <option value="">Select type</option>
                <option value="retail">Retail Store</option>
                <option value="online">Online Store</option>
                <option value="distributor">Distributor</option>
                <option value="wholesaler">Wholesaler</option>
                <option value="other">Other</option>
              </select>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label>Product Categories Interested In</label>
              <div class="checkbox-group">
                <label v-for="cat in interestCategories" :key="cat.value" class="checkbox-label">
                  <input type="checkbox" :value="cat.value" v-model="form.interests" />
                  <span>{{ cat.label }}</span>
                </label>
              </div>
            </div>
            <div class="form-group">
              <label>Estimated Order Quantity</label>
              <select v-model="form.quantity">
                <option value="">Select range</option>
                <option value="10-50">10 - 50 units</option>
                <option value="50-200">50 - 200 units</option>
                <option value="200-500">200 - 500 units</option>
                <option value="500+">500+ units</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label>White Label / OEM</label>
            <div class="radio-group">
              <label class="radio-label">
                <input type="radio" value="yes" v-model="form.whitelabel" />
                <span>Yes, I need white label</span>
              </label>
              <label class="radio-label">
                <input type="radio" value="no" v-model="form.whitelabel" />
                <span>No, standard packaging is fine</span>
              </label>
            </div>
          </div>

          <div class="form-group">
            <label>Message / Additional Details</label>
            <textarea v-model="form.message" rows="4" placeholder="Tell us more about your business needs..."></textarea>
          </div>

          <button type="submit" class="btn-primary submit-btn" :disabled="isSubmitting">
            <span>{{ isSubmitting ? 'Sending...' : 'Submit Request' }}</span>
            <svg v-if="!isSubmitting" viewBox="0 0 60 59" class="btn-arrow">
              <path d="M20.018,29.5h-8.663V3.5l43.645,26L11.355,55.5H0" fill="none" stroke="currentColor" stroke-miterlimit="10" />
            </svg>
          </button>
        </form>
      </div>
    </section>

    <!-- Trust Bar -->
    <section class="trust-section">
      <div class="trust-grid">
        <div class="trust-item fade-in-up" v-for="(t, i) in trustItems" :key="i">
          <div class="trust-number">{{ t.number }}</div>
          <div class="trust-label">{{ t.label }}</div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'

const isSubmitting = ref(false)

const form = reactive({
  company: '',
  name: '',
  email: '',
  phone: '',
  country: '',
  businessType: '',
  interests: [],
  quantity: '',
  whitelabel: 'no',
  message: ''
})

const benefits = [
  {
    title: 'Premium Quality',
    desc: 'All products are made with medical-grade materials and pass rigorous quality testing.',
    icon: 'M30 5 L30 15 M15 25 L15 55 M45 25 L45 55 M5 35 L25 35 M35 35 L55 35',
    color: '#dd5da2'
  },
  {
    title: 'Competitive Pricing',
    desc: 'Tiered wholesale pricing with volume discounts. The more you order, the more you save.',
    icon: 'M10 45 L25 30 L35 38 L50 15 M10 50 L50 50',
    color: '#e5c000'
  },
  {
    title: 'White Label OEM',
    desc: 'Custom branding, packaging, and product design to make the products truly yours.',
    icon: 'M30 10 L45 25 L30 40 L15 25 Z M15 45 L45 45',
    color: '#f29520'
  },
  {
    title: 'Global Shipping',
    desc: 'Worldwide shipping with discreet packaging. DHL, FedEx, UPS, and sea freight options.',
    icon: 'M10 20 L50 20 L50 40 L10 40 Z M30 20 L30 40 M20 10 L30 20 L40 10 M10 40 L20 50 M40 50 L50 40',
    color: '#8b5cf6'
  },
  {
    title: 'Fast Turnaround',
    desc: 'Stock orders ship within 48 hours. Custom orders in 15-25 days.',
    icon: 'M30 5 A25 25 0 1 1 5 30 L30 30 L30 5',
    color: '#06b6d4'
  },
  {
    title: 'Dedicated Support',
    desc: 'Personal account manager to assist you from inquiry to delivery and beyond.',
    icon: 'M30 20 A10 10 0 1 1 20 30 M10 45 Q10 35 30 35 Q50 35 50 45',
    color: '#10b981'
  }
]

const pricingTiers = [
  {
    name: 'Starter',
    price: '$6.99',
    moq: '10 units',
    features: [
      'Bulk discount pricing',
      'Standard packaging',
      'Discreet shipping',
      'Email support',
      'Mixed SKUs allowed'
    ],
    featured: false
  },
  {
    name: 'Growth',
    price: '$4.99',
    moq: '100 units',
    features: [
      'Up to 40% off retail',
      'Custom logo option',
      'Priority shipping',
      'Dedicated account manager',
      'Flexible payment terms',
      'Free samples available'
    ],
    featured: true
  },
  {
    name: 'Enterprise',
    price: 'Custom',
    moq: '500+ units',
    features: [
      'Best pricing guaranteed',
      'Full white label OEM',
      'Custom product design',
      'Air + sea freight',
      'Private labeling',
      'Exclusive distribution option',
      '24/7 priority support'
    ],
    featured: false
  }
]

const categoryTags = [
  'Wand Massagers',
  'Vibrators',
  'Kegel Balls',
  'Couples Toys',
  'Suction Stimulators',
  'Rabbit Vibrators',
  'Accessories',
  'Lubricants',
  'Bondage',
  'Dildos',
  'Male Toys',
  'Lingerie'
]

const interestCategories = [
  { value: 'wand', label: 'Wand Massagers' },
  { value: 'vibrator', label: 'Vibrators' },
  { value: 'couples', label: 'Couples Toys' },
  { value: 'kegel', label: 'Kegel Balls' },
  { value: 'suction', label: 'Suction Stimulators' },
  { value: 'accessories', label: 'Accessories' },
  { value: 'male', label: 'Male Toys' },
  { value: 'lingerie', label: 'Lingerie' }
]

const trustItems = [
  { number: '500+', label: 'Global Partners' },
  { number: '50+', label: 'Countries Served' },
  { number: '1M+', label: 'Units Sold' },
  { number: '24/7', label: 'Support' }
]

const scrollToForm = () => {
  document.getElementById('contact-form')?.scrollIntoView({ behavior: 'smooth' })
}

const handleSubmit = async () => {
  isSubmitting.value = true
  // Simulate API call
  await new Promise(resolve => setTimeout(resolve, 1500))
  alert('Thank you for your inquiry! Our wholesale team will contact you within 24 hours.')
  isSubmitting.value = false
  // Reset form
  Object.keys(form).forEach(key => {
    if (Array.isArray(form[key])) {
      form[key] = []
    } else if (key === 'whitelabel') {
      form[key] = 'no'
    } else {
      form[key] = ''
    }
  })
}

onMounted(() => {
  setTimeout(() => {
    document.querySelectorAll('.fade-in-up, .fade-in').forEach((el, i) => {
      setTimeout(() => el.classList.add('visible'), i * 80)
    })
  }, 200)
})
</script>

<style scoped>
.wholesale-page {
  padding-top: 70px;
  width: 100%;
}

/* Hero Banner */
.hero-banner {
  position: relative;
  padding: 6rem 1.5rem 5rem;
  text-align: center;
  overflow: hidden;
  background: linear-gradient(135deg, var(--color-bg) 0%, var(--color-flavor-light) 100%);
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 700px;
  margin: 0 auto;
}

.hero-title {
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  margin-bottom: 1rem;
}

.hero-subtitle {
  font-size: 1.125rem;
  color: var(--color-text-light);
  line-height: 1.7;
  max-width: 550px;
  margin: 0 auto;
}

.hero-shapes {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0.3;
  filter: blur(40px);
}

.shape-1 {
  width: 300px;
  height: 300px;
  background: var(--color-flavor);
  top: -100px;
  left: -50px;
}

.shape-2 {
  width: 250px;
  height: 250px;
  background: #e5c000;
  bottom: -80px;
  right: 10%;
}

.shape-3 {
  width: 200px;
  height: 200px;
  background: #f29520;
  top: 50%;
  right: -50px;
  transform: translateY(-50%);
}

/* Benefits */
.benefits-section {
  padding: 5rem 1.5rem;
  max-width: 1200px;
  margin: 0 auto;
}

.section-title {
  font-size: clamp(2rem, 4vw, 3rem);
  margin-bottom: 0.75rem;
}

.section-subtitle {
  font-size: 1.1rem;
  color: var(--color-text-light);
  margin-bottom: 3rem;
}

.benefits-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.benefit-card {
  background: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 2rem;
  transition: all var(--transition-base);
}

.benefit-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
}

.benefit-icon {
  width: 60px;
  height: 60px;
  margin-bottom: 1.25rem;
}

.benefit-icon svg {
  width: 100%;
  height: 100%;
}

.benefit-card h3 {
  font-size: 1.25rem;
  margin-bottom: 0.75rem;
}

.benefit-card p {
  font-size: 0.95rem;
  line-height: 1.6;
}

/* Tiers */
.tiers-section {
  padding: 5rem 1.5rem;
  background: rgba(255, 255, 255, 0.3);
}

.tiers-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  max-width: 1000px;
  margin: 3rem auto 0;
}

.tier-card {
  position: relative;
  background: white;
  border-radius: 20px;
  padding: 2.5rem 2rem;
  text-align: center;
  transition: all var(--transition-base);
  display: flex;
  flex-direction: column;
}

.tier-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
}

.tier-card.featured {
  border: 3px solid var(--color-flavor);
  transform: scale(1.05);
}

.tier-card.featured:hover {
  transform: scale(1.05) translateY(-6px);
}

.tier-badge {
  position: absolute;
  top: -14px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--color-flavor);
  color: white;
  padding: 0.375rem 1.25rem;
  border-radius: 9999px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.tier-name {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.tier-price {
  margin: 1rem 0 0.25rem;
}

.price-amount {
  font-size: 3rem;
  font-weight: 700;
  color: var(--color-flavor);
}

.price-unit {
  font-size: 0.9rem;
  color: var(--color-text-light);
}

.tier-moq {
  font-size: 0.9rem;
  color: var(--color-text-light);
  margin-bottom: 1.5rem;
}

.tier-features {
  list-style: none;
  padding: 0;
  margin-bottom: 2rem;
  text-align: left;
  flex: 1;
}

.tier-features li {
  padding: 0.5rem 0;
  font-size: 0.9rem;
  color: var(--color-text-light);
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
}

.tier-features .check {
  color: var(--color-flavor);
  font-weight: 700;
  flex-shrink: 0;
}

.tier-btn {
  width: 100%;
  padding: 0.875rem 1.5rem;
  border: 2px solid var(--color-text);
  border-radius: 9999px;
  background: transparent;
  font-family: inherit;
  font-size: 1rem;
  font-weight: 500;
  color: var(--color-text);
  cursor: pointer;
  transition: all var(--transition-base);
}

.tier-btn:hover {
  background: var(--color-text);
  color: var(--color-bg);
}

.tier-card.featured .tier-btn {
  background: var(--color-flavor);
  border-color: var(--color-flavor);
  color: white;
}

.tier-card.featured .tier-btn:hover {
  background: var(--color-flavor-dark);
  border-color: var(--color-flavor-dark);
}

/* Categories */
.categories-section {
  padding: 5rem 1.5rem;
  max-width: 1000px;
  margin: 0 auto;
  text-align: center;
}

.category-tags {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.75rem;
  margin-top: 2rem;
}

.cat-tag {
  padding: 0.5rem 1.25rem;
  background: rgba(255, 255, 255, 0.6);
  border: 1px solid rgba(35, 31, 32, 0.1);
  border-radius: 9999px;
  font-size: 0.9rem;
  color: var(--color-text);
  transition: all var(--transition-fast);
}

.cat-tag:hover {
  background: var(--color-flavor);
  color: white;
  border-color: var(--color-flavor);
}

/* Form */
.form-section {
  padding: 5rem 1.5rem;
  background: rgba(255, 255, 255, 0.3);
}

.form-container {
  max-width: 800px;
  margin: 0 auto;
  background: white;
  border-radius: 24px;
  padding: 3rem;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.08);
}

.form-title {
  font-size: clamp(1.75rem, 3.5vw, 2.5rem);
  text-align: center;
  margin-bottom: 0.75rem;
}

.form-subtitle {
  text-align: center;
  color: var(--color-text-light);
  margin-bottom: 2.5rem;
  line-height: 1.6;
}

.wholesale-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--color-text);
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 0.75rem 1rem;
  border: 2px solid rgba(35, 31, 32, 0.15);
  border-radius: 12px;
  font-family: inherit;
  font-size: 0.95rem;
  color: var(--color-text);
  background: #fafafa;
  transition: all var(--transition-fast);
  outline: none;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  border-color: var(--color-flavor);
  background: white;
}

.form-group textarea {
  resize: vertical;
  min-height: 100px;
}

.checkbox-group {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: var(--color-text-light);
  cursor: pointer;
  font-weight: 400;
}

.checkbox-label input {
  width: auto;
  padding: 0;
}

.radio-group {
  display: flex;
  gap: 2rem;
}

.radio-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9rem;
  color: var(--color-text-light);
  cursor: pointer;
  font-weight: 400;
}

.submit-btn {
  justify-content: center;
  padding: 1rem 2rem;
  font-size: 1rem;
  margin-top: 0.5rem;
}

.submit-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-arrow {
  width: 22px;
}

/* Trust Section */
.trust-section {
  padding: 4rem 1.5rem;
}

.trust-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 2rem;
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
}

.trust-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.trust-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--color-flavor);
  font-family: var(--font-plaster);
}

.trust-label {
  font-size: 0.95rem;
  color: var(--color-text-light);
}

@media (max-width: 768px) {
  .wholesale-page {
    padding-top: 60px;
  }

  .hero-banner {
    padding: 4rem 1rem 3.5rem;
  }

  .benefits-section,
  .tiers-section,
  .categories-section,
  .form-section {
    padding: 3rem 1rem;
  }

  .tier-card.featured {
    transform: scale(1);
  }

  .tier-card.featured:hover {
    transform: translateY(-6px);
  }

  .form-container {
    padding: 2rem 1.5rem;
    border-radius: 16px;
  }

  .form-row {
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }

  .checkbox-group {
    grid-template-columns: 1fr;
  }

  .radio-group {
    flex-direction: column;
    gap: 0.75rem;
  }

  .trust-section {
    padding: 3rem 1rem;
  }

  .trust-number {
    font-size: 2rem;
  }
}
</style>
