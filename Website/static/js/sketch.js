let windy;

// function getData(amount) {
//   var a;
//   switch (amount) {
//   case "15":
//     a = 15;
//     break;
//   case "30":
//     a = 30;
//     break;
//   case "45":
//     a = 45;
//     break;
//   case "60":
//     a = 60;
//     break;
//   default:
//     a = 15
//   }
// }

var a = 15;

function setup() {
  createCanvas(800, 400);
}

function draw() {
  background(0);
  stroke(255);
  windy = radians(a);
  translate(width/2,height);
  line(0,0,0,-130);
  translate(0,-130);
  branch(120);

}

function branch(h) {
    h *= 0.66;
  
    if (h > 2) {
      push();   
      rotate(windy);
      line(0, 0, 0, -h);
      translate(0, -h);
      branch(h);      
      pop();
  
      push();
      rotate(-windy);
      line(0, 0, 0, -h);
      translate(0, -h);
      branch(h);
      pop();
    }
  }

  function mousePressed() {
    if (a < 60) {
      a+=15;
    }
    else {
      a = 15;
    }
    redraw();
  }