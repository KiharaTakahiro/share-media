import axios from "axios"

/**
 * バックエンドとの通信を行うための設定
 */
const instance = axios.create({
  baseURL: "http://localhost:8000/",
  timeout: 2000,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json"
  }
})

/**
 * リクエストのインターセプタ
 * config: requestが送信される前に実行される処理
 * error: then/catchの処理の「前に」実行されるエラーハンドリング
 */
instance.interceptors.request.use(
  config => {
    // request.headers.common["Authorization"] = "AUTH_TOKEN";
    
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
    return Promise.reject(error);
  }
)

export default instance