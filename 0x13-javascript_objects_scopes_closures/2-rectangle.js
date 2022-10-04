#!/usr/bin/node
module.exports = class Rectangle {
  // class Rectangle
  constructor (w, h) {
    // initializing the width and height attribute
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
