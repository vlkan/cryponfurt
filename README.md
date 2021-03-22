## What is the cryponfurt?
cryponfurt is a string(text) encryption program. You can encrypt and decrypt encrypted messages.

## How it works?
This software was created using PI numbers. For example;

 - Let us use the word "mkemal" as an example.
 - if we break this word into pieces; ['m', 'k', 'e', 'm', 'a', 'l']
 - Now let's examine the PI number in a fragmented way; 3,1,4,1,5,9
 - Now I have to convert the word "mkemal" to ASCII standards; [109, 107, 101, 109, 97, 108]
 - In short, I converted the text I have into numbers. Click [here](https://www.asciitable.com/) for the ASCII table.
 - I will add PI numbers to the word I convert to numbers.
 - ['m+3', 'k+1', 'e+4', 'm+1', 'a+5', 'l+9'] or [109+3, 107+1, 101+4, 109+1, 97+5, 108+9]
 - New version; [112, 108, 105, 110, 102, 117]
 - Now let's convert these ASCII numbers back to letters; "plinfu"
 - Done.

## How Can I Use It?

 **1. Add project:** If you want to add it to your project, you must copy it to your project directory (cust "cryponfurt.py") and in which program you want to use "import cryponfurt" you need to add the code.

    import cryponfurt
    cryponfurt.encrypt("mkemal") ##for encrypt
    cryponfurt.decrypt("plinfu") ##for decrypt

 **2.Terminal:** If you try this program you must download all files and start the terminal in the directory where the project is located.
 

    python main.py
    Press for Encrypt(1) or Decrypt(2) QUIT(Q or q)
    What is your process?

Should seems this like that. Choose and give a text.


## Advantages Disadvantages
**Advantages**
 - Even if the letter you use is the same, it cannot be detected when encrypted. Lets look at example;
	 -  Let us use the word "aaaaa" as an example.
	 -  Now I have to convert the word "aaaaa" to ASCII standards; [97, 97, 97, 97, 97, 97]
	 -  I will add PI numbers to the word I convert to numbers.
	 - ['a+3', 'a+1', 'a+4', 'a+1', 'a+5', 'a+9'] or [97+3, 97+1, 97+4, 97+1, 97+5, 97+9]
	 - New version; [100, 98, 101, 98, 102, 106]
	 - Now let's convert these ASCII numbers back to letters; "dbebfj"
	 - As you see, all numbers and encrypted letters different.

**Disadvantages**

 - Sometimes some of the letters may appear undefined when words are encrypted.
 - [Click](https://drive.google.com/open?id=1gc6TAdK_d7zGNLFbTRn7vx-cuZgh_9I2) to see the error I mentioned.
 
 
 //09.09.2019
	
	
