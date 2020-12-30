import TextField from '@material-ui/core/TextField';
import React from "react";

type Props = {
  default_value?: string
  id?: string
  required?: boolean
}

const PasswordText: React.FC<Props> = ({default_value, id, required}) => {
  return (
    <TextField required={required} id={id} label="パスワード" defaultValue={default_value} variant="outlined"/>
  )
};

export default PasswordText;