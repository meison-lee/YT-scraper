import React, { useState, useEffect, useContext} from 'react';
import { AuthContext } from '../AuthContext';

const Note = () => {
  const [note, setNote] = useState('');
  const {video, setVideo} = useContext(AuthContext);

  useEffect(() => {
    console.log(video)
  })

  const handleNoteChange = (event) => {
    setNote(event.target.value);
  };

  const handleSaveNote = () => {
    // Save the note here
    console.log(note);
  };


  return (
    <div style={{
      width: '90%',
      height: '90%',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      position: 'absolute',
      top: '50%',
      left: '50%',
      transform: 'translate(-50%, -50%)'
    }}>
      <iframe src={video.videoId} title={video.title} style={{ width: '50%', height: '80%', border: 'none' }}></iframe>
      <h1>{video.title}</h1>
      <textarea value={note} onChange={handleNoteChange} style={{ width: '80%', height: '80%', border: 'solid' }} />
      <button onClick={handleSaveNote}>Save Note</button>
    </div>
  );
};

export default Note;
