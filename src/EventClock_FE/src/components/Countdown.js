import React, { Component } from "react";
import { connect } from 'react-redux';
import mapReduxStoreToProps from '../redux/mapReduxStoreToProps';
import Api from '../api';

class Countdown extends Component {
  state = {
    timerOn: false,
    timerStart: 0,
    timerTime: 0,
    timerID: '',
    inputHrs: 0,
    inputMin: 0,
    inputSec: 0,
  };

  preStart = () => {
    this.setState({
      timerTime: this.props.store.currentTime.timerTime,
    }, () => {
      // Setting up post for api call, needs to match endpoint titles and information
      Api.postTime({
        ...this.props.store.currentTime,
        id: this.props.id,
        status: 'start'
      })
      // Then is a response to make sure that it was successful to hit api
      .then((response) => {
        window.setTimeout(() => {
          this.startTimer()
        }, 2000);
      })
      // Catch is an error... its just an error
      .catch((error) => {
        console.log('Error on preStart for Countdown.js', error);
      });
      // Remove when endpoints are working
      window.setTimeout(() => {
        this.startTimer()
      }, 2000);
    });
  }

  startTimer = () => {
    // TODO: Use npm install "axios" for ajax call to backend
    this.setState({
      timerOn: true,
      timerStart: this.state.timerTime
    });
    
    this.timer = setInterval(() => {
      const newTime = this.state.timerTime - 10;
      if (newTime >= 0) {
        this.setState({
          timerTime: newTime
        });
      } else {
        clearInterval(this.timer);
        this.setState({ timerOn: false });
        alert("Countdown Ended");
      }
    }, 10);
  };

  stopTimer = () => {
    clearInterval(this.timer);
    this.setState({ timerOn: false });
  };

  resetTimer = () => {
    this.setState({
      timerTime: this.state.timerStart
    });
  };

  startForMaster() {
    this.props.resetMasterCallback();
    this.preStart();
  }

  render() {
    let { timerTime, timerStart, timerOn } = this.state;
    let disableButtons = false;

    if (this.props.store.masterTime.timerOn === true) {
      timerTime = this.props.store.masterTime.timerCount;
      timerStart = this.props.store.masterTime.timerStart;
      timerOn = this.props.store.masterTime.timerOn;
      disableButtons = true;
    }
    
    let seconds = ("0" + (Math.floor((timerTime / 1000) % 60) % 60)).slice(-2);
    let minutes = ("0" + Math.floor((timerTime / 60000) % 60)).slice(-2);
    let hours = ("0" + Math.floor((timerTime / 3600000) % 60)).slice(-2);

    return (
      <div id={this.props.id} className="roomClock">
        <div className="roomClock-hd">{this.props.id}</div>
        <div className="roomClock-bd">
          <div className="timer">
            <div className="timer-display">
              {hours} : {minutes} : {seconds}
            </div>
            <div className="timer-control">
              {timerOn === false &&
                (timerStart === 0 || timerTime === timerStart) && (
                  <button className="btn btn_start" onClick={this.preStart} disabled={disableButtons}>Start</button>
                )}
              {timerOn === true && timerTime >= 1000 && (
                <button className="btn btn_stop" onClick={this.stopTimer} disabled={disableButtons}>Stop</button>
              )}
              {timerOn === false &&
                (timerStart !== 0 && timerStart !== timerTime && timerTime !== 0) && (
                  <button className="btn btn_start" onClick={this.startTimer} disabled={disableButtons}>Resume</button>
                )}
              {(timerOn === false || timerTime < 1000) && (
                <button className="btn btn_reset" onClick={this.resetTimer} disabled={disableButtons}>Reset</button>
              )}
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default connect(mapReduxStoreToProps)(Countdown);
