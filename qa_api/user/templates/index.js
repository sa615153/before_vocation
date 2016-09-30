angular.module('myApp', [])
  .controller('stationController', ['$interval', function ($interval) {
    var LeanWorkflow = this;
    LeanWorkflow.stations =
      [
        { 'velocity': 1, 'product': 0, 'waiting': 0 },
        { 'velocity': 1, 'product': 0, 'waiting': 0 },
        { 'velocity': 0.5, 'product': 0, 'waiting': 0 },
        { 'velocity': 2, 'product': 0, 'waiting': 0 }
      ];
    LeanWorkflow.viewStations = LeanWorkflow.stations;
    LeanWorkflow.calcQueue = 0;

    LeanWorkflow.simTime = 0;
    LeanWorkflow.isStart = false;
    LeanWorkflow.isPush = true;
    LeanWorkflow.totalOut = 0;
    LeanWorkflow.newVelocity = 5;
    LeanWorkflow.deleteIndex = 0;
    LeanWorkflow.amount = 10;
    LeanWorkflow.firstCycle = 0;
    LeanWorkflow.totalTime = 0;
    LeanWorkflow.lastProductLeadTime = 0;

    LeanWorkflow.onStart = function () {
      LeanWorkflow.Timer = $interval(LeanWorkflow.timeUp, 1000);
      LeanWorkflow.isStart = true;
    }

    LeanWorkflow.onStop = function () {
      $interval.cancel(LeanWorkflow.Timer);
      LeanWorkflow.isStart = false;
    }

    LeanWorkflow.onReset = function () {
      LeanWorkflow.simTime = 0;
      for (var i = 0; i < LeanWorkflow.stations.length; i++) {
        LeanWorkflow.stations[i].product = 0;
        LeanWorkflow.stations[i].waiting = 0;
        LeanWorkflow.totalOut = 0;
        LeanWorkflow.firstCycle = 0;
      }
    }

    LeanWorkflow.onPush = function () {
      LeanWorkflow.stations[0].velocity = LeanWorkflow.stations[1].velocity;
      LeanWorkflow.isPush = true;
    }

    LeanWorkflow.onPull = function () {
      LeanWorkflow.isPush = false;
      LeanWorkflow.stations[0].velocity = 0.01;
      LeanWorkflow.pullTime = 0;
      LeanWorkflow.calcQueue =  LeanWorkflow.calcTimeToClearQueue();
    }

    LeanWorkflow.timeUp = function () {
      LeanWorkflow.simTime += 1;
      LeanWorkflow.pullTime += 1;
      if (!LeanWorkflow.isPush && LeanWorkflow.pullTime >= LeanWorkflow.calcQueue + 1) {
        LeanWorkflow.stations[0].velocity = LeanWorkflow.stations.reduce((prev, curr) => {
          return prev < curr.velocity ? prev : curr.velocity;
        })
      }
      console.log("Timer per second", LeanWorkflow.simTime);
      if (!LeanWorkflow.checkValidate()) return;
      if (LeanWorkflow.simTime < 0) {
        alert("the amount is invalid, should be a positive number!");
        return;
      }
      var timeleft = LeanWorkflow.simTime;
      var length = LeanWorkflow.stations.length;
      LeanWorkflow.stations[0].product += 1 * LeanWorkflow.stations[0].velocity;
      for (var i = 1; i < length; i++) {
        var eachStationTime = timeleft;

        let left = eachStationTime - 1 / LeanWorkflow.stations[i - 1].velocity;
        timeleft = left > 0 ? left : timeleft;

        var r = LeanWorkflow.calculateQueue(LeanWorkflow.stations[i - 1].product, timeleft, LeanWorkflow.stations[i].velocity, i);
        LeanWorkflow.stations[i].product = r;
        console.log(".>>>", LeanWorkflow.stations[i].product);
        // LeanWorkflow.stations[i].product = LeanWorkflow.stations[i].product;
        // console.log(".>>>", LeanWorkflow.stations[i].product);
      }
      LeanWorkflow.calcFirstCycle();
      LeanWorkflow.firstCycle = LeanWorkflow.firstCycle;
      LeanWorkflow.totalOut = Math.floor(LeanWorkflow.stations[length - 1].product);

      LeanWorkflow.viewStations = [];
      LeanWorkflow.stations.map(s => {
        LeanWorkflow.viewStations.push(s);
      })
    };

    LeanWorkflow.calculateQueue = function (formerOutput, wt2, v2, i) {
      if (v2 * wt2 > formerOutput) {
        var q = 0;
        if (formerOutput == Math.floor(formerOutput)) {
          q = 1;
          //if(formerOutput != 0)
          //formerOutput = formerOutput - 1;
        }
        this.stations[i - 1].waiting = q;
        return formerOutput;
      } else {
        var waiting = Math.floor(Math.floor(formerOutput) - Math.ceil(v2 * wt2));

        //let waiting = Math.floor(formerOutput) + this.stations[i - 1].waiting - v2 * 1;

        this.stations[i - 1].waiting = waiting > 0 ? waiting : 0;
        if (wt2 < 0)
          return 0;
        return v2 * wt2;
      }
    };

    LeanWorkflow.isWorking = function (value, velocity) {
      if (value > Math.floor(value)) {
        return 'my-class';
      }
      if (velocity == 0) {
        return 'nullclass';
      }
    };

    LeanWorkflow.add = function () {
      var newone = { 'velocity': 0, 'product': 0, 'waiting': 0 };
      this.stations.push(newone);
    };

    LeanWorkflow.delete = function () {
      for (var i = 0; i < this.stations.length; i++) {
        if (this.stations[i].velocity == 0) {
          this.stations.splice(i, 1);
          return;
        }
      }
    }

    LeanWorkflow.calcTime = function () {
      if (!this.checkValidate()) return;
      if (this.amount != Math.floor(this.amount) || this.amount < 0) {
        alert("the amount is invalid, should be a positive int number!");
        return;
      }
      this.totalTime = 0;
      var length = this.stations.length;
      var bottleneck = 0;
      for (var i = 0; i < length; i++) {
        var currentStep = 1 / this.stations[i].velocity;
        if (currentStep > bottleneck) {
          bottleneck = currentStep;
        }
      }
      this.calcFirstCycle();
      this.totalTime = this.firstCycle + (this.amount - 1) * bottleneck;
      this.totalTime = this.totalTime;
      LeanWorkflow.lastProductLeadTime = LeanWorkflow.totalTime - (LeanWorkflow.amount - 1) / LeanWorkflow.stations[0].velocity;
    };

    LeanWorkflow.calcFirstCycle = function () {
      this.firstCycle = 0;
      var length = this.stations.length;
      for (var i = 0; i < length; i++) {
        var currentStep = 1 / this.stations[i].velocity;
        this.firstCycle = this.firstCycle + currentStep;
      }
      console.log(this.firstCycle);
    }

    LeanWorkflow.checkValidate = function () {
      var length = this.stations.length;
      for (var i = 0; i < length; i++) {
        var index = i + 1;
        if (this.stations[i].velocity <= 0) {
          alert("No." + index + " station velocity is Invalid!");
          return false;
        }
      }
      return true;
    }

    LeanWorkflow.calcTimeToClearQueue = function () {
      var bottleNeckTime = 0;
      console.log("bottleNeckTime:" + bottleNeckTime);
      var bottleNeckIndex;
      var length = this.stations.length;
      var firstRoundTimeCost = 0;
      for (var i = 1; i < length; i++) {
        var curStationTime = 1 / this.stations[i].velocity;
        if (curStationTime > bottleNeckTime) {
          bottleNeckTime = curStationTime;
          bottleNeckIndex = i;
        }
        //firstRoundTimeCost = firstRoundTimeCost + 1/this.stations[i].velocity;
      }
      console.log("firstRoundTimeCost:" + firstRoundTimeCost);
      var totalQueueBN = 0;
      for (var j = 1; j < bottleNeckIndex; j++) {
        totalQueueBN = totalQueueBN + this.stations[j].waiting;
      }
      console.log("totalQueueBN:" + totalQueueBN);

      var timeAfterBN = 0;
      for (var k = bottleNeckIndex + 2; k < length; k++) {
        timeAfterBN = timeAfterBN + 1 / this.stations[k].velocity;
      }
      LeanWorkflow.calcFirstCycle();
      var timeToClearQueue = totalQueueBN * bottleNeckTime + timeAfterBN;
      var timeToStartPull = timeToClearQueue - LeanWorkflow.firstCycle;
      console.log("timeToStartPull:" + timeToStartPull);
      console.log("timeToClearQueue: " + timeToClearQueue);

      return timeToClearQueue;
    }

  }]);
