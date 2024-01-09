import { Button, TextField } from '@mui/material';
import axios from 'axios';
import { useState } from 'react';
import shaHash from './utils/shaHash';
import PasswordStrengthBar from 'react-password-strength-bar';

export default function Home() {

    const [username, setUsername] = useState('');
    const [firstName, setfirstName] = useState('');
    const [lastName, setlastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [passwordMatch, setPasswordMatch] = useState('');
    const [passwordError, setPasswordError] = useState('')
    const [passwordScore, setPasswordScore] = useState(0)
    const [errorMessages, setErrorMessages] = useState([]);

    const validateForm = () => {
        const errors = [];
        // Validate fields
        if (![username, email, firstName, lastName, password, confirmPassword].every(field => field.trim() !== '')) {
            errors.push('All fields are required');
        }

        // Validate email
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            errors.push('Invalid email address');
        }

        // Validate password
        if (password.length < 8) {
            errors.push('Password must be at least 8 characters');
        }

        // Validate password match
        if (password !== confirmPassword) {
            errors.push('Passwords do not match');
        }

        if (passwordScore < 3) {
            errors.push('Password too weak')
        }

        setErrorMessages(errors);

        return errors.length === 0;
    };

    const logIn = async () => {
        if (validateForm()) {
            const hashedPassword = shaHash(password); // Encode plaintext to sha-256 prior to sending to backend
            try {
                const res = await axios.post('http://127.0.0.1:8000/signUp/', {
                    username,
                    firstName,
                    lastName,
                    email,
                    hashedPassword,
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
        } else {
            console.log(errorMessages);
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
                    <TextField id="firstName" label="FirstName" variant="outlined" onChange={(e) => setfirstName(e.target.value)} />
                    <TextField id="lastName" label="LastName" variant="outlined" onChange={(e) => setlastName(e.target.value)} />
                    <TextField id="username" label="Username" variant="outlined" onChange={(e) => setUsername(e.target.value)} />
                    <TextField id="email" label="Email" variant="outlined" onChange={(e) => setEmail(e.target.value)} />
                    <TextField id="password" label="Password" variant="outlined" type="password" onChange={(e) => setPassword(e.target.value)} />
                    <PasswordStrengthBar password={password} onChangeScore={(score) => setPasswordScore(score)} />
                    <TextField id="confrimPassword" label="Confirm Password" variant="outlined" type="password" onChange={(e) => setConfirmPassword(e.target.value)} />
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
