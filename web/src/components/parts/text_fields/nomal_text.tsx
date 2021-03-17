import TextField from '@material-ui/core/TextField';
import React from "react";

type Props = {
  label?: string
  default_value?: string
  id?: string
  required?: boolean
}

const NomalText: React.FC<Props> = ({label, default_value, id, required}) => {
  return (
    <TextField required={required} id={id} label={label} defaultValue={default_value} variant="outlined"/>
  )
};

export default NomalText;