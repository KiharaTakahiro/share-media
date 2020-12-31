/**
 * ユーザの年齢入力用のテキストフィールド
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

const AgeText: React.FC<Props> = ({required, default_value, id, register, errors}) => {

  const validation_rule = (required: boolean) => {
    var component_rule: ValidationRule = {
      maxLength: {
        value: 3,
        message: "年齢は3文字以内で入力してください"
      }
    }
    if (required) {
      component_rule['required'] = "年齢は必須です"
    }
    return component_rule
  }

  return (
    <TextField 
      required={required}
      defaultValue={default_value}
      id={id}
      inputRef={register(validation_rule(required))}
      name="age"
      label="年齢"
      variant="outlined"
      type="number"
      error={Boolean(errors.age)}
      helperText={errors.age && errors.age.message}/>
  )
};

export default AgeText;