import Button from '@material-ui/core/Button';
import React from "react";

type Props = {
  button_name: string
}

const PrimarySubmitButton: React.FC<Props> = ({button_name}) => {
 return (
    <Button variant="contained" color="primary" type="submit" >
      {button_name}
    </Button>
  )

}

export default PrimarySubmitButton;