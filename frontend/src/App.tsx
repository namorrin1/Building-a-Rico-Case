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
const socket = io(URL, {
      path: '/socket.io/',
      transports: ['websocket'],
    })

function App() {
    const [connected, setConnected] = useState(false)
    const [on , setOn] = useState(false)
    const [drawSize, setDrawSize] = useState(100)
    const [message, setMessage] = useState('')
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
    const keydown = (e: KeyboardEvent) => {
        if(!on) return
        let direction = ''; 
        if(e.key === 'w') direction = 'forward';
        else if (e.key === 's')
            direction = 'backward';
        else if (e.key === 'a')
            direction = 'left';
        else if (e.key === 'd')
            direction = 'right';
        if (direction) {
            socket.emit('move', {direction});
        }
    }; 
    const keyup = () => {
        if (!on) return 
        socket.emit('move', {direction: 'stop'});
    }; 
    window.addEventListener('keydown', keydown);
    window.addEventListener('keyup', keyup);

    return () => {
        window.removeEventListener('keydown', keydown);
        window.removeEventListener('keyup', keyup);
    }; 
    }, [on])
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
       {/* wrapping buttons in this flex div */}
        <div style ={{ display: 'flex', gap: '16px', padding: PADDING, justifyContent: 'center' }}> 
            <Button
                variant ='outlined'
                sx ={{
                    backgroundColor: '#7ce4be',
                    color: '#ffffff',
                    '&:hover': {backgroundColor: '#3ada9f', border: '1px solid black' },
                    width: '150px',
                    height: '50px',
                    fontSize: '16px',
                    border: '1px solid #3ada9f',
                    
                
                }}
                onClick={() => {
                    if (on) {
                        socket.emit('move', {direction: 'stop'})
                    }
                    setOn(!on)
                }}
            >
                Move
            </Button>
        
            <Button
                sx={{
                    backgroundColor: '#7ce4be',
                    color: '#ffffff',
                    '&:hover': {backgroundColor: '#3ada9f' },
                    width: '150px',
                    height: '50px',
                    fontSize: '16px',
                }}
                onClick={() => 
                    socket.emit('roomba')
                }>
                Roomba
            </Button>
        </div>
        {/*wrapping songbuttons like the other two */}
        <div id="songbuttons" style={{display: 'flex', gap: '16px', padding: PADDING, justifyContent:'center'}}>
            <Button
                sx={{
                    backgroundColor: '#7ce4be',
                    color: 'white',
                    '&:hover': {backgroundColor: '#3ada9f' },
                    width: '180px',
                    height: '70px',
                    fontSize: '12px',
                }}
                onClick={() => 
                    socket.emit('songhandler','mary')
                }
            >Mary Had A Little Lamb</Button>
            <Button 
                sx={{
                    backgroundColor: '#7ce4be',
                    color: '#ffffff',
                    '&:hover': {backgroundColor: '#3ada9f' },
                    width: '180px',
                    height: '70px',
                    fontSize: '12px',
                }}
                onClick={() => 
                    socket.emit('songhandler','twinkle')
                }>Twinkle Twinkle Little Star</Button>
            <Button
            sx={{
                    backgroundColor: '#7ce4be',
                    color: '#ffffff',
                    '&:hover': {backgroundColor: '#3ada9f' },
                    width: '180px',
                    height: '70px',
                    fontSize: '12px',
                }}
                onClick={() => 
                    socket.emit('songhandler','saints')
                }
            >Oh When The Saints Come Marching In</Button> 
        </div>
        <div style= {{display: 'flex', gap:'16px',padding:PADDING, justifyContent: 'center'}}>
            <TextField
                label="Size"
                type="Number"
                value={drawSize}
                onChange={(e) => setDrawSize(Number(e.target.value))}
                sx={{width:'80px', 
                    
                    '& .MuiOutlinedInput-root': {
                        backgroundColor: '#7ce4be',
                        height: '50px',
                        alignItems: 'center',
                    },
                    '& .MuiInputLabel-root': {
                        color: '#ffffff',
                    },
                    '& .MuiOutlinedInput-input': {
                        color: '#ffffff',
                    },
                    '& .MuiOutlinedInput-notchedOutline': {
                        border: '1px solid #3ada9f'
                    },
                    '&:hover .MuiOutlinedInput-notchedOutline': {
                        border: '1px solid black'
                    },

                }}
            />
            <Button
                sx={{
                    backgroundColor: '#7ce4be',
                    color:'#ffffff',
                    '&:hover': {backgroundColor: '#3ada9f'},
                    width: '120px',
                    height: '50px',
                    fontSize: '12px',
                
                }}
                onClick={() => socket.emit('draw', drawSize, 'SQUARE')}
            >Square</Button>

            <Button
                sx={{
                    backgroundColor: '#7ce4be',
                    color:'#ffffff',
                    '&:hover': {backgroundColor: '#3ada9f'},
                    width: '120px',
                    height: '50px',
                    fontSize: '12px',
                
                }}
                onClick={() => socket.emit('draw', drawSize, 'HEXAGON')}
            >Hexagon</Button>

            <Button
                sx={{
                    backgroundColor: '#7ce4be',
                    color:'#ffffff',
                    '&:hover': {backgroundColor: '#3ada9f'},
                    width: '120px',
                    height: '50px',
                    fontSize: '12px',
                
                }}
                onClick={() => socket.emit('draw', drawSize, 'STAR')}
            >Star</Button>
        </div>
        <div style={{display: 'flex', gap: '16px', padding: PADDING, justifyContent: 'center', alignItems: 'center'}}>
            <TextField 
                label="Message"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                sx={{
                    width: '180px',
                    '& .MuiOutlinedInput-root': {backgroundColor: '#7ce4be', height: '70px'},
                    '& .MuiInputLabel-root': {color: '#ffffff'},
                    '& .MuiOutlinedInput-input': {color: '#ffffff'},

                }}
            />
            <Button
                sx={{
                    backgroundColor: '#7ce4be',
                    color: '#ffffff',
                    '&:hover':{ backgroundColor: '#3ada9f'},
                    width:'180px',
                    height: '70px',
                    fontSize: '14px',

                }}
                onClick={() => socket.emit('write', message)}
            >
                Print Message
            </Button>
        </div>
        </>
    )
}

export default App
