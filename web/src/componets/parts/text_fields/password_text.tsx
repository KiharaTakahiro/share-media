/**
 * ユーザのパスワード入力用のテキストフィールド
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

interface ValidationRule {
  required?: string
  maxLength: {
    value: number,
    message: string
  }
}

const PasswordText: React.FC<Props> = ({required, default_value, id, register, errors}) => {
  const validation_rule = (required: boolean) => {
    var component_rule: ValidationRule = {
      maxLength: {
        value: 15,
        message: "パスワードは15文字以内で入力してください"
      }
    }
    if (required) {
      component_rule['required'] = "パスワードは必須です"
    }
    return component_rule
  }

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