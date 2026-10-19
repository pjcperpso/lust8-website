// Newsletter API
import http from './http'

export function subscribe(email) {
  return http.post('/newsletter/subscribe', { email })
}

export function unsubscribe(email) {
  return http.post('/newsletter/unsubscribe', { email })
}

export default {
  subscribe,
  unsubscribe,
}
