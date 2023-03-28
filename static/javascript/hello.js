const{spawn}= require('child_process');
//const childPython= spawn('python',['--version']);
const childPython= spawn('python',['testing.py']);
childPython.stdout.on('data',(data)=>
{
    console.log(`stdout: ${data}`);
})
childPython.stderr.on('data',(data)=>
{
    console.log(`stdout: ${data}`);
})
childPython.on('close',(close)=>
{
    console.log(`childprocess exited with code: ${close}`);
})