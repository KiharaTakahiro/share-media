import Button from '@material-ui/core/Button';
import React from "react";

type Props = {
  button_name: string;
}

const PrimaryButton: React.FC<Props> = ({button_name}) => (
    <Button variant="contained" color="primary">
      {button_name}
    </Button>
  );

export default PrimaryButton;