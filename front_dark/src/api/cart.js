// Cart API
import http from './http'

export function getCart(lang = 'en') {
  return http.get('/cart', { lang })
}

export function addToCart(productId, quantity = 1, selectedColor = '', lang = 'en') {
  return http.post('/cart', { product_id: productId, quantity, selected_color: selectedColor, lang })
}

export function updateCartItem(itemId, quantity) {
  return http.put(`/cart/${itemId}`, { quantity })
}

export function removeCartItem(itemId) {
  return http.delete(`/cart/${itemId}`)
}

export function clearCart() {
  return http.delete('/cart')
}

export default {
  getCart,
  addToCart,
  updateCartItem,
  removeCartItem,
  clearCart,
}
