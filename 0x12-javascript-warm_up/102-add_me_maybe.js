#!/usr/bin/node

module.exports = {
  addMeMaybe: function (number, theFunction) {
    const incrementedNumber = number + 1;
    theFunction(incrementedNumber);
  }
};
