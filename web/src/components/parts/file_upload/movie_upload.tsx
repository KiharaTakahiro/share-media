import React, { Key } from 'react'
import { useDropzone } from 'react-dropzone'

type Props = {
  register: any
}

const MovieUpload: React.FC<Props> = ({ register }) => {
  const {acceptedFiles, getRootProps, getInputProps} = useDropzone()
  const files = acceptedFiles.map(file => (
    <li key={file.name}>
      {file.name} - {file.size} bytes
    </li>
  ))
  return (
    <>
      <section className="container">
        <div {...getRootProps({className: 'dropzone', ref: {register}})}>
          <input {...getInputProps()}/>
          <p>ファイルを選択してください</p>
        </div>
        <aside>
          <h4>Files</h4>
          <ul>{files}</ul>
        </aside>
      </section>
    </>
  )

}

export default MovieUpload