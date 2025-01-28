import './App.css';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import LandingPage from './Components/LandingPage/LandingPage';
import Problem from './Components/Problem/Problem';
import Problems from './Components/Problems/Problems';
import Test from './Components/Test/Test';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<LandingPage />}/>
        <Route path='/problems' element={<Problems />}/>
        <Route path='/problems/:id' element={<Problem />}/>
      </Routes>
    </Router>
  );
}

export default App;
