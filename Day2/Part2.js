'use strict';
const fs = require('fs');

var input_file = fs.readFileSync('./input.txt', (e, data) => {}).toString();
var input_arr = input_file.split('\n')

var hp = 0;
var depth = 0;
var aim = 0;
while(input_arr.length)
{
   var k = input_arr.shift().split(' ');
   k[1] = parseInt(k[1]);
    switch(k[0])
    {
        case "forward":
            hp += k[1];
            if (aim != 0){depth += k[1] * aim;}
            break;
        case "up":
            aim -= k[1]
            break;
        case "down":
            aim += k[1]
            break;
    }
}
console.log(hp*depth)
