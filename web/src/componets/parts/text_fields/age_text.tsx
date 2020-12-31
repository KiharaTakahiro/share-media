/**
 * ユーザの年齢入力用のテキストフィールド
 */
import TextField from '@material-ui/core/TextField'
import React from "react"

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
  max: {
    value: number,
    message: string
  }
  min: {
    value: number,
    message: string
  }
}

const AgeText: React.FC<Props> = ({required, default_value, id, register, errors}) => {

  /**
   * 最大の年齢
   */
  const MAX_AGE = 200
  
  /**
   * 最小の年齢
   */
  const MIN_AGE = 15
  
  /**
   * バリデーションルール
   * @param required 
   */
  const validation_rule = (required: boolean) => {
    var component_rule: ValidationRule = {
      max: {
        value: MAX_AGE,
        message: `年齢は${MAX_AGE}才以内で入力してください`
      },
      min: {
        value: MIN_AGE,
        message: `年齢は${MIN_AGE}才以上で入力してください`
      }
    }
    if (required) {
      component_rule['required'] = "年齢は必須です"
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
      name="age"
      label="年齢"
      variant="outlined"
      type="number"
      error={Boolean(errors.age)}
      helperText={errors.age && errors.age.message}/>
  )
};

export default AgeText;