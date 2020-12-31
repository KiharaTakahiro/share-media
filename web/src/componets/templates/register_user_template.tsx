import React from "react";
import PrimaryButton from "../parts/buttons/primary_button"
import UserNameText from "../parts/text_fields/user_name_text"
import PasswordText from "../parts/text_fields/password_text"
import EMailText from "../parts/text_fields/email_text"
import AgeText from "../parts/text_fields/age_text"
import PartsTitle from "../parts/styles/title"
import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'
import { useForm } from 'react-hook-form'
import ApiCaller from '../../service/api_caller'
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles'
import Router from 'next/router'

type Props = {}

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      '& .MuiTextField-root': {
        margin: theme.spacing(2),
        width: '40ch',
      },
      '& .MuiButton-root': {
        margin: theme.spacing(2),
        width: '52ch',
        height: '7ch'
      },

    },
  }),
)

const RegisterUserTemplate: React.FC<Props> = ({}) => {
  const classes = useStyles()
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
    Router.push('/complete_register_user')
  }

  return (
    <>
      <Grid container direction="column" justify="center" alignItems="center">
        <PartsTitle title="ユーザ登録"/>
        <Paper  elevation={3}>
          <form className={classes.root} onSubmit={handleSubmit(onSubmit)}>
            <Grid container direction="column" justify="center" alignItems="center">
              <UserNameText required register={register} errors={errors}/>
              <PasswordText required register={register} errors={errors}/> 
              <EMailText required register={register} errors={errors} />
              <AgeText register={register} errors={errors} />
              <PrimaryButton button_name="登録"/>
            </Grid>
          </form>
        </Paper>
      </Grid>
    </>
  )
}

export default RegisterUserTemplate;