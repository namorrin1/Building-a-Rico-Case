import { useState } from 'react'
import './App.css'

function App() {
    const [status, setStatus] = useState('Waiting')

    const connect = async (url: String) : Promise<any> => {
        setStatus('Sending request to endpoint...')
        try {
            const response = await fetch(`/${url}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
            const data = await response.json()
            if (data.status === 'success') {
                setStatus('Success: ' + data.output)
            } else {
                setStatus('Error: ' + data.message)
            }

        } catch (error: any) {
            setStatus('Network Error: ' + error.message);
        }
    }

  return (
    <div>
        <button onClick={() => { connect('first_finch_test') }}>
            <h2>Run Finch Test</h2>
        </button>
        <br/>
        {status}
        <br/>
    </div>
  )
}

export default App
