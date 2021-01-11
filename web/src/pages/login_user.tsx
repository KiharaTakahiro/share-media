import React from 'react'
import LoginUserTemplate from '../componets/templates/login_user_template';
import ApiCaller from '../common/api_caller'
import Router from 'next/router'
import { set_token } from '../common/auth'
import { NextPageContext } from 'next'

const LoginUser = (ctx: NextPageContext) => {
    // TODO: ページに移す予定
    const login = (data: Object) => { 
      console.log(data)
      ApiCaller.post("/users/login", data)
      .then(response => {
        set_token(response.data, ctx)
        Router.push('/menu')
      })
      .catch(error => {
        console.log(error)
      })
    }
  
  return (
    <LoginUserTemplate login={login}/>
  )
}

export default LoginUser;