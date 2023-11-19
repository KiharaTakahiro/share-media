import React from "react"
import PrimarySubmitButton from "../parts/buttons/primary_submit_button"
import UserNameText from "../parts/text_fields/user_name_text"
import PasswordText from "../parts/text_fields/password_text"
import PartsTitle from "../parts/styles/title"
import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'
import { useForm } from 'react-hook-form'
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles'

type Props = {
  login: any // ログイン処理
}

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

const LoginUserTemplate: React.FC<Props> = ({ login }) => {
  const classes = useStyles()
  const { handleSubmit, register, errors } = useForm()

  return (
    <>
      <Grid container direction="column" justify="center" alignItems="center">
        <PartsTitle title="ログイン"/>
        <Paper  elevation={3}>
          <form className={classes.root} onSubmit={handleSubmit(login)}>
            <Grid container direction="column" justify="center" alignItems="center">
              <UserNameText required register={register} errors={errors}/>
              <PasswordText required register={register} errors={errors}/> 
              <PrimarySubmitButton button_name="ログイン"/>
            </Grid>
          </form>
        </Paper>
      </Grid>
    </>
  )
}

export default LoginUserTemplate