<template>
  <div class="wholesale-page">
    <!-- Hero -->
    <section class="hero-banner">
      <div class="hero-content fade-in-up">
        <h1 class="font-plaster hero-title">{{ t.heroTitle }}</h1>
        <p class="hero-subtitle tracking-wide">
          {{ t.heroSubtitle }}
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
        {{ t.benefitsTitle }}
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
        {{ t.tiersTitle }}
      </h2>
      <p class="section-subtitle text-center fade-in-up">
        {{ t.tiersSubtitle }}
      </p>

      <div class="tiers-grid">
        <div
          v-for="(tier, i) in pricingTiers"
          :key="i"
          class="tier-card fade-in-up"
          :class="{ featured: tier.featured }"
        >
          <div v-if="tier.featured" class="tier-badge">{{ t.mostPopular }}</div>
          <h3 class="tier-name">{{ tier.name }}</h3>
          <div class="tier-price">
            <span class="price-amount">{{ tier.price }}</span>
            <span class="price-unit">{{ t.perUnit }}</span>
          </div>
          <p class="tier-moq">MOQ: {{ tier.moq }}</p>
          <ul class="tier-features">
            <li v-for="(f, fi) in tier.features" :key="fi">
              <span class="check">✓</span> {{ f }}
            </li>
          </ul>
          <button class="tier-btn" @click="scrollToForm">
            {{ t.getQuote }}
          </button>
        </div>
      </div>
    </section>

    <!-- Categories We Offer -->
    <section class="categories-section fade-in-up">
      <h2 class="section-title font-plaster text-center">
        {{ t.categoriesTitle }}
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
        <h2 class="form-title font-plaster">{{ t.formTitle }}</h2>
        <p class="form-subtitle">
          {{ t.formSubtitle }}
        </p>

        <!-- Success message -->
        <div v-if="submitSuccess" class="success-message">
          <div class="success-icon">✓</div>
          <h3>{{ t.successTitle }}</h3>
          <p>{{ t.successMessage }}</p>
          <button class="btn-primary" @click="resetForm">
            {{ t.submitAnother }}
          </button>
        </div>

        <form v-else class="wholesale-form" @submit.prevent="handleSubmit">
          <div class="form-row">
            <div class="form-group">
              <label>{{ t.companyName }} *</label>
              <input type="text" v-model="form.company" required :placeholder="t.companyNamePh" />
            </div>
            <div class="form-group">
              <label>{{ t.contactPerson }} *</label>
              <input type="text" v-model="form.name" required :placeholder="t.contactPersonPh" />
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label>{{ t.email }} *</label>
              <input type="email" v-model="form.email" required placeholder="business@email.com" />
            </div>
            <div class="form-group">
              <label>{{ t.phone }}</label>
              <input type="tel" v-model="form.phone" :placeholder="t.phonePh" />
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label>{{ t.country }} *</label>
              <input type="text" v-model="form.country" required :placeholder="t.countryPh" />
            </div>
            <div class="form-group">
              <label>{{ t.businessType }}</label>
              <select v-model="form.businessType">
                <option value="">{{ t.selectType }}</option>
                <option value="retail">{{ t.typeRetail }}</option>
                <option value="online">{{ t.typeOnline }}</option>
                <option value="distributor">{{ t.typeDistributor }}</option>
                <option value="wholesaler">{{ t.typeWholesaler }}</option>
                <option value="other">{{ t.typeOther }}</option>
              </select>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label>{{ t.interestedIn }}</label>
              <div class="checkbox-group">
                <label v-for="cat in interestCategories" :key="cat.value" class="checkbox-label">
                  <input type="checkbox" :value="cat.value" v-model="form.interests" />
                  <span>{{ cat.label }}</span>
                </label>
              </div>
            </div>
            <div class="form-group">
              <label>{{ t.estimatedQty }}</label>
              <select v-model="form.quantity">
                <option value="">{{ t.selectRange }}</option>
                <option value="10-50">10 - 50 {{ t.units }}</option>
                <option value="50-200">50 - 200 {{ t.units }}</option>
                <option value="200-500">200 - 500 {{ t.units }}</option>
                <option value="500+">500+ {{ t.units }}</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label>{{ t.whiteLabel }}</label>
            <div class="radio-group">
              <label class="radio-label">
                <input type="radio" value="yes" v-model="form.whitelabel" />
                <span>{{ t.wlYes }}</span>
              </label>
              <label class="radio-label">
                <input type="radio" value="no" v-model="form.whitelabel" />
                <span>{{ t.wlNo }}</span>
              </label>
            </div>
          </div>

          <div class="form-group">
            <label>{{ t.message }}</label>
            <textarea v-model="form.message" rows="4" :placeholder="t.messagePh"></textarea>
          </div>

          <button type="submit" class="btn-primary submit-btn" :disabled="isSubmitting">
            <span>{{ isSubmitting ? t.sending : t.submit }}</span>
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
import { ref, reactive, computed, onMounted, inject } from 'vue'
import { submitInquiry } from '../api/wholesale'
import { useScrollAnimation } from '../composables/useScrollAnimation'

