import { Button, TextField } from '@mui/material';
import axios from 'axios';
import { useState } from 'react';

// const fetchData = async () => {
//   try {
//     const response = await axios.get('http://127.0.0.1:8000/test/');
//     return response.data;
//   } catch (error) {
//     console.error('Error fetching data:', error);
//     throw error;
//   }
// };

// export default fetchData;
export default function Home() {

const [username, setUserName] = useState('');
const [password, setPassword] = useState('');

const logIn = async () => {
  try {
    const res = await axios.post('http://127.0.0.1:8000/test/', {
      username,
      password,
    });
    if (res.status === 200) {
      console.log('Successfully sent username and password to backend');
    } else {
      console.log('Error logging in');
    }
  } catch (error) {
    console.log(error);
  }
}


  return (
    // <main className="grid grid-cols-12 min-h-screen">
    //   <div className="col-span-2 bg-gray-300">Column 1</div>
    //   <div className="col-span-8 bg-gray-400">Column 2</div>
    //   <div className="col-span-2 bg-gray-500">Column 3</div>
    // </main>
    <>
      <main id='home'>
        <section className='min-h-screen'>
          <TextField id="username" label="Username" variant="outlined" onChange={(e) => setUserName(e.target.value)} />
          <TextField id="password" label="Password" variant="outlined" type="password" onChange={(e) => setPassword(e.target.value)} />
          <Button onClick={logIn}
            style={{
              borderRadius: 5,
              padding: "10px 30px",
              fontSize: "12px",
              backgroundColor: "#F64C72",
              color: "#FFF"
            }}
          >
            Log In
          </Button>
        </section>
      </main>
    </>
  );
}
