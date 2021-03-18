import React, {useEffect} from 'react'
import MenuTemplate from '../components/templates/menu_template';
import { logout } from '../common/auth'
import { NextPageContext } from 'next'
import ApiCaller from '../common/api_caller'

const Menu = (ctx: NextPageContext) => {
  const page_logout = () => {
    logout(ctx)
  }
  const get_user = () => {
    ApiCaller.get("/users/me")
    .then(response => {
        console.log(response)
    })
    .catch(error => {
      console.log(error)
    })
  }

  useEffect(() => {
    get_user()
  })

  return (
    <MenuTemplate logout={page_logout}/>
  )
} 

export default Menu;
