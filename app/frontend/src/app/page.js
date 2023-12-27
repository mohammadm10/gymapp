import Image from 'next/image'

// Example Axios request in Next.js
import axios from 'axios';

const fetchData = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/test/');
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export default fetchData;


// export default function Home() {
//   return (
//     <main className="flex min-h-screen flex-col items-center justify-between p-24">
//       <p className=' text-xl'>Hello world!</p>
//     </main>
//   )
// }
