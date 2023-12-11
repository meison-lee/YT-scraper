import React, { useState, useEffect, useContext} from 'react';
import { AuthContext } from '../AuthContext';

const Note = () => {

  const {video, setVideo} = useContext(AuthContext);

  useEffect(() => {
    console.log(video)
  })


  return (
    <div style={{ width: '900px', height: '500px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
      <iframe src={video} title='test' style={{ width: '80%', height: '80%', border: 'none' }}></iframe>
    </div>
  );
};

export default Note;
