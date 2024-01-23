import { Select, MenuItem, FormControl, InputLabel, Button, TextField } from '@mui/material';
import axios from 'axios';
import { useState } from 'react';

export default function RepCalculator() {

    const muscle = ['Chest', 'Back', 'Shoulders', 'Legs', 'Biceps', 'Triceps'];
    const level = ['Beginner', 'Intermediate', 'Advanced'];
    const goals = ['Weightloss', 'Maintain', 'Build Muscle'];

    const [muscleSelect, setMuscleSelect] = useState('');
    const [levelSelect, setLevelSelect] = useState('');
    const [goalSelect, setGoalSelect] = useState('');
    const [APINotes, setAPINotes] = useState('')

    const createWorkoutAPI = async () => {
        try {
          const res = await axios.post('http://127.0.0.1:8000/workout_creator/', {
            muscleSelect,
            levelSelect,
            goalSelect,
            APINotes
          });
          if (res.status === 200) {
            console.log(res.data.result);
          } else {
            console.log('Error sending weight data to backend');
          }
        } catch (error) {
          console.log(error);
        }
      }

    const handleMuscleSelect = (event) => {
        setMuscleSelect(event.target.value);
    }

    const handleExperienceSelect = (event) => {
        setLevelSelect(event.target.value);
    }

    const handleGoalChange = (event) => {
        setGoalSelect(event.target.value);
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
                    <FormControl sx={{ m: 1, minWidth: 160, width: '100%' }}>
                        <InputLabel id="muscle-label">Muscle</InputLabel>
                        <Select
                            labelId="muscle-label"
                            label="Muscle"
                            value={muscleSelect}
                            onChange={handleMuscleSelect}
                            MenuProps={{
                                PaperProps: {
                                    style: {
                                        maxHeight: 190, // Set the maximum height for the dropdown menu
                                    },
                                },
                            }}
                        >
                            {muscle.map((muscleName, index) => (
                                <MenuItem key={index} value={muscleName}>{muscleName}</MenuItem>
                            ))}
                        </Select>
                    </FormControl>
                    <FormControl sx={{ m: 1, minWidth: 160, width: '100%' }}>
                        <InputLabel id="level-label">Gym Experience</InputLabel>
                        <Select
                            labelId="level-label"
                            label="Gym Experience"
                            value={levelSelect}
                            onChange={handleExperienceSelect}
                        >
                            {level.map((levelName, index) => (
                                <MenuItem key={index} value={levelName}>{levelName}</MenuItem>
                            ))}
                        </Select>
                    </FormControl>
                    <FormControl sx={{ m: 1, minWidth: 160, width: '100%' }}>
                        <InputLabel id="goal-label">Gym Goal</InputLabel>
                        <Select
                            labelId="goal-label"
                            label="Gym Goal"
                            value={goalSelect}
                            onChange={handleGoalChange}
                        >
                            {goals.map((goalsName, index) => (
                                <MenuItem key={index} value={goalsName}>{goalsName}</MenuItem>
                            ))}
                        </Select>
                    </FormControl>
                    <TextField id="notes" label="Notes" placeholder='Ex: I want to use dumbells only.' variant="outlined" fullWidth={true} multiline={true} rows={4} onChange={(e) => setAPINotes(e.target.value)}/>
                    <div className=' py-7 flex justify-center'>
                        <Button onClick={createWorkoutAPI} variant="outlined">Create Exercise</Button>
                    </div>
                </section>
            </main>
        </>
    )
}