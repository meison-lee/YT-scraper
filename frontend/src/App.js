import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Note from "./component/note";
import Search from "./component/search";

function App() {
  return (
    <Router>
    <Routes>
      <Route path="/"  element={<Search/>} />
      <Route path="/note"  element={<Note/>} />
      {/* <Route path="/note" element={</>} />
      <Route element={<ProtectedRoute />}>
        <Route path="/note" element={<TextEditor/>} />
      </Route> */}
    </Routes>
  </Router>
  );
}

export default App;