const lang = inject('lang', ref('en'))
const { refreshObserver } = useScrollAnimation()

const isSubmitting = ref(false)
const submitSuccess = ref(false)

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

const t = computed(() => ({
  heroTitle: lang.value === 'en' ? 'B2B Wholesale' : 'B2B 批发',
  heroSubtitle: lang.value === 'en'
    ? 'Partner with LUST8 for premium adult pleasure products. Competitive wholesale pricing, OEM/ODM services, and discreet global shipping for retailers & distributors worldwide.'
    : '与 LUST8 合作，获取高端成人情趣产品。有竞争力的批发价格，OEM/ODM 服务，为全球零售商和经销商提供隐私全球配送。',
  benefitsTitle: lang.value === 'en' ? 'Why Partner With Us' : '为什么选择我们',
  tiersTitle: lang.value === 'en' ? 'Wholesale Pricing Tiers' : '批发价格等级',
  tiersSubtitle: lang.value === 'en' ? 'Flexible MOQs to suit businesses of all sizes' : '灵活的起订量，适合各种规模的企业',
  mostPopular: lang.value === 'en' ? 'Most Popular' : '最受欢迎',
  perUnit: lang.value === 'en' ? '/ unit' : '/ 件',
  getQuote: lang.value === 'en' ? 'Get Quote' : '获取报价',
  categoriesTitle: lang.value === 'en' ? 'Product Categories' : '产品分类',
  formTitle: lang.value === 'en' ? 'Request a Quote' : '申请报价',
  formSubtitle: lang.value === 'en'
    ? 'Fill out the form below and our wholesale team will get back to you within 24 hours.'
    : '填写下面的表单，我们的批发团队将在24小时内与您联系。',
  companyName: lang.value === 'en' ? 'Company Name' : '公司名称',
  companyNamePh: lang.value === 'en' ? 'Your company name' : '您的公司名称',
  contactPerson: lang.value === 'en' ? 'Contact Person' : '联系人',
  contactPersonPh: lang.value === 'en' ? 'Your full name' : '您的姓名',
  email: lang.value === 'en' ? 'Email' : '邮箱',
  phone: lang.value === 'en' ? 'Phone' : '电话',
  phonePh: lang.value === 'en' ? '+1 (555) 000-0000' : '+86 138 0000 0000',
  country: lang.value === 'en' ? 'Country / Region' : '国家 / 地区',
  countryPh: lang.value === 'en' ? 'e.g. United States' : '例如：美国',
  businessType: lang.value === 'en' ? 'Business Type' : '业务类型',
  selectType: lang.value === 'en' ? 'Select type' : '请选择',
  typeRetail: lang.value === 'en' ? 'Retail Store' : '线下零售店',
  typeOnline: lang.value === 'en' ? 'Online Store' : '线上商城',
  typeDistributor: lang.value === 'en' ? 'Distributor' : '经销商',
  typeWholesaler: lang.value === 'en' ? 'Wholesaler' : '批发商',
  typeOther: lang.value === 'en' ? 'Other' : '其他',
  interestedIn: lang.value === 'en' ? 'Product Categories Interested In' : '感兴趣的产品分类',
  estimatedQty: lang.value === 'en' ? 'Estimated Order Quantity' : '预估订单数量',
  selectRange: lang.value === 'en' ? 'Select range' : '请选择范围',
  units: lang.value === 'en' ? 'units' : '件',
  whiteLabel: lang.value === 'en' ? 'White Label / OEM' : '白牌 / OEM',
  wlYes: lang.value === 'en' ? 'Yes, I need white label' : '是的，需要白牌服务',
  wlNo: lang.value === 'en' ? 'No, standard packaging is fine' : '不需要，标准包装即可',
  message: lang.value === 'en' ? 'Message / Additional Details' : '留言 / 补充说明',
  messagePh: lang.value === 'en' ? 'Tell us more about your business needs...' : '请告诉我们更多您的业务需求...',
  submit: lang.value === 'en' ? 'Submit Request' : '提交申请',
  sending: lang.value === 'en' ? 'Sending...' : '发送中...',
  successTitle: lang.value === 'en' ? 'Thank You!' : '感谢您的咨询！',
  successMessage: lang.value === 'en'
    ? 'Our wholesale team will contact you within 24 hours.'
    : '我们的批发团队将在24小时内与您联系。',
  submitAnother: lang.value === 'en' ? 'Submit Another Request' : '再提交一份申请',
}))

