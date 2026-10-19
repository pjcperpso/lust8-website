// Cart store - reactive global state with API sync
import { reactive } from 'vue'
import { getCart, addToCart as apiAddToCart, updateCartItem, removeCartItem, clearCart as apiClearCart } from '../api/cart'

const state = reactive({
  items: [],
  totalItems: 0,
  totalPrice: 0,
  loaded: false,
  loading: false,
})

let loadPromise = null

export async function fetchCart(lang = 'en') {
  if (state.loading && loadPromise) return loadPromise

  state.loading = true
  loadPromise = (async () => {
    try {
      const data = await getCart(lang)
      state.items = data.items
      state.totalItems = data.total_items
      state.totalPrice = data.total_price
      state.loaded = true
    } catch (err) {
      console.warn('Failed to fetch cart:', err.message)
      state.items = []
      state.totalItems = 0
      state.totalPrice = 0
      state.loaded = true
    } finally {
      state.loading = false
      loadPromise = null
    }
  })()

  return loadPromise
}

export async function addProductToCart(productId, quantity = 1, selectedColor = '', lang = 'en') {
  try {
    const data = await apiAddToCart(productId, quantity, selectedColor, lang)
    state.items = data.items
    state.totalItems = data.total_items
    state.totalPrice = data.total_price
    state.loaded = true
    return data
  } catch (err) {
    console.error('Add to cart failed:', err.message)
    throw err
  }
}

export async function updateQuantity(itemId, quantity) {
  try {
    const data = await updateCartItem(itemId, quantity)
    state.items = data.items
    state.totalItems = data.total_items
    state.totalPrice = data.total_price
    return data
  } catch (err) {
    console.error('Update cart failed:', err.message)
    throw err
  }
}

export async function removeItem(itemId) {
  try {
    const data = await removeCartItem(itemId)
    state.items = data.items
    state.totalItems = data.total_items
    state.totalPrice = data.total_price
    return data
  } catch (err) {
    console.error('Remove cart item failed:', err.message)
    throw err
  }
}

export async function clearCartItems() {
  try {
    await apiClearCart()
    state.items = []
    state.totalItems = 0
    state.totalPrice = 0
  } catch (err) {
    console.error('Clear cart failed:', err.message)
    throw err
  }
}

export function useCartStore() {
  return {
    state,
    fetchCart,
    addProductToCart,
    updateQuantity,
    removeItem,
    clearCartItems,
  }
}

export default useCartStore
