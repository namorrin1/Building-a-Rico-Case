import { useEffect, useState } from 'react'
import { io } from 'socket.io-client'
import Button from '@mui/material/Button'
import Box from '@mui/material/Box'
import TextField from '@mui/material/TextField'
import './App.css'

//const TOTALLY_SECURE_KEY: string = 'meow'
const PORT: number = 5555
const URL: string = 'http://localhost:' + String(PORT)
const PADDING: string = '25px'

function App() {

    const socket = io(URL, {
      path: '/socket.io/',
      transports: ['websocket'],
    })

    const [connected, setConnected] = useState(false)
    useEffect(() => {

    function onConnect() {
        setConnected(true)
        console.log('connected!')
    }

    function onDisconnect() {
        setConnected(false)
        console.log('disconnected!')
    }

    socket.on('connect', onConnect)
    socket.on('disconnect', onDisconnect)
    socket.on('error', (err) => {
        console.log(err)
    })
    })
    return (
        <>
        <div style={{ padding: PADDING }} >
            <Button
                variant='contained'
                color = { connected ? 'success' : 'error' }
                onClick={() => {
                    socket.emit('finch_test')
                }}
            >
                <h2>Run Finch Test</h2>
            </Button>
            <div style={{padding: PADDING}} >
            { connected ? 'connected' : 'not connected' }
            </div>
        </div>
        <div> 
            <Button 
                onClick={() => 
                    socket.emit('move')
            }>
                Move
            </Button>
        </div>
        <div id="roombabutton"> 
            <Button
                onClick={() => 
                    socket.emit('roomba')
                }>
                Roomba</Button>
        </div>
        <div id="songbuttons">
            <Button
                onClick={() => 
                    socket.emit('songhandler','mary')
                }
            >Mary Had A Little Lamb</Button>
            <Button 
                onClick={() => 
                    socket.emit('songhandler','twinkle')
                }>Twinkle Twinkle Little Star</Button>
            <Button
                onClick={() => 
                    socket.emit('songhandler','saints')
                }
            >Oh When The Saints Come Marching In</Button> 
        </div>
        <div id="message"> 
                <Box
      component="form"
      sx={{ '& > :not(style)': { m: 1, width: '25ch' } }}
      noValidate
      autoComplete="off"
    >
      <TextField id="outlined-basic" label="Outlined" variant="outlined" />
      <TextField id="filled-basic" label="Filled" variant="filled" />
      <TextField id="standard-basic" label="Standard" variant="standard" />
    </Box>
        </div>
        </>
    )
}

export default App