const benefits = [
  {
    titleKey: 'quality',
    icon: 'M30 5 L30 15 M15 25 L15 55 M45 25 L45 55 M5 35 L25 35 M35 35 L55 35',
    color: '#dd5da2'
  },
  {
    titleKey: 'pricing',
    icon: 'M10 45 L25 30 L35 38 L50 15 M10 50 L50 50',
    color: '#e5c000'
  },
  {
    titleKey: 'whitelabel',
    icon: 'M30 10 L45 25 L30 40 L15 25 Z M15 45 L45 45',
    color: '#f29520'
  },
  {
    titleKey: 'shipping',
    icon: 'M10 20 L50 20 L50 40 L10 40 Z M30 20 L30 40 M20 10 L30 20 L40 10 M10 40 L20 50 M40 50 L50 40',
    color: '#8b5cf6'
  },
  {
    titleKey: 'fast',
    icon: 'M30 5 A25 25 0 1 1 5 30 L30 30 L30 5',
    color: '#06b6d4'
  },
  {
    titleKey: 'support',
    icon: 'M30 20 A10 10 0 1 1 20 30 M10 45 Q10 35 30 35 Q50 35 50 45',
    color: '#10b981'
  }
]

const benefitText = computed(() => ({
  quality: { title: lang.value === 'en' ? 'Premium Quality' : '优质品质', desc: lang.value === 'en' ? 'All products are made with medical-grade materials and pass rigorous quality testing.' : '所有产品均采用医疗级材料制造，经过严格的质量检测。' },
  pricing: { title: lang.value === 'en' ? 'Competitive Pricing' : '有竞争力的价格', desc: lang.value === 'en' ? 'Tiered wholesale pricing with volume discounts. The more you order, the more you save.' : '分层批发价格，量大从优。订购越多，节省越多。' },
  whitelabel: { title: lang.value === 'en' ? 'White Label OEM' : '白牌 OEM', desc: lang.value === 'en' ? 'Custom branding, packaging, and product design to make the products truly yours.' : '定制品牌、包装和产品设计，让产品真正属于您。' },
  shipping: { title: lang.value === 'en' ? 'Global Shipping' : '全球配送', desc: lang.value === 'en' ? 'Worldwide shipping with discreet packaging. DHL, FedEx, UPS, and sea freight options.' : '全球配送，隐私包装。提供DHL、FedEx、UPS和海运选项。' },
  fast: { title: lang.value === 'en' ? 'Fast Turnaround' : '快速交付', desc: lang.value === 'en' ? 'Stock orders ship within 48 hours. Custom orders in 15-25 days.' : '现货订单48小时内发货。定制订单15-25天。' },
  support: { title: lang.value === 'en' ? 'Dedicated Support' : '专属支持', desc: lang.value === 'en' ? 'Personal account manager to assist you from inquiry to delivery and beyond.' : '专属客户经理，从咨询到交付及后续全程协助。' },
}))

const displayBenefits = computed(() => benefits.map((b, i) => ({
  ...b,
  title: benefitText.value[b.titleKey].title,
  desc: benefitText.value[b.titleKey].desc,
})))

