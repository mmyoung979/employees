import './App.css';
import FetchApi from './FetchApi';
import ApiRequests from './ApiRequests';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ApiRequests />
        <FetchApi />
      </header>
    </div>
  );
}

export default App;
