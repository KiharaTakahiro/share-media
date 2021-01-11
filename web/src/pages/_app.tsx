import { NextPageContext } from 'next'
import { AppProps } from 'next/app'
import { useEffect } from 'react'
import { useRouter } from 'next/router'
import { exclude_login_route } from '../common/auth'
import { PAGE_END_POINT } from '../common/const'
import { get_access_token } from '../common/auth'

const MyApp = ({ Component, pageProps }: AppProps, ctx: NextPageContext) => {
  const router = useRouter()
  useEffect(() => {
    router.beforePopState(({ url }) => {
      if (!exclude_login_route(url) && typeof get_access_token(ctx) === 'undefined') {
        window.location.href = PAGE_END_POINT.LOGIN_USER
        return false
      }
      return true
    })
  }, [])

  return typeof pageProps === 'undefined' ? null : <Component {...pageProps} />
}

MyApp.getInitialProps = async (appContext: any) => {
  if (!exclude_login_route(appContext.ctx.pathname) && typeof get_access_token(appContext.ctx) === 'undefined') {
    if (typeof window === 'undefined') {
      appContext.ctx.res.statusCode = 302
      appContext.ctx.res.setHeader('Location', PAGE_END_POINT.LOGIN_USER)
      return {}
    }
  }
  return {
    pageProps: {
      ...(appContext.Component.getInitialProps
        ? await appContext.Component.getInitialProps(appContext.ctx)
        : {}),
      pathname: appContext.ctx.pathname,
    },
  }
}

export default MyApp