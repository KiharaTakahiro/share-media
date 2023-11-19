import React from 'react'
import RegisterMovieTemplate from '../componets/templates/register_movie_template'
import ApiCaller from '../common/file_uploader'

const RegisterMovie = () => {
  // 動画登録処理
  const register_movie = (data: Object) => { 
    console.log(data)
    ApiCaller.post("movies/upload_file", data)
    .then(response => {
      console.log(response)
    })
    .catch(error => {
      // TODO: エラーメッセージを表示するようにしたい
      console.log(error.response.data)
    })
  }
  return (
    <>
      <RegisterMovieTemplate postmovie={register_movie}/>
    </>
  )
}

export default RegisterMovie