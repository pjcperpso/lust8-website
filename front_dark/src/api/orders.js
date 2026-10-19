// Orders API
import http from './http'

export function createOrder(data) {
  return http.post('/orders', data)
}

export function getMyOrders() {
  return http.get('/orders')
}

export function getOrder(id) {
  return http.get(`/orders/${id}`)
}

export default {
  createOrder,
  getMyOrders,
  getOrder,
}
