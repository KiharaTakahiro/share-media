import React from 'react'
import RegisterUserTemplate from '../components/templates/register_user_template';
import ApiCaller from '../common/api_caller'
import Router from 'next/router'

const RegisterUser = () => {
  
  // ユーザ取得処理
  const register_user = (data: Object) => { 
    console.log(data)
    ApiCaller.post("users/create", data)
    .then(response => {
      Router.push('/complete_register_user')
    })
    .catch(error => {
      // TODO: エラーメッセージを表示するようにしたい
      console.log(error.response.data)
    })
  }

  return (
    <RegisterUserTemplate register_user={register_user}/>
  )
} 

export default RegisterUser;