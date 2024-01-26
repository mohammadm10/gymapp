import { Select, MenuItem, FormControl, InputLabel, Button, TextField, IconButton } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import { useState, useEffect } from 'react';
import axios from 'axios';

export default function WorkoutPlan() {
    const [workoutName, setWorkoutName] = useState('');
    const [sets, setSets] = useState([{ exercise: '', sets: '', reps: '', info: [] }]);

    const handleAddSet = () => {
        setSets([...sets, { exercise: '', sets: '', reps: '', info: [] }]);
    };

    const handleDeleteSet = (index) => {
        const newSets = [...sets];
        newSets.splice(index, 1);
        setSets(newSets);
    };

    const handleInputChange = (index, field, value, weightIndex) => {
        const newSets = [...sets];

        if (field === 'sets') {
            newSets[index][field] = value;
            newSets[index].info = Array.from({ length: parseInt(value) }, () => ({ reps: '', weight: '' }));
        } else if (field === 'reps' || field === 'weight') {
            newSets[index].info[weightIndex][field] = value;
        } else {
            newSets[index][field] = value;
        }

        setSets(newSets);
    };

    const submitPlan = async () => {
        try {
            const formattedSets = sets.map(({ exercise, sets, reps, info }) => ({
                exercise,
                sets,
                reps,
                info,
            }));
            const res = await axios.post('http://127.0.0.1:8000/workout_plan/', {
                workoutName,
                sets: formattedSets,
            });
            if (res.status === 200) {
                console.log('Successfully sent user data to backend');
            } else {
                console.log(res);
                console.log('Error signing up');
            }
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <>
            <main id="home">
                <section className="min-h-screen">
                    <div>
                        {/* Input for Workout Name */}
                        <TextField
                            id="workout_name"
                            label="Workout Name"
                            variant="outlined"
                            placeholder="Ex: Push"
                            onChange={(e) => setWorkoutName(e.target.value)}
                        />
                    </div>
                    {sets.map((set, index) => (
                        <div key={index} style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                            {/* Input for Exercise */}
                            <TextField
                                id={`exercise-${index}`}
                                label="Exercise"
                                variant="outlined"
                                placeholder="Ex: Bench Press"
                                value={set.exercise}
                                onChange={(e) => handleInputChange(index, 'exercise', e.target.value)}
                            />
                            {/* Input for Sets */}
                            <TextField
                                id={`sets-${index}`}
                                label="Sets"
                                variant="outlined"
                                inputProps={{ type: 'number' }}
                                value={set.sets}
                                onChange={(e) => handleInputChange(index, 'sets', e.target.value)}
                            />
                            {/* Inputs for Reps and info */}
                            {set.info.map((weight, weightIndex) => (
                                <div key={`${index}-${weightIndex}`} style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    {/* Input for Reps */}
                                    <TextField
                                        id={`reps-${index}-${weightIndex}`}
                                        label={`Reps - Set ${weightIndex + 1}`}
                                        variant="outlined"
                                        inputProps={{ type: 'number' }}
                                        value={weight.reps}
                                        onChange={(e) => handleInputChange(index, 'reps', e.target.value, weightIndex)}
                                    />

                                    {/* Input for Weight */}
                                    <TextField
                                        id={`weight-${index}-${weightIndex}`}
                                        label={`Weight - Set ${weightIndex + 1}`}
                                        variant="outlined"
                                        inputProps={{ type: 'number' }}
                                        value={weight.weight}
                                        onChange={(e) => handleInputChange(index, 'weight', e.target.value, weightIndex)}
                                    />

                                </div>
                            ))}
                            {/* Button to delete a set */}
                            <IconButton onClick={() => handleDeleteSet(index)} color="secondary">
                                <DeleteIcon />
                            </IconButton>
                        </div>
                    ))}
                    {/* Button to add a new set */}
                    <Button onClick={handleAddSet} variant="contained" color="primary">
                        +
                    </Button>
                    <div>
                        <Button
                            onClick={submitPlan}
                            style={{
                                borderRadius: 5,
                                padding: '10px 30px',
                                fontSize: '12px',
                                backgroundColor: '#F64C72',
                                color: '#FFF',
                            }}
                        >
                            Submit
                        </Button>
                    </div>
                </section>
            </main>
        </>
    );
}
