// Products API
import http from './http'

export function getProducts(params = {}) {
  return http.get('/products', params)
}

export function getFeaturedProducts(limit = 6, lang = 'en') {
  return http.get('/products/featured', { limit, lang })
}

export function getCategories(lang = 'en') {
  return http.get('/products/categories', { lang })
}

export function getProduct(idOrSlug, lang = 'en') {
  return http.get(`/products/${idOrSlug}`, { lang })
}

export default {
  getProducts,
  getFeaturedProducts,
  getCategories,
  getProduct,
}
