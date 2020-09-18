const util = require('util');

const inputs = [
  'THIS + IS + HIS == CLAIM',
  'WHAT + WAS + THY == CAUSE',
  'HIS + HORSE + IS == SLAIN',
  'HERE + SHE == COMES',
  'FOR + LACK + OF == TREAD',
  'I + WILL + PAY + THE == THEFT',
  'SEND + MORE == MONEY'
];

var tokenize = function(input) {
  
  const parts = input.split(/[\+\= ]/).filter(part => part !== '');

  
  let tokens = {};
  parts.forEach(part => {
    for (let i=0; i<part.length; i++) {
      const token = part[i];

      tokens[token] = { value: i === 0 ? 1 : (tokens[token] ? tokens[token].value : 0), first: tokens[token] && tokens[token].first || i === 0 };
    }
  });

  return { parts: parts, tokens: tokens };
}

var encode = function(parts, tokens) {
  
  let equation = [];

  for (let i=0; i<parts.length; i++) {
    const part = parts[i];
    let number = '';

    for (let j=0; j<part.length; j++) {
      const ch = part[j];
      const value = tokens[ch].value;

      number += value;
    }

    equation.push(parseInt(number));
  }

  return equation;
}

var complete = function(equation) {
  
  let sum = 0;

  for (let i=0; i<equation.length - 1; i++) {
    sum += equation[i];
  }

  return { sum: sum, target: equation[equation.length - 1], success: (sum === equation[equation.length - 1]) };
}

var random = function(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

var solve = function(input, tokens, verbose) {
  let count = 0;
  var fringe = [ tokens ];
  let result = null;

  while (fringe.length) {
    // Get the next state.
    const values = fringe.shift();

    // Encode the equation with values from the state.
    const equation = encode(input, values)
    const balance = complete(equation);

    if (verbose && ++count % 100000 === 0) {
      count = 0;
      console.log(equation);
      console.log(result);
    }

    if (balance.success) {
      // Solution found!
      result = { values: values, equation: equation, balance: balance };
      break;
    }
    else {
      // Add child states. A child state will be 
      let child = {};
      const keys = Object.keys(values);
      for (let i=0; i<keys.length; i++) {
        const key = keys[i];
        const first = values[key].first;
        let r = random(10);
        r = first && !r ? 1 : r; // No leading zeroes.

        child[key] = { value: r, first: first };
      }

      fringe.push(child);
    }
  }

  return result;
}

inputs.forEach(input => {
  const data = tokenize(input);

  console.log(data.parts);

  const result = solve(data.parts, data.tokens);

  console.log('*** Solution ***');
  console.log(util.inspect(result, true, 10));
  console.log('');
});