import { createHash } from 'crypto';

export default function shaHash (inputString){


    // Create a hash object using the SHA-256 algorithm
    const hash = createHash('sha256');
    
    // Update the hash object with the input string
    hash.update(inputString);
    
    // Retrieve the hash in hexadecimal encoding
    const hashedString = hash.digest('hex');
    
    return hashedString;

}