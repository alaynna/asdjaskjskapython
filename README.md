# Little Python Demo for Quest

This one is a very simple python demo, which listen to a TCP port and play back the data from file on fixed interval 
to new connection.
The data package started with && and ended with !!, each line is seprate by newline character '\n'
For example in demo data file (a.wits)
&&
abcd
1234
!!
zzzz
zzzz
!!
&&
efgh
6789
!!

The output should be 
&&
abcd
1234
!!
&&
efgh
6789
!!

It is because 
!!
zzzz
zzzz
!!

did not started with &&

Note:
In the real world application for better handling IO performance, it should implement by using IO selector.
In addition it's also a much better way to spawn a new thread on every new connection, Thread pool or exector are two
of the possible alternative.
Lastly, to make it simple I did not do any error handling.

The program take 3 arguments 
python Witsplayer.py 7080  1 a.wits  
The first argument is binding port
The second argument is play back interval
The third argument is the play back file name.

