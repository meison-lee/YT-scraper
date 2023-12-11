import React, { useEffect } from 'react';

const VideoButton = ({video, chooseVideo}) => {

  useEffect(() => {
    console.log(video)
  })
  return (
    <div style={{gridTemplateColumns:'repeat(2, 1fr)', gap:'10px'}}>
      <iframe src={video} title='test' style={{ width: '80%', height: '80%', border: 'none' }}></iframe>
      <button onClick={() => chooseVideo(video)}
      style={{ marginTop: '20px', padding: '10px 20px' }}>
        O
      </button>
    </div>
  );
};

export default VideoButton;
