// #!/usr/bin/node
arg = process.argv;
if (typeof (arg) != 'number') {
    console.log('Not a number');
} else if (typeof(arg) == 'number') {
    console.log(Number(arg));
}