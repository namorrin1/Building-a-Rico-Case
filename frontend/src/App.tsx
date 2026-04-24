import { useEffect, useState } from 'react'
import { io } from 'socket.io-client'
import Button from '@mui/material/Button'
import ButtonGroup from '@mui/material/ButtonGroup'
import ArrowBackIcon from '@mui/icons-material/ArrowBack' 
import ArrowDownwardIcon from '@mui/icons-material/ArrowDownward'
import ArrowForwardIcon from '@mui/icons-material/ArrowForward'
import ArrowUpwardIcon from '@mui/icons-material/ArrowUpward'
import Box from '@mui/material/Box'
import TextField from '@mui/material/TextField'
import IconButton from '@mui/material/IconButton';
import Stack from '@mui/material/Stack';
import DeleteIcon from '@mui/icons-material/Delete';
import AlarmIcon from '@mui/icons-material/Alarm';
import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';
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
            <ButtonGroup variant="contained" aria-label="Basic button group">
                <Button><ArrowBackIcon></ArrowBackIcon></Button>
                <Button><ArrowDownwardIcon></ArrowDownwardIcon></Button>
                <Button><ArrowForwardIcon></ArrowForwardIcon></Button>
                <Button><ArrowUpwardIcon></ArrowUpwardIcon></Button>
                </ButtonGroup>
        </div>
        <div id="roombabutton"> 
            <Button>Roomba</Button>
        </div>
        <div id="songbuttons">
            <Button>Mary Had A Little Lamb</Button>
            <Button>Twinkle Twinkle Little Star</Button>
            <Button>Oh When The Saints Come Marching In</Button> 
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
