# Included in this repo is the screenshot of turtlebot3 simulation and instructions to run  using the burger model 

###  Turtlebot3 Can Be Installed In These Simple Steps
 Go To The Src Folder Of The Ros Workspace And 
 
| $ git clone https://github.com/ROBOTIS-GIT/turtlebot3.git  |
| ------------ |
| to download the source files  |




then '$ cd ..' to go back to workspace home and execute

`Catkin_make
`

then go back to SRC folder and download the simulation files using



    $ git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
    cd ..
    Catkin_make
    

##### now to run the simulation 

do not forget to `source  devel/setup.bash`

then excute



    $ roslaunch turtlebot3_fake turtlebot3_fake.launch ##This launches Rviz to start simulation
    $ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch ## this lauches the control to move the Robot 

Done now you can enjoy your Turtlebot3 Simulation 
[![Simulation](https://raw.githubusercontent.com/malikib97/Artificial-Intelligence-Robot/master/Turtlebot3%20Simulation/Screenshot%20from%202020-07-04%2015-39-30.png "Simulation")](http://https://raw.githubusercontent.com/malikib97/Artificial-Intelligence-Robot/master/Turtlebot3%20Simulation/Screenshot%20from%202020-07-04%2015-39-30.png "Simulation")
*Written by Malik Ibrahim *

