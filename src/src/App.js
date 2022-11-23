import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import GuestDashboard from './Pages/DashBoard/GuestDashboard';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<GuestDashboard />} />
      </Routes>
    </Router>
  );
}

export default App;
