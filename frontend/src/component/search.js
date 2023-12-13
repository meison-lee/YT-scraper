import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import VideoButton from './videoButton';
import { AuthContext } from '../AuthContext';

const SearchComponent = () => {

  const { video, setVideo } = useContext(AuthContext);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const navigate = useNavigate();

  const handleSearch = async () => {

    try {

      console.log('query', query)
      axios.get('http://localhost:8080/api/search?query=' + query)
        .then(response => {
          // handle response
          console.log(response.data);
          setResults(response.data);
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
    setVideo(video);
    navigate('/note');
  };

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'flex-start',
      height: '100vh'
    }}>
      <div style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        marginBottom: '20px'
      }}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder='Search for video...'
          style={{
            fontSize: '1.5em',
            padding: '10px',
            borderRadius: '5px',
            border: '1px solid #ccc',
            marginBottom: '10px',
            width: '80%'
          }}
        />
        <button onClick={handleSearch} style={{
          fontSize: '1.5em',
          padding: '10px',
          borderRadius: '5px',
          border: 'none',
          backgroundColor: '#007BFF',
          color: 'white',
          cursor: 'pointer',
          width: '80%'
        }}>Search</button>
      </div>
      <div className='videos_square' style={{ display: 'flex', justifyContent: 'space-around', flexWrap: 'wrap' }}>
        {results.map((item, index) => (
          <VideoButton key={index} video={item} chooseVideo={chooseVideo} />
        ))}
      </div>
    </div>
  );
};

export default SearchComponent;
