# Steganography-Project
Steganography is the practice of concealing a secret message behind 
a normal message. It stems from two Greek words, which 
are steganos, means covered and graphia, means writing. Steganography is 
an ancient practice, being practiced in various forms for thousands of years 
to keep communications private<br />
It is the method of hiding secret data in any image/audio/video. In a 
nutshell, the main motive of steganography is to hide the intended 
information within any image/audio/video that doesn’t appear to be secret 
just by looking at it.<br />
The purpose of steganography is to conceal and deceive. It is a form 
of covert communication and can involve the use of any medium to hide 
messages. It’s not a form of cryptography, because it doesn’t involve 
scrambling data or using a key. Instead, it is a form of data hiding and can 
be executed in clever ways. Where cryptography is a science that largely 
enables privacy, steganography is a practice that enables secrecy – and 
deceit.<br />

## Algorithm for encryption
1. Load the image and write the text in the text box provided.
2. Convert the message into an array representation of the ascii letters.
3. Compute the number of pixels required, which is equal to the 3 times 
the length of the array of ascii letters
4. Number of rows required = number of pixels required / width of the 
image
5. Traversing the image row-wise, we will check for the following 
conditions:
1. Check the number of pixels traversed. If the bit is 1 and the pixel value is 
an even number, make it an odd number by subtracting 1. Similarly, if 
the bit is 0 and the pixel value is an odd number, make it an even 
number by subtracting 1.
2. Keep a count of the number of letters using the count variable.
3. If the index is 7, check if the next character exists. If yes, mark the eof bit 
as 0 and continue. Else, mark as 1 and end.
6. We have successfully encrypted the image into the file.

## Algorithm for Decryption
1. Open the encrypted image and convert it into a NumPy array.
2. Obtain the data from the image by going through the encryption 
algorithm.
3. Every pixel in every row has 1 bit of information, which is added into 
the data variable, using the for loop.
A. Check if the eof character is reached.
I. If yes break from the for loop
II. Otherwise, continue.
B. The ascii is stored serially in the data variable.
4. After obtaining the ascii bits, bits are grouped into letters by making 
groups of 8.
5. The letters are stored in the message variable, which is linked using 
the join command in python.
6. Finally, the proper message is shown on the screen.

## Encryption Message
![plot](https://github.com/dawarepramod4/Steganography-Project/blob/master/Screenshot%202022-04-12%20162836.png)

## Decryption Message
![plot](https://github.com/dawarepramod4/Steganography-Project/blob/master/Screenshot%202022-04-12%20162939.png)
