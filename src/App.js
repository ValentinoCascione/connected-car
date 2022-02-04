import './App.css';

function App() {
  // Create WebSocket connection.
  const socket = new WebSocket('ws://192.168.1.210:4040');
  console.log(socket);

  // Connection opened
  socket.addEventListener('open', function (event) {
      console.log('iciicici')
      socket.send('Yo')
      console.log('Connected to the WS Server!')
  });

  // Listen for messages
  socket.addEventListener('message', function (event) {
      console.log('Message from server ', event.data);
  });

  const sendForward = () => {
      socket.send('forward')
  }

  const sendReverse = () => {
      socket.send('reverse')
  }

  const sendTurnLeft = () => {
      socket.send('turnLeft')
  }

  const sendTurnRight = () => {
      socket.send('turnRight')
  }

  const stop = () => {
    socket.send('stop')
  }

  return (
    <div className="App">
      <button className='button' id="turnLeftButton" onTouchEnd={() => stop()} onTouchStart={() => sendTurnLeft()}>Left</button>
      <div id="ForwardReverseButtons">
        <button className='button' id="forwardButton" onTouchEnd={() => stop()} onTouchStart={() => sendForward()}>Forward</button>
        <button className='button' id="reverseButon" onTouchEnd={() => stop()} onTouchStart={() => sendReverse()}>Reverse</button>
      </div>
      <button className='button' id="turnRightButton" onTouchEnd={() => stop()} onTouchStart={() => sendTurnRight()}>Right</button>
    </div>
  );
}

export default App;
