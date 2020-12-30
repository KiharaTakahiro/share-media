/**
 * ユーザのユーザ名入力用のテキストフィールド
 */
import TextField from '@material-ui/core/TextField'
import React from "react"

type Props = {
  /**
   * 必須(true)/必須ではない(false)
   */
  required?: boolean
  /**
   * 初期値
   */
  default_value?: string
  /**
   * id属性
   */
  id?: string
  /**
   * register
   */
  register?: any
  /**
   * errors属性
   */
  errors?: any
}

const UserNameText: React.FC<Props> = ({required, default_value, id, register, errors}) => {
  return (
    <TextField 
      required={required}
      defaultValue={default_value}
      id={id}
      inputRef={register({ required: required, maxLength: 10 })}
      name="username"
      label="ユーザ名"
      variant="outlined"
      error={Boolean(errors.title)}
      helperText={errors.title && "ユーザ名は10文字以内にして下さい。"}/>
  )
};

export default UserNameText;