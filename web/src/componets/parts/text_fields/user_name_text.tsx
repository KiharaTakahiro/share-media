/**
 * ユーザのユーザ名入力用のテキストフィールド
 */
import TextField from '@material-ui/core/TextField'
import React from "react"
import { RegConst } from "../../../common/const"

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

interface ValidationRule {
  required?: string
  maxLength: {
    value: number,
    message: string
  }
  pattern:{
    value: RegExp
    message: string
  }
}

const UserNameText: React.FC<Props> = ({required, default_value, id, register, errors}) => {

  const validation_rule = (required: boolean) => {
    var component_rule: ValidationRule = {
      maxLength: {
        value: 10,
        message: "ユーザ名は10文字以内で入力してください"
      },
      pattern: {
        value: RegConst.HANKAKU_EISU,
        message: "ユーザ名は半角英数字で入力してください"
      }
    }
    if (required) {
      component_rule['required'] = "ユーザ名は必須です"
    }
    return component_rule
  }

  return (
    <TextField 
      required={required}
      defaultValue={default_value}
      id={id}
      inputRef={register(validation_rule(required))}
      name="username"
      label="ユーザ名"
      variant="outlined"
      error={Boolean(errors.username)}
      helperText={errors.username && errors.username.message}/>
  )
};

export default UserNameText;