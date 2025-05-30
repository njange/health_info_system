import React from 'react';
import HealthDataList from './HealthDataList';
import '../styles/App.css';

const App: React.FC = () => {
    return (
        <div className="App">
            <header className="header">
                <h1>Health Information System</h1>
            </header>
            <main className="container">
                <HealthDataList />
            </main>
        </div>
    );
};

export default App;