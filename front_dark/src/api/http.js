// HTTP client wrapper with base URL, auth token, and error handling
import { getToken, clearAuth } from './auth'

const BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'

async function request(path, options = {}) {
  const url = path.startsWith('http') ? path : `${BASE_URL}${path}`

  const headers = {
    'Content-Type': 'application/json',
    ...options.headers,
  }

  const token = getToken()
  if (token) {
    headers['Authorization'] = `Bearer ${token}`
  }

  const config = {
    ...options,
    headers,
    credentials: 'include', // send cookies (session_id for guest cart)
  }

  if (options.body && typeof options.body !== 'string' && !(options.body instanceof FormData)) {
    config.body = JSON.stringify(options.body)
  }

  try {
    const res = await fetch(url, config)

    // Handle 401 - clear token and redirect
    if (res.status === 401) {
      clearAuth()
    }

    const data = await res.json().catch(() => ({}))

    if (!res.ok) {
      throw new ApiError(res.status, data.detail || data.message || 'Request failed', data)
    }

    return data
  } catch (err) {
    if (err instanceof ApiError) throw err
    throw new ApiError(0, 'Network error', null)
  }
}

export class ApiError extends Error {
  constructor(status, message, data) {
    super(message)
    this.status = status
    this.data = data
  }
}

export const http = {
  get: (path, params) => {
    let url = path
    if (params) {
      const search = new URLSearchParams()
      Object.entries(params).forEach(([k, v]) => {
        if (v !== undefined && v !== null && v !== '') {
          search.append(k, v)
        }
      })
      const qs = search.toString()
      if (qs) url += `?${qs}`
    }
    return request(url, { method: 'GET' })
  },
  post: (path, body) => request(path, { method: 'POST', body }),
  put: (path, body) => request(path, { method: 'PUT', body }),
  patch: (path, body) => request(path, { method: 'PATCH', body }),
  delete: (path) => request(path, { method: 'DELETE' }),
}

export default http
