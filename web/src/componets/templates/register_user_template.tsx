import React from "react";
import PrimaryButton from "../parts/buttons/primary_button"
import RequireText from "../parts/text_fields/nomal_text"
import UserNameText from "../parts/text_fields/user_name_text"
import PartsTitle from "../parts/styles/title"
import Grid from '@material-ui/core/Grid'

type Props = {}

const RegisterUserTemplate: React.FC<Props> = ({}) => (
  <Grid container direction="column" justify="center" alignItems="center">
    <PartsTitle title="ユーザ登録画面"/>
    <UserNameText required id="username"/>
    <RequireText required id="password" label="パスワード" />
    <RequireText required id="email" label="email" />
    <RequireText id="age" label="年齢" />
    <PrimaryButton button_name="登録"/>
  </Grid>
);

export default RegisterUserTemplate;