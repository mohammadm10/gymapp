import { Button, TextField } from '@mui/material';
import axios from 'axios';
import { useState } from 'react';

export default function RepCalculator () {

    const [weight, setWeight] = useState(0)
    const [reps, setReps] = useState(0)

    const calculateMax = async () => {
        try {
          const res = await axios.post('http://127.0.0.1:8000/rep_max_calculator/', {
            weight,
            reps,
          });
          if (res.status === 200) {
            const oneRepMax = res.data.one_rep_max;
            const fiveByFive = res.data.five_by_five;
            const hypoLow = res.data.hypertrophy_low;
            const hypoHigh = res.data.hypertrophy_high;
            console.log('1 rep calculation result:', oneRepMax);
            console.log('5x5 calculation result:', fiveByFive);
            console.log('Hypertrophy low side result:', hypoLow);
            console.log('Hypertrophy high side result:', hypoHigh);
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
                    <TextField id="reps" label="Repititions" variant="outlined" onChange={(e) => setReps(e.target.value)} />
                    <Button onClick={calculateMax}
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
    )
}