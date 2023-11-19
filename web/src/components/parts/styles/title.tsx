import React from "react";
import Typography from "@material-ui/core/Typography";

type Props = {
  title: string
}

const PartsTitle: React.FC<Props> = ({title}) => (
<Typography variant="h5" component="h2">
  {title}
</Typography>
  );
  export default PartsTitle;