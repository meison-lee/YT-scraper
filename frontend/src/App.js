import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Note from "./component/note";
import Search from "./component/search";
import Navbar from './component/Navbar';

function App() {
  return (
    <Router>
      <Navbar/>
      <Routes>
        <Route path="/"  element={<Search/>} />
        <Route path="/note"  element={<Note/>} />
      </Routes>
    </Router>
  );
}

export default App;
