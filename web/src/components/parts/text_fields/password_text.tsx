/**
 * ユーザのパスワード入力用のテキストフィールド
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
  minLength:{
    value: number,
    message: string
  }
  pattern: {
    value: RegExp,
    message: string
  }
}

const PasswordText: React.FC<Props> = ({required, default_value, id, register, errors}) => {

  /**
   * 最大文字数
   */
  const MAX_LENGTH = 20

  /**
   * 最小文字数
   */
  const MIN_LENGHT = 8

  /**
   * バリデーションルール
   * @param required 
   */
  const validation_rule = (required: boolean) => {
    var component_rule: ValidationRule = {
      maxLength: {
        value: MAX_LENGTH,
        message: `パスワードは${MAX_LENGTH}文字以内で入力してください`
      },
      minLength: {
        value: MIN_LENGHT,
        message: `パスワードは${MIN_LENGHT}文字以上で入力してください`
      },
      pattern: {
        value: RegConst.HANKAKU_EISU_KIGOU,
        message: "パスワードは半角英数字か記号で入力してください"
      }
    }
    if (required) {
      component_rule['required'] = "パスワードは必須です"
    }
    return component_rule
  }

  /**
   * 表示領域
   */
  return (
    <TextField 
      required={required}
      defaultValue={default_value}
      id={id}
      inputRef={register(validation_rule(required))}
      type="password"
      name="password"
      label="パスワード"
      variant="outlined"
      error={Boolean(errors.password)}
      helperText={ errors.password && errors.password.message}/>
  )
};

export default PasswordText;