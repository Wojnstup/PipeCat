# PipeCat
A command line Youtube music player written in python. It's an app written for Linux. It also supports offline playlists that are stored in a playlists.db file. 

<h2>
FEATURES:
</h2>
  <li>private playlists stored on your device (no need for Google account)</li>
  <li>song queue</li>
  <li>creating shortcuts for YouTube playlists and channels</li>
  <li>video and audio playback</li>
  <li>mixes based on your playlists</li>
  <li>it can also run in Termux on Android devices to serve you music (audio only) on the go.</li>
  
<h3>Also check out: <a href="https://github.com/Wojnstup/PipeCatTurbo">PipeCatTurbo</a></h3>
<h2>
DEPENDENCIES:
</h2>
<ul>
  <li>pip3 install youtube-dl youtube-search-python pyfiglet</li>
  <li>mpv has to be installed - check your distro's install method</li>
  <li>python3</li>
  <li>an audio server</li>
  <li>a kernel</li>
</ul>
<h3>
  You can install all the pip3 requirements by running 'pip3 install -r requirements.txt'  
</h3>


After launching main.py in your terminal, type in 'man' to print a manual on how to use the program.

You can replace main.py with your own script - maybe you want a GUI, or keyboard shortcuts from anywhare using the keyboard library? I made the program modular so if you throw away main.py you discard only the input method.
