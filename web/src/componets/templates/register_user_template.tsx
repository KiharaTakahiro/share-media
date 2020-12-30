import React from "react";
import PrimaryButton from "../parts/buttons/primary_button"
import UserNameText from "../parts/text_fields/user_name_text"
import PasswordText from "../parts/text_fields/password_text"
import EMailText from "../parts/text_fields/email_text"
import AgeText from "../parts/text_fields/age_text"
import PartsTitle from "../parts/styles/title"
import Grid from '@material-ui/core/Grid'
import { useForm } from 'react-hook-form'
import ApiCaller from '../../service/api_caller'

type Props = {}

const RegisterUserTemplate: React.FC<Props> = ({}) => {
  const { handleSubmit, register, errors } = useForm()
  const onSubmit = (data: Object) => { 
    console.log(data)
    ApiCaller.post("users/create", data)
    .then(response => {
      console.log(response)
    })
    .catch(error => {
      console.log(error)
    })
  }
  return (
    <Grid container direction="column" justify="center" alignItems="center">
      <PartsTitle title="ユーザ登録画面"/>
      <form onSubmit={handleSubmit(onSubmit)}>
        <UserNameText required register={register} errors={errors}/>
        <PasswordText required register={register} errors={errors} />
        <EMailText required register={register} errors={errors} />
        <AgeText register={register} errors={errors} />
        <PrimaryButton button_name="登録"/>
      </form>
    </Grid>
  )
};

export default RegisterUserTemplate;