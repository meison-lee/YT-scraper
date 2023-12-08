import React, { useEffect } from 'react';

const VideoButton = ({video, chooseVideo}) => {

  useEffect(() => {
    console.log(video)
  })
  return (
    <div >
      <iframe src={video} title='test'></iframe>
      <button onClick={() => chooseVideo(video)}>O</button>
    </div>
  );
};

export default VideoButton;
