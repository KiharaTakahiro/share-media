import React from "react"
import Grid from '@material-ui/core/Grid'
import PartsTitle from "../parts/styles/title"
import MovieUpload from '../../componets/parts/file_upload/movie_upload'
import { useForm } from 'react-hook-form'
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles'
import PrimarySubmitButton from "../parts/buttons/primary_submit_button"

type Props = {
  postmovie: any
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

const RegisterMovieTemplate: React.FC<Props> = ({ postmovie }) => {
  const classes = useStyles()
  const { handleSubmit, register, errors } = useForm()

  return (
    <>
      <Grid container direction="column" justify="center" alignItems="center">
        <PartsTitle title="動画投稿画面"/>
        <form className={classes.root} onSubmit={handleSubmit(postmovie)}>
          <MovieUpload register={register}/>
          <PrimarySubmitButton button_name="登録"/>
        </form>
      </Grid>
    </>
  )
}
export default RegisterMovieTemplate