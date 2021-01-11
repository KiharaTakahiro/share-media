import Button from '@material-ui/core/Button';
import React from "react";

type Props = {
  button_name: string
  onClick: any
}

const PrimaryClickButton: React.FC<Props> = ({button_name, onClick}) => {
 return (
    <Button variant="contained" color="primary" onClick={onClick} >
      {button_name}
    </Button>
  )

}

export default PrimaryClickButton;