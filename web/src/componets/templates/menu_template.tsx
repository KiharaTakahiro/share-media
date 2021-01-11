import React from "react";
import PrimaryClickButton from '../parts/buttons/primary_click_button'

type Props = {
  logout: any
}

const MenuTemplate: React.FC<Props> = ({logout}) => {
  return (
    <>
      <div>ログイン後のメニュー</div>
      <PrimaryClickButton button_name="ログアウト" onClick={logout} />
    </>
  )
}

export default MenuTemplate;