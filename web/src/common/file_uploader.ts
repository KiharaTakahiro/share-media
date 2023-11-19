import axios from "axios"
import { get_access_token, logout } from '../common/auth'

/**
 * バックエンドとの通信を行うための設定
 */
const instance = axios.create({
  baseURL: "http://localhost:8000/",
  timeout: 2000,
  headers: {
    Accept: "multipart/form-data",
    "Content-Type": "multipart/form-data"
  }
})

/**
 * リクエストのインターセプタ
 * config: requestが送信される前に実行される処理
 * error: then/catchの処理の「前に」実行されるエラーハンドリング
 */
instance.interceptors.request.use(
  config => {
    // tokenが存在する場合は再度
    const access_token = get_access_token()
    if (typeof access_token !== 'undefined') {
      config.headers = { Authorization: `Bearer ${access_token}` }
    }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

/**
 * レスポンスのインターセプタ
 * response: レスポンスを取得後の処理
 * error: エラー時の処理
 */
instance.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if(error.state == 401){
      logout()
    }
    return Promise.reject(error)
  }
)

export default instance