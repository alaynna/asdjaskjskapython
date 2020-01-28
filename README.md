# Little Python Demo Patrick Tsang

This one is a very simple python demo, which listen to a TCP port and play back the data from file on fixed interval 
to new connection.<br>
The data package started with && and ended with !!, each line is seprate by newline character '\n'
For example in demo data file (a.wits)<br>
&&<br>
abcd<br>
1234<br>
!!<br>
zzzz<br>
zzzz<br>
!!<br>
&&<br>
efgh<br>
6789<br>
!!<br>
<br>
The output should be<br> 
&&<br>
abcd<br>
1234<br>
!!<br>
&&<br>
efgh<br>
6789<br>
!!<br>
<br>
It is because <br>
!!<br>
zzzz<br>
zzzz<br>
!!<br>
<br>
did not started with &&<br>
<br>
Note:<br>
In the real world application for better handling IO performance, it should implement by using IO selector.<br>
In addition it's also a much better way to spawn a new thread on every new connection, Thread pool or exector are two<br>
of the possible alternative.<br>
Lastly, to make it simple I did not do any error handling.<br>
<br>
The program take 3 arguments <br>
python Witsplayer.py 7080  1 a.wits  <br>
The first argument is binding port<br>
The second argument is play back interval<br>
The third argument is the play back file name.<br>

