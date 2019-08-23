import axios from 'axios';

class Api {
    baseAxios = axios.create({
        baseURL: 'http://192.168.12.140/clocksapp'
    });

    // Create another method for Master if changes are too extensive or if new api call is needed
    postTime (postObj) {
        return this.baseAxios.get(`/timer`, {
            time: `${postObj.hours}:${postObj.minutes}:${postObj.seconds}`,
            fulltime: postObj.timerTime,
            id: postObj.id,
            stop: false,
            pause: false
            // Send time to start
            // Set stop: true or false
            // set pause: true of false
        });
    }
    postPower (postObj) {
        return this.baseAxios.get(`/powerBtn`, {
            on: postObj.power
        });
    }
    postBright (postObj) {
        return this.baseAxios.get(`/dim`, {
            bright: postObj.bright
        });
    }
    postSync (postObj) {
        return this.baseAxios.get(`/sync`, {
            sync: postObj.sync
        });
    }
    postMil (postObj) {
        return this.baseAxios.get(`/milTime`, {
            mil: postObj.mil
        });
    }
};

export default new Api();