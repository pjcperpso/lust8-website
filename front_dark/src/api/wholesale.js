// Wholesale API
import http from './http'

export function submitInquiry(data) {
  return http.post('/wholesale/inquiry', data)
}

export default {
  submitInquiry,
}
