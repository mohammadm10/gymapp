import { Button, TextField } from '@mui/material';
import axios from 'axios';
import { useState } from 'react';

export default function WeightTracker() {

    const [weight, setWeight] = useState(0);

    const addWeight = async () => {
        try {
          const res = await axios.post('http://127.0.0.1:8000/addWeight/', {
            weight,
          });
          if (res.status === 200) {
            console.log('Successfully sent weight to backend');
          } else {
            console.log('Error sending weight data to backend');
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
                    <TextField id="weight" label="Weight (lb)" variant="outlined" onChange={(e) => setWeight(e.target.value)} />
                    <Button onClick={addWeight}
                        style={{
                            borderRadius: 5,
                            padding: "10px 30px",
                            fontSize: "12px",
                            backgroundColor: "#F64C72",
                            color: "#FFF"
                        }}
                    >
                        Enter
                    </Button>
                </section>
            </main>
        </>
    );
}
