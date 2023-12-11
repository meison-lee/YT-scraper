import React, { useState, useContext} from 'react';
import { useNavigate} from 'react-router-dom';
import axios from 'axios';
import VideoButton from './videoButton';
import { AuthContext } from '../AuthContext';

const SearchComponent = () => {

  const {video, setVideo} = useContext(AuthContext);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const navigate = useNavigate();

  const handleSearch = async () => {

    try {

      console.log('query', query )
      axios.get('http://localhost:8080/api/search?query='+query)
     .then(response => {
         // handle response
        console.log(response.data[1][0]);
        setResults(response.data[1]);
     })
     .catch(error => {
         console.error('Error:', error);
     });
    } catch (error) {
      console.error('Error fetching data: ', error);
      setResults([]);
    }
  };

  const chooseVideo = (video) => {
    // Handle the video selection
    // For example, you might update the state to show the selected video
    console.log("Selected video:", video);
    setVideo(video);
    navigate('/note');
  };

  return (
    <div >
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
      <div className='videos_square' style={{display:'flex', justifyContent:'space-around', flexWrap:'wrap'}}>
        {results.map((item, index) => (
          <VideoButton key={index} video={item} chooseVideo={chooseVideo}/>
          // <iframe key={index} src={item} title="W3Schools Free Online Web Tutorials"></iframe>
        ))}
      </div>
    </div>
  );
};

export default SearchComponent;
