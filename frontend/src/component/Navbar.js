import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {

  return (
    <div style={{height:'40px', width:'100%', backgroundColor:'#dfdfdf'}}>
      <Link to="/" style={{margin: '10px'}}>Home</Link>
    </div>
  );
};

export default Navbar;
