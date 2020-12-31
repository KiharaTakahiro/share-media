/**
 * ユーザのEmail入力用のテキストフィールド
 */
import TextField from '@material-ui/core/TextField'
import React from "react"
import { RegConst } from "../../../common/const"

type Props = {
  /**
   * register
   */
  register: any
  /**
   * errors属性
   */
  errors: any
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
}

interface ValidationRule {
  required?: string
  maxLength: {
    value: number,
    message: string
  }
  pattern: {
    value: RegExp,
    message: string
  }
}

const EMailText: React.FC<Props> = ({required, default_value, id, register, errors}) => {

  /**
   * 最大文字数
   */
  const MAX_LENGTH = 30

  /**
   * バリデーションルール
   * @param required 
   */
  const validation_rule = (required: boolean) => {
    var component_rule: ValidationRule = {
      maxLength: {
        value: MAX_LENGTH,
        message: `emailは${MAX_LENGTH}文字以内で入力してください`
      },
      pattern: {
        value: RegConst.EMAIL,
        message: "emailアドレスの形式で入力してください"
      }
    }
    if (required) {
      component_rule['required'] = "emailは必須です"
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
      name="email"
      label="email"
      variant="outlined"
      error={Boolean(errors.email)}
      helperText={errors.email && errors.email.message}/>
  )
};

export default EMailText;