/**
 * ユーザのEmail入力用のテキストフィールド
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

const EMailText: React.FC<Props> = ({required, default_value, id, register, errors}) => {
  return (
    <TextField 
      required={required}
      defaultValue={default_value}
      id={id}
      inputRef={register({ required: required, maxLength: 30 })}
      name="email"
      label="email"
      variant="outlined"
      error={Boolean(errors.title)}
      helperText={errors.title && "emailは10文字以内にして下さい。"}/>
  )
};

export default EMailText;