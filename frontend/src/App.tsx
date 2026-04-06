import { useState } from 'react';
import { io } from 'socket.io-client';
import './App.css';

//const TOTALLY_SECURE_KEY: string = 'meow';
const PORT: number = 5555;
const URL: string = 'http://localhost:' + String(PORT);

function App() {

    const socket = io(URL, {
      path: '/socket.io/',
      transports: ['websocket'],
    });

    const [connected, setConnected] = useState(false);

    function onConnect() {
        setConnected(true);
        console.log('connected!')
    }

    function onDisconnect() {
        setConnected(false);
        console.log('disconnected!')
    }

    socket.on('connect', onConnect);
    socket.on('disconnect', onDisconnect);
    socket.on('error', (err) => {
        console.log(err)
    })

    return (
        <div>
            <button
                style={{
                    backgroundColor: connected ? 'green' : 'red'
                }}
                onClick={() => {
                    socket.emit('finch_test');
                }}
            >
                <h2>Run Finch Test</h2>
            </button>
            <br />
            { connected ? 'connected' : 'not connected' }
            <br />
        </div>
    );
}

export default App;
