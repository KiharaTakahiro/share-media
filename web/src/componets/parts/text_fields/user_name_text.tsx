import TextField from '@material-ui/core/TextField';
import React from "react";

type Props = {
  default_value?: string
  id?: string
  required?: boolean
}

const UserNameText: React.FC<Props> = ({default_value, id, required}) => {
  return (
    <TextField required={required} id={id} label="ユーザ名" defaultValue={default_value} variant="outlined"/>
  )
};

export default UserNameText;