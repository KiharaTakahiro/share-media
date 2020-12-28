import TextField from '@material-ui/core/TextField';
import React from "react";

type Props = {
  label?: string
  default_value?: string
}

const RequireText: React.FC<Props> = ({label, default_value}) => (
<div>
  <TextField required label={label} defaultValue={default_value} variant="outlined"/>
</div>
  );

export default RequireText;