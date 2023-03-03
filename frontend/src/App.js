import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <div className="app-title">
          <h1>ARCHIPELAGO</h1>
          <p>
            Australia's leading carbon markets management platform
          </p>
        </div>
        <a
          className="grafana-button"
          href="http://localhost:3000/d/imGPdB14z/arichipelago?orgId=1"
          target="_blank"
          rel="noopener noreferrer"
        >
          Visit Dashboard
        </a>
      </header>
    </div>
  );
}

export default App;
