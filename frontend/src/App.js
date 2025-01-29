import './App.css';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import LandingPage from './Components/LandingPage/LandingPage';
import Problem from './Components/Problem/Problem';
import Problems from './Components/Problems/Problems';
import Contests from './Components/Contests/Contests';
import Contest from './Components/Contest/Contest';
import Users from './Components/Users/Users';
import User from './Components/User/User';

import Test from './Components/Test/Test';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<LandingPage />}/>
        <Route path='/problems' element={<Problems />}/>
        <Route path='/problems/:id' element={<Problem />}/>
        <Route path='/contests/' element={<Contests />}/>
        <Route path='/contests/:id' element={<Contest />}/>
        <Route path='/users' element={<Users />}/>
        <Route path='/users/:id' element={<User />}/>
      </Routes>
    </Router>
  );
}

export default App;
