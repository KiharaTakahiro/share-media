import { PAGE_END_POINT } from '../common/const'
import { parseCookies, destroyCookie, setCookie} from 'nookies';
import { NextPageContext } from 'next';
import Router from 'next/router'

/**
 * トークンのインターフェース
 */
interface Token {
  access_token: string,
  refresh_token: string
}

/**
 * トークンの情報を取得する
 * @param ctx 
 */
export const get_access_token = (ctx?: NextPageContext): Token | any => {
  if(typeof parseCookies(ctx).access_token === 'undefined') {
    return undefined
  }
  return parseCookies(ctx).access_token;
}

export const set_token = (data: Token, ctx?: NextPageContext) =>{
  setCookie(ctx, "access_token", data.access_token , {
    maxAge: 24 * 60 * 60, // 1日で切れる
    path: '/'
  })
  setCookie(ctx, "refresh_token", data.refresh_token , {
    maxAge: 90 * 24 * 60 * 60, // 90日で切れる
    path: '/'
  })
}

/**
 * 認証不要ページの判定処理
 * @param url 
 */
export const exclude_login_route = (url: string) => {
  return url === PAGE_END_POINT.REGISTER_USER || url === PAGE_END_POINT.LOGIN_USER
}

/**
 * ログアウト処理
 */
export const logout = (ctx?: NextPageContext) => {
  destroyCookie(ctx, "access_token")
  destroyCookie(ctx, "refresh_token")
  Router.push(PAGE_END_POINT.LOGIN_USER)
}