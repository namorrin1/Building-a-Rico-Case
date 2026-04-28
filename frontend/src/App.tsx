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
const BUTTONCOLOR = '#7ce4be'

const BUTTONOUTLINE = '#3ada9f'
const socket = io(URL, {
      path: '/socket.io/',
      transports: ['websocket'],
    })


function App() {
    const [connected, setConnected] = useState(false)
    const [on , setOn] = useState(false)
    const [drawSize, setDrawSize] = useState(10)
    const [message, setMessage] = useState('')
    const [roombaOn, setRoombaOn] = useState(false)
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
        <div style={{
            backgroundColor: BUTTONCOLOR,
            borderBottom: '2px solid ${BUTTONOUTLINE}',
            padding: '16px',
            width: '100%',
            boxSizing: 'border-box',
        }}>
            <h1 style={{textAlign: 'center', color: '#ffffff' }}>RICO</h1>
        </div>
        {/*<div style={{ padding: PADDING }} >
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
        </div> */}
       {/* wrapping buttons in this flex div */}
        <div style ={{ display: 'flex', gap: '16px', padding: PADDING, justifyContent: 'center' }}> 
            <Button
                variant ='outlined'
                sx ={{
                    backgroundColor: BUTTONCOLOR,
                    color: '#ffffff',
                    '&:hover': {backgroundColor: BUTTONOUTLINE, border: '1px solid black' },
                    width: '150px',
                    height: '50px',
                    fontSize: '16px',
                    border: '1px solid BUTTONOUTLINE',
                    
                
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
                variant='outlined'
                sx={{
                    backgroundColor: roombaOn ? BUTTONOUTLINE : BUTTONCOLOR,
                    color: '#ffffff',
                    '&:hover': {backgroundColor: BUTTONOUTLINE, border: '1px solid black' },
                    width: '150px',
                    height: '50px',
                    fontSize: '16px',
                    border: '1px solid BUTTONOUTLINE',
                }}
                onClick={() => {
                    socket.emit('roomba')
                    setRoombaOn(!roombaOn)
                }}
            >
                {roombaOn ? 'Stop Roomba' : 'Roomba'}
            </Button>
        </div>
        {/*wrapping songbuttons like the other two */}
        <div id="songbuttons" style={{display: 'flex', gap: '16px', padding: PADDING, justifyContent:'center'}}>
            <Button
                variant='outlined'
                sx={{
                    backgroundColor: BUTTONCOLOR,
                    color: 'white',
                    '&:hover': {backgroundColor: BUTTONOUTLINE, border: '1px solid black'},
                    width: '180px',
                    height: '70px',
                    fontSize: '12px',
                }}
                onClick={() => 
                    socket.emit('songhandler','mary')
                }
            >Mary Had A Little Lamb</Button>
            <Button 
                variant='outlined'
                sx={{
                    backgroundColor: BUTTONCOLOR,
                    color: '#ffffff',
                    '&:hover': {backgroundColor: BUTTONOUTLINE, border: '1px solid black',  },
                    width: '180px',
                    height: '70px',
                    fontSize: '12px',
                }}
                onClick={() => 
                    socket.emit('songhandler','twinkle')
                }>Twinkle Twinkle Little Star</Button>
            <Button
                variant='outlined'
                sx={{
                    backgroundColor: BUTTONCOLOR,
                    color: '#ffffff',
                    '&:hover': {backgroundColor: BUTTONOUTLINE, border: '1 px solid black' },
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
                        backgroundColor: BUTTONCOLOR,
                        height: '50px',
                        alignItems: 'center',
                        '&:hover': {
                            backgroundColor: BUTTONOUTLINE,
                        }
                    },
                    '& .MuiInputLabel-root': {
                        color: '#ffffff',
                    },
                    '& .MuiOutlinedInput-input': {
                        color: '#ffffff',
                    },
                    '& .MuiOutlinedInput-notchedOutline': {
                        border: '1px solid ${BUTTONOUTLINE}'
                    },
                    '&:hover .MuiOutlinedInput-notchedOutline': {
                
                        border: '1px solid black'
                    },

                }}
            />
            <Button
                variant='outlined'
                sx={{
                    backgroundColor: BUTTONCOLOR
                    ,
                    color:'#ffffff',
                    '&:hover': {backgroundColor: BUTTONOUTLINE, border: '1px solid black'},
                    width: '120px',
                    height: '50px',
                    fontSize: '12px',
                
                }}
                onClick={() => socket.emit('draw', drawSize, 'SQUARE')}
            >Square</Button>

            <Button
                variant='outlined'
                sx={{
                    backgroundColor: BUTTONCOLOR
                    ,
                    color:'#ffffff',
                    '&:hover': {backgroundColor: BUTTONOUTLINE, border: '1px solid black'},
                    width: '120px',
                    height: '50px',
                    fontSize: '12px',
                
                }}
                onClick={() => socket.emit('draw', drawSize, 'HEXAGON')}
            >Hexagon</Button>

            <Button
                variant='outlined'
                sx={{
                    backgroundColor: BUTTONCOLOR
                    ,
                    color:'#ffffff',
                    '&:hover': {backgroundColor: BUTTONOUTLINE, border: '1px solid black'},
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
                    '& .MuiOutlinedInput-root': {
                        backgroundColor: BUTTONCOLOR,
                        height: '70px'},
                        '&:hover': {
                            backgroundColor: BUTTONOUTLINE,
                        },
                    
                    '& .MuiInputLabel-root': {color: '#ffffff'},
                    '& .MuiOutlinedInput-input': {color: '#ffffff'},
                    '& .MuiOutlinedInput-notchedOutline': {
                        border: '1px solid ${BUTTONOUTLINE}',
                    },
                    
                    '&:hover .MuiOutlinedInput-notchedOutline': {
                        border: '1px solid black',
                    },
                    

                }}
            />
            <Button
            variant='outlined'
                sx={{
                    backgroundColor: BUTTONCOLOR
                    ,
                    color: '#ffffff',
                    '&:hover':{ backgroundColor: BUTTONOUTLINE, border: '1px solid black'},
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