const pricingTiers = computed(() => {
  const en = {
    starter: { name: 'Starter', price: '$6.99', moq: '10 units', features: ['Bulk discount pricing', 'Standard packaging', 'Discreet shipping', 'Email support', 'Mixed SKUs allowed'] },
    growth: { name: 'Growth', price: '$4.99', moq: '100 units', features: ['Up to 40% off retail', 'Custom logo option', 'Priority shipping', 'Dedicated account manager', 'Flexible payment terms', 'Free samples available'] },
    enterprise: { name: 'Enterprise', price: 'Custom', moq: '500+ units', features: ['Best pricing guaranteed', 'Full white label OEM', 'Custom product design', 'Air + sea freight', 'Private labeling', 'Exclusive distribution option', '24/7 priority support'] },
  }
  const zh = {
    starter: { name: '入门版', price: '¥49.99', moq: '10件起', features: ['批量折扣价', '标准包装', '隐私配送', '邮件支持', '可混合SKU'] },
    growth: { name: '成长版', price: '¥34.99', moq: '100件起', features: ['最高40%折扣', '可定制Logo', '优先发货', '专属客户经理', '灵活付款条件', '可提供样品'] },
    enterprise: { name: '企业版', price: '面议', moq: '500件起', features: ['保证最优价格', '完整白牌OEM', '定制产品设计', '空运+海运', '自有品牌', '独家经销选项', '24/7优先支持'] },
  }
  const text = lang.value === 'en' ? en : zh
  return [
    { ...text.starter, featured: false },
    { ...text.growth, featured: true },
    { ...text.enterprise, featured: false },
  ]
})

const categoryTags = computed(() => lang.value === 'en'
  ? ['Wand Massagers', 'Vibrators', 'Kegel Balls', 'Couples Toys', 'Suction Stimulators', 'Rabbit Vibrators', 'Accessories', 'Lubricants', 'Bondage', 'Dildos', 'Male Toys', 'Lingerie']
  : ['震动棒', '振动器', '凯格尔球', '情侣玩具', '吮吸刺激器', '兔子跳蛋', '配件', '润滑液', '束缚', '仿真阳具', '男用玩具', '内衣']
)

const interestCategories = computed(() => lang.value === 'en'
  ? [
      { value: 'wand', label: 'Wand Massagers' },
      { value: 'vibrator', label: 'Vibrators' },
      { value: 'couples', label: 'Couples Toys' },
      { value: 'kegel', label: 'Kegel Balls' },
      { value: 'suction', label: 'Suction Stimulators' },
      { value: 'accessories', label: 'Accessories' },
      { value: 'male', label: 'Male Toys' },
      { value: 'lingerie', label: 'Lingerie' },
    ]
  : [
      { value: 'wand', label: '震动棒' },
      { value: 'vibrator', label: '振动器' },
      { value: 'couples', label: '情侣玩具' },
      { value: 'kegel', label: '凯格尔球' },
      { value: 'suction', label: '吮吸刺激器' },
      { value: 'accessories', label: '配件' },
      { value: 'male', label: '男用玩具' },
      { value: 'lingerie', label: '内衣' },
    ]
)

const trustItems = computed(() => lang.value === 'en'
  ? [
      { number: '500+', label: 'Global Partners' },
      { number: '50+', label: 'Countries Served' },
      { number: '1M+', label: 'Units Sold' },
      { number: '24/7', label: 'Support' },
    ]
  : [
      { number: '500+', label: '全球合作伙伴' },
      { number: '50+', label: '服务国家' },
      { number: '100万+', label: '销售件数' },
      { number: '24/7', label: '客户支持' },
    ]
)

const scrollToForm = () => {
  document.getElementById('contact-form')?.scrollIntoView({ behavior: 'smooth' })
}

const handleSubmit = async () => {
  isSubmitting.value = true
  try {
    await submitInquiry({
      company_name: form.company,
      contact_person: form.name,
      email: form.email,
      phone: form.phone,
      country: form.country,
      business_type: form.businessType,
      interests: form.interests,
      quantity: form.quantity,
      whitelabel: form.whitelabel,
      message: form.message,
    })
    submitSuccess.value = true
  } catch (err) {
    alert(lang.value === 'en'
      ? `Submission failed: ${err.message}`
      : `提交失败：${err.message}`
    )
  } finally {
    isSubmitting.value = false
  }
}

const resetForm = () => {
  submitSuccess.value = false
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
    refreshObserver()
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
  color: var(--color-text-light);
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

.success-message {
  text-align: center;
  padding: 2rem 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.success-icon {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: var(--color-flavor);
  color: white;
  font-size: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
}

.success-message h3 {
  font-size: 1.5rem;
}

.success-message p {
  color: var(--color-text-light);
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
